import socketserver
import socket
import struct
import logging
import argparse
import select
import sys
import enum


class TLSProxyHandler(socketserver.BaseRequestHandler):

    logger = logging.getLogger("TLSProxyHandler")
    timeout = 10.0  # In seconds
    # For tls content types see for example https://tools.ietf.org/html/rfc5246#appendix-A.1
    # Or https://en.wikipedia.org/wiki/Transport_Layer_Security
    tls_content_type = {
        20: "change_cipher_spec",
        21: "alert",
        22: "handshake",
        23: "application_data",
        24: "heartbeat",
    }

    def _handle_tls_record(self, _socket: socket.socket):
        """Method for handling potential TLS packet and making actions based on data

        TODO implement downgrading attack

        Detect supported TLS versions
        Detect supported ciphers

        Drop connections in such a way to web server thinks we support only the lowest available.
        You might need to edit code elsewhere as well.

        """

        # TLS record header length is 5 in general
        # Can you use content type to identify when we get TLS record, and what it contains?
        # For great tutorial see https://tls.ulfheim.net/
        self.raw_data = _socket.recv(5)
        if len(self.raw_data) < 5:
            self.logger.debug("Not enough data to be TLS record...")
            return

        self.raw_data += _socket.recv(1024 ** 64)

    def handle(self):
        """Handle incoming request. New thread is instanced automatically for separete sources.
        Request could be in ipv4 or ipv6 address format
        """
        SO_ORIGINAL_DST = 80
        is_ipv4 = "." in self.request.getsockname()[0]
        if is_ipv4:
            dst = self.request.getsockopt(socket.SOL_IP, SO_ORIGINAL_DST, 16)
            _dst_port, raw_ip = struct.unpack_from("!2xH4s", dst)
            _dst_host = socket.inet_ntop(socket.AF_INET, raw_ip)
        else:
            dst = self.request.getsockopt(SOL_IPV6, SO_ORIGINAL_DST, 28)
            _dst_port, raw_ip = struct.unpack_from("!2xH4x16s", dst)
            _dst_host = socket.inet_ntop(socket.AF_INET6, raw_ip)

        self.logger.info(f"New connection from {self.client_address[0]}")
        self.logger.info(f"Connection destination is {_dst_host}:{_dst_port}")

        # Let's see initial request data
        self._handle_tls_record(self.request)
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.forward.connect((_dst_host, _dst_port))

        # Make type definition of 'request' and 'forward' source
        socket_direction = enum.Enum(
            "SocketDirection",
            {
                "Initial Source": self.request,
                "Final Destination": self.forward,
            },
        )

        if self.raw_data:
            self.forward.sendall(self.raw_data)
        else:
            return

        while True:
            readable, writable, errors = select.select(
                (self.request, self.forward),
                (),
                (self.request, self.forward),
                self.timeout,
            )
            if len(errors) > 0:
                error_source = socket_direction(errors[0])
                self.logger.error(f"Error on socket {error_source.name}")
                break

            for rsock in readable:
                # Socket where data is sent
                ssock = None
                self._handle_tls_record(rsock)
                if not self.raw_data:
                    return
                if rsock == self.forward:
                    ssock = self.request
                else:
                    ssock = self.forward

                self.logger.debug(
                    f"Forwarding TLS record from {socket_direction(rsock).name} into {socket_direction(ssock).name} with length of {self.length} and content type {self.text_content_type}"
                )
                ssock.sendall(self.raw_data)


class TLSProxy(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


def main():

    logger = logging.getLogger("main")
    # Proxy is running on localhost, port 8080
    _lhost = "127.0.0.1"
    _lport = 8080
    logger.info(f"Initializing proxy server on {_lhost}:{_lport}")
    server = TLSProxy((_lhost, _lport), TLSProxyHandler)
    server.serve_forever()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-l",
        "--log",
        dest="log_level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level",
        default=None,
    )
    if len(sys.argv) >= 1:
        args = parser.parse_args(args=sys.argv[1:])
    if len(sys.argv) > 2:
        print("Warning: Too many program arguments provided, they have been ignored.")

    log_level = args.log_level if args.log_level else "INFO"
    if log_level not in {"DEBUG"}:
        sys.tracebacklimit = 0  # avoid track traces unless debugging
    logging.basicConfig(
        format=f"%(asctime)s %(levelname)s - %(name)s: %(message)s",
        level=getattr(logging, log_level),
    )
    main()

    # run for example python3 tls_mitm.py -lDEBUG to run in debug mode
