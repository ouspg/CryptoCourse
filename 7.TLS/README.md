# Week 7 Exercises

This week’s exercises focus on TLS.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 1 | Getting to know TLS versions
Task 2 | 2 | Getting to know the vulnerabilities of SSL/TLS
Task 3 | 3 | Testing TLS connections with OpenSSL
Task 4 | 4 | Downgrading attack

## Task 1: Getting to know TLS versions ##

In this task you will familiarise yourself with the TLS versions 1.1, 1.2. and 1.3.

**1.1** Find the RFC documents related to different TLS versions [1.1](https://tools.ietf.org/html/rfc4346), [1.2](https://tools.ietf.org/html/rfc5246), [1.3](https://tools.ietf.org/html/rfc8446). Read at least the parts that specify major differences to the previous version and the Mandatory cipher suites parts.

**1.2** List the major differences in the three different versions. Use a table with the different versions as columns and then label rows as you best see fit to demonstrate the differences.

> Answer the questions above. Reference any outside sources that you have used.

## Task 2: Getting to know the vulnerabilities of SSL/TLS ##

Go to the Common Vulnerabilities and Exposures (CVE) [website](https://cve.mitre.org/). Search for vulnerabilities in the TLS protocol and different versions (1.1, 1.2, 1.3).

**2.1** Which version has the most listed vulnerabilities in the CVE database?

**2.2** What is the most severe vulnerability listed for each version of TLS? Severity can be measured with the [CVSS](https://nvd.nist.gov/vuln-metrics/cvss) and this information can be accessed by clicking the *Learn more at National Vulnerability Database (NVD)* -link from the CVE listing. How does the vulnerability work? What cryptographic primitive (if any) is affected? At what level of abstraction does the vulnerability appear (theoretical, protocol or implementation)? What types of applications does it impact? Can you find tools/code from the Internet that implement this attack? Are there any news on this vulnerability being used in some data breach/attack?

**2.3** What is the most recent vulnerability listed for each version of TLS? How does the vulnerability work? What cryptographic primitive (if any) is affected? At what level of abstraction does the vulnerability appear (theoretical, protocol or implementation)? What types of applications does it impact? Can you find tools/code from the Internet that implement this attack? Are there any news on this vulnerability being used in some data breach/attack?

Feel free to expand the table from Task 1 with the information from this task.

> Answer the questions above. Reference any outside sources that you have used.

## Task 3: Testing TLS connections with OpenSSL ##

In this task you are to test a website of your choosing with the help of OpenSSL. The OpenSSL Cookbook section 2: [Testing TLS with OpenSSL](https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html) will be **very helpful** in this task. 

You can also use `nmap` and suitable scripts like [this](https://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html). Yet another great tool is [testssl.sh](https://github.com/drwetter/testssl.sh) for this kind of testing. If you know more helpful tools, you are allowed to use them. Document their usage.

**Be mindful that some methods of testing may be invasive and may be considered 'hostile' by the server. If you choose to use such tools, please test only sites that approve of this type of testing e.g. have an active bug bounty program**. You can always ask the course staff for advice, if you need any assistance.

We have provided one website for you that you can test without any limits: https://tlstest.rahtiapp.fi

**3.1** Choose a website that supports HTTPS/TLS. What versions of TLS are supported? What ciphersuites are supported? Are there any preferences set by the website? (e.g. in what order are ciphers selected?)

**3.2** Test how low you can go with TLS connections (you can try even SSL, if you feel like it). What is the lowest version of TLS (or SSL) that is supported by the website?

**3.3** Go back to Task 2 and the different vulnerabilities listed for TLS. Does it seem that the website you are testing could be vulnerable to some of the known CVEs? For example `testssl.sh` shows some potential CVEs directly. Look for some of them if you did not report them previosly. What is the severity of CVE? What it allows attacker to do? **Beware that even if analysis script shows potential CVEs, you might always need to verify it manually before claming that the site being vulnerable. Unless you know exactly how script is testing it.**

> Answer the questions and provide any code/scripts that you used in testing the systems. You can provide snippets of the TLS tests that you run with OpenSSL.


## Task 4: Downgrading attack ##

In the previous tasks you might have noticed that the legacy versions are probably the biggest threat for compromising the security of TLS.

Many systems are intentionally (and maybe unintentionally) supporting older versions of TLS to maintain compatibility for various different clients for providing the best user experience. While from the point of perspective of user usability this could be great, this comes with significant security issues.

If we look at the [Shodan](https://www.shodan.io/) data from Finland (based on geolocation), we can see many web servers supporting deprecated TLS versions:

```console
shodan stats --facets ssl.version country:FI has_ssl:true HTTP
Top 6 Results for Facet: ssl.version
tlsv1.2                          184,237
tlsv1.1                          102,137
tlsv1                             97,097
tlsv1.3                           65,446
sslv3                             10,282
sslv2                              1,159
```

Could we knowingly force specific clients to use older, dangerous versions of TLS instead of their latest supported version?

### Task 4.1. Implement downgrading attack with non-transparent TCP proxy

To be able to implement downgrading attack for specific client and server, attacker should be able to intercept and modify the traffic. In the most of the cases, attacker has no possibility to change the behavior of client, hence it must implement man-in-the-middle attack and remain undetected.

Any link, hop or router between the client and destination server could be usable for a such scenario.

In this task, we will implement a **proxy server** on the provided virtual machine to demonstrate such a link and modify traffic on the fly. In practice, it could be any router or link, client might not notice anything.

It is recommended to use provided virtual machine, unless you know what you are doing.

Take a look for initial source code of the [proxy](tls_mitm.py). You should modify it further to implement downgrading attack. 

#### Pre-requisites

Following modifications for virtual machine are required that traffic is correctly redirected through proxy.
They will reset on reboot (except groupadd).

Run following commands as root (Run `sudo su` to change into root user):

Enable IP forwarding:
```console
sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv6.conf.all.forwarding=1
```

Prevent ICMP redirects:
```console
sysctl -w net.ipv4.conf.all.send_redirects=0
```

Create testing group, which is not affected by the routing table to prevent circularity (process must by launched by user which has this group as primary group):

```console
groupadd tlstesting && \
usermod -a -G tlstesting crypto  # Append group to user, crypto is our non-root user
```

Modify routing table to redirect any request from ports 80 or 443 into our proxy at the port 8080
```console
iptables -t nat -A OUTPUT -p tcp -m owner ! --gid-owner tlstesting --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -A OUTPUT -p tcp -m owner ! --gid-owner tlstesting --dport 443 -j REDIRECT --to-port 8080
ip6tables -t nat -A OUTPUT -p tcp -m owner ! --gid-owner tlstesting --dport 80 -j REDIRECT --to-port 8080
ip6tables -t nat -A OUTPUT -p tcp -m owner ! --gid-owner tlstesting --dport 443 -j REDIRECT --to-port 8080
```

Return to regular user, activate group changes and set `tlstesting` as primary group:
```console
newgrp tlstesting
```

From now on, the proxy must be running for those ports to work.

In the case of problems or when you stop using the proxy, you can reset iptables with command `iptables -t nat -F`. Note that this will also remove prior custom modifications.

If endless circulation seems to happen when running the proxy code, make sure that group changes are activated (run `id` command and see if you are part of `tlstesting` group and that is primary group.)

#### Goal

The great starting point for getting to know how TLS packets are handled on byte level, is [this website](https://tls.ulfheim.net/). And Wikipedia...

Your main goal is to identify supported TLS versions and ciphers from data analysis, finally dropping connections in such a way, that client will establish connection with lower TLS version than it supports with the target server. In practice, this is not that many lines of *correct* code.

You can further modify proxy code to only alter the target server traffic.

#### Target

Use server https://tlstest.rahtiapp.fi as your target. What is the lowest supported TLS/SSL version?

Server does not use `TLS_FALLBACK_SCSV` mechanism to prevent downgrading. However, you might need to use specific client anyway to be able to accept TLSv1 connections. Virtual machine has Docker installed, if you need some really old versions for some cases.

### Task 4.2. Downgrade attack and existing vulnerabilities

The target website has some potential vulnerabilities. Give some examples how attacker can further use downgrade attack to compromise potentially otherwise secure system or client data.

Find some proof of concept (PoC) code from GitHub or other place which could be potentially used to exploit identified vulnerabilities. Reference these with links.

### Task 4.3. Applying protection

 How TLS 1.3 is protecting from downgrade attacks? How is this better/is this different than previous mechanism ([RFC7507](https://tools.ietf.org/html/rfc7507))?

> Return modified source code, answer the questions and provide required information.
