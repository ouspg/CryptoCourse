# Week 2: Cryptographic security and block ciphers

This week’s exercises focus on block ciphers, public-private key generation and practical use of certificates.

*Pages 53-75* from the course book could be helpful for block cipher related assignments. It is available in the library of the University of Oulu in [digital format](https://oula.finna.fi/Record/oy_electronic_oy.9917612964306252).

Second and third task are heavily using [OpenSSL](https://www.openssl.org/) from the command-line, and the book [OpenSSL Cookbook 3ed Online](https://www.feistyduck.com/library/openssl-cookbook/online/) could be very useful.

## Environment

You should have access into Linux/Unix environment to be able to complete the final task.

The course virtual machine is suitable.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

[Task](Task) #|Grade|Description|
-----|:---:|-----------|
Task 1 | 1 | Modes of operation
Task 2 | 2-3 | Digital COVID Certificate
Task 3 | 3 | Forged cipher (alternative)
Task 4 | 4 | Padding oracle

## Task 1: Modes of operations in block ciphers

Let's have a practical look at different modes of operations.

**Task 1.1.** Pick a programming language and a crypto library that supports AES.

Take a short message with two identical message blocks (e.g. all zeroes). Notice that AES has a block length of 128 bits.

Generate a suitable key (e.g. 128 bits) to use with AES. 

Encrypt your message using three different modes of operation ECB, CBC and CTR with the same key. Compare the encryptions, from the part of the first and second identical message blocks. Describe the results. 

Explain also shortly the purpose of the nonce and possible salt in this case. Are they the same thing?

**Task 1.2.** What can you say about for example the indistinguishability properties of the three modes of operation? 

**Task 1.3.** Is there a difference in the overhead of the encrypted messages (i.e. are some messages longer/shorter than the original plaintext)?

> Include source code and answer the questions. You can highlight interesting comparison results with screenshots for example.

## Task 2: Digital COVID Certificate (DCC)

COVID-19 has been a nuisance of the past two years. 
Just recently, there has been a lot of discussion and usage of the COVID-19 Passport (or more precisely, The European Digital Covid Certificate (DCC)) on verification of the vaccasine status, confirmation of recent Rapid Antigen Test (RAT) or Nucleic acid aplification test (NAAT) and confirmed recovery status.

But how does it work? In this exercise, we will take a brief look on practical public-key cryptography and its usage on certificate generation and use cases. 
Finally, we demonstrate a simple application of DCC and how one simple implementation works. 

Note also that for example TLS certificates on your browser work by using similar principles.

### Task 2.1. Public and private key generation

The main advantage of public key cryptography was the requirement of two different keys; public key can be used for encryption but only the private key can decrypt the data. 
Public key can be derived from the private key but not the other way around (at least with the current state-of-the-art algorithms).
Hence, you can share the public key for everyone to secure the data, but only the owner of the private key can access it.

Public-key cryptography is not only limited for the encryption; authentication is an another important concept.
Private keys can be used for creating *the digital certificate* for the data; with purpose of verifying the entity behind the authentication (ownership) by using the corresponding public key.
Compare with *digital signature*: it verifies the authenticity of the data but not always the entity behind the data.

Your first task is to create different kind of public-private (also called asymmetric) key-pairs, by using different cryptographic algorithms.
Later some of these keys are used for creating the digital certificate.

#### Task 2.1.1. Generate RSA, ECDSA and EdDSA keys with OpenSSL. Both public and private keys are required.

Use both legacy command `genrsa` and newer command `genpkey` for creating the RSA keys.
For ECDSA keys, use `ecparam` command.
OpenSSL Cookbook could be very useful in this exercise.

Compare the results and the time it takes to generate the keys.
It is recommended to try relatively high key length to notice difference (RSA).

For ECDSA, use `secp256r1` curve as it is used as base for certificates later on.
For comparison, use `Curve25519` for ECDSA key generation as well.
Finally, generate `EdDSA` keys, by using also `Curve25519` to construct so-called `Ed25519` keys.

Note, that with legacy commands you are expected to generate only RSA keys. With newer commands you should generate other keys.

We are mainly interested on the differences and practical use of OpenSSL on here .
You might need to use some additional commands, to generate the public keys only.

On Linux, you can measure time with `time` command.

#### Task 2.1.2. Different commands (legacy vs. new) might be using different Public-Key Cryptography Standards (PKCS) output format. Which ones have been used?

#### Task 2.1.3. What are the practical differences of curves `secp256r1` and `Curve25519`? 

#### Task 2.1.4. Can you notice significant time differences between tested algorithms on key generation?

#### Task 2.1.5. Why DSA/ECDSA algorithm can be considered as problematic or even "weak"? Why is EdDSA (especially Ed25519) considered as better alterinative?

> Answer the questions and include all possible commands you used on your answers. Return your public keys (and public keys only!) as a mark of completion of this task.


### 2.2. Certificate sign requests and root of trust

In this task, we'll take a look for a so called **a chain of trust**; how different entities can be tied together by using other certificate as issuer for another one, to create so called certificate chains.
These certificates are created by using private keys; similar keys than we created in the previous task.

On DCC, trust chain contains usually three entities; Country Signing Certificate Authority (CSCA), Document Signer Certificate (DSC) and finally the electronic health certificate itself. 
CSCA can be usually thought as root certificate, DSC as intermediate certificate and DCC as end-entity certificate.

There can be one or more CSCA and DSC issuers per country.

#### Task 2.2.1. Generating certificate chains

Let's create a sample certification chain. 
Consult OpenSSL cookbook for certificate sign requests.

Your task is to create root certificate, intermediate certificate and end-entity certificate.
We will be using different key and key type for each certificate. 
This is only for testing purposes and you should use the best available algorithm in your real life scenario.

Workflow is the following. Use keys from the previous task.

  1. Use Ed25519 key for creating the root certificate
  2. Use ECDSA key with `secp256r1` curve for the intermediate certificate and use previous root certificate as issuer
  3. Finally use RSA key with at least 4096 bit key size for end-entity certificate. Use intermediate certificate as issuer.

  Note, that end-entity certificate should not be able to sign other certificates! Some `openssl` extensions are required.
  
  > Show commands and return certificates and as mark of completion of this part. Certificates will be used later on.
  
#### Task 2.2.2. Understanding and verifying certificate chains

If you are curious how DCC works in Finland:
  * Based on the [EU DCC.](https://dvv.fi/-/digi-ja-vaestotietovirasto-toteuttaa-eu-koronatodistusten-tarkastuspalvelun-suomeen?languageId=en_US)
  * "CSCA" in Finland for DCC (VRK CA for Social Welfare and Health Care Service Providers): https://dvv.fi/en/ca-certificates
    * Official CSCA, but for different purposes https://poliisi.fi/en/csca 
   
  * DCC:s in Finland are issued by Kela (kanta.fi), which is the final DSC issuer. More details available [here.](https://www.kanta.fi/en/system-developers/eu-koronatodistuksen-verifiointi)

Finnish DCC public certificate (Kela/kanta.fi cert) can be found from the international public list provided by Sweden, which is available [here.](https://dgcg.covidbevis.se/tp/)
Finland does not maintain similar public service themselves, according to kanta.fi technical support.

We will use that as an example.

By using command line, we can download public trust list of EU countries as following:
```console
curl https://dgcg.covidbevis.se/tp/trust-list | jq -R 'split(".") | .[0],.[1] | @base64d | fromjson' <<< $(cat "${JWT}") > trustlist.json
```
Trust list is in [JWT format](https://jwt.io/), which is correctly parsed with above command and actual JSON is generated into file `trustlist.json`.
We'll pass signature verification at this time, but you can do it if you want. JWT header contains algorithm information and the signature could be found from the final section.

Further, we can extract public certificate information of the Finland as following
```console
jq -s '.[1].dsc_trust_list.FI' trustlist.json 
```
Or extract the actual certificate in DER format:
```console
jq -sr '.[1].dsc_trust_list.FI.keys[0].x5c[0]' trustlist.json | base64 -d > fi.der
```

Now, we can read certificate contents with `openssl`. Note the correct data format.

Let's verificate the certificate chain:

 1. Get issuer information from the DER file, and find provided issuer from the https://dvv.fi/en/ca-certificates.
 2. Download this issuer certificate.
 3. Read information from the issuer certificate with `openssl` and find root certificate from the same place. Download it and read its information.

 At this point, we should have three different files. Root certificate, and two intermediate certificates.
 
 We can verify the whole current certificate chain with single `openssl verify` command.
 
 > Construct sample command, and provide it as completion of this part. Is certificate chain OK?


### Task 2.3. DCC verification and generation

At this point, we haven't touched the actual DCC yet. 
For the most people, this is seen as QR code which you download from the `kanta.fi` website.

We are not going too deep into the techinal details.

Following image showcases the high level data structure. (Source: HCERT spec)

![overview](https://github.com/ehn-dcc-development/hcert-spec/raw/main/overview.png)

The health data is signed with the certificate, which is issued by Kela and was downloaded from the Swedish trust list.

Primary signature algorithm in DCC is Elliptic Curve Signature Algorithm (ECDSA), by using P-256 parameters with combination of SHA256 hashing algorithm, as defined in the [HCERT specification(Electronic Health Certificate).](https://github.com/ehn-dcc-development/hcert-spec/blob/main/hcert_spec.md#332-signature-algorithm)
In the previous task we already generated suitable keys for this, by using *secp256r1* curve, which is [alias for NIST P-256/prime256v1.](https://tools.ietf.org/search/rfc4492#appendix-A)



You can also take a look on the sample implementation of eHN-S protocol which is available [here.](https://github.com/ehn-dcc-development/ehn-sign-verify-python-trivial)


Format:
base45-encoded QR code and decoding CBOR to JSON
Base45 for QR required

Spec : https://github.com/ehn-dcc-development/hcert-spec
Finland test data: https://github.com/eu-digital-green-certificates/dgc-testdata/tree/main/FI


More information

* Sample in [kanta.fi](https://www.kanta.fi/documents/20143/120102/mallitodistus_eu-rokotustodistus.pdf/f107fdfc-bfbc-6e0f-0bac-da56fbe01722?t=1624341191059)
* Collection of trustlits to find certificates for validating DCC available for example [here.](https://github.com/section42/hcert-trustlist-mirror)


## Task 3: Forged cipher (Alternative)?

In this task you will do a similar attack as in Week 1 Task 1, but against a real world secure encryption scheme. The message below is encrypted with AES (a secure standard for symmetric encryption) using a provably secure mode of operation. Yet, you should be able to modify the message according to the task below.

You have managed to intercept the following encrypted message:

`a7896ad1b2f7da8d40b33d1438e04a839a88b5c9a97625fe5017a5e1fb542072595d804d5ad1a3af11ea7244a39d76cde1`

You have information that tells you it is the unauthenticated encryption of the following message: 

`Move the tables to the patio as soon as possible!`

The intelligence also tells you that the encryption is done using AES encryption in Counter mode with a 128 bit key and an unknown (but fixed) initialization vector (IV). They also use plain ASCII encoding of their text before the actual encryption.

**Task 3.1.** Your challenge is to provide a ciphertext that decrypts to:

`Move the chairs to the house as soon as possible!`

Ciphertext should be in similar format than the original one. You can check that you have produced the correct one, comparing it to following sha256 hash:

> `102f853f3e0f38fa7ba7448e6933acaaec5c1bd975c93fc65bff4faa94d2ca34`

**Task 3.2.** What was the flaw here? Are we actually using block cipher here?

**Task 3.3.** What limitations you have on modifying the ciphertext?

> Include possible source code for producing the ciphertext and answer the questions.

## Task 4: Padding oracle

Failed CBC encryption implementation could lead for catastrophic consequences. Implementation fail could be as little as telling when decryption of given ciphertext is successful or not, by checking on if decryption provides plaintext with valid padding.

Take a look at the padding oracle attack in the course book, on the page 74.

You are given a ciphertext and an executable binary as a command-line application which is demonstrating the interface for possible bigger software implementation. Make a padding oracle attack and decrypt the given ciphertext. 

Provided binary uses `AES-128` encryption with `PKCS#7` padding. Initialization vector is in the ciphertext as a prefix.

Binary is named as `decryptor` in the [files](files) folder. It is expected to be executed on glibc enabled Linux environment. Ciphertext is in raw binary format in the same folder.

> Return source code and the decrypted text. Describe shortly, how you could avoid this attack by using different methods.

> If you are using existing tools for making the attack, you **need to write additionally step-by-step** guide, how the attack works in this context; what the tool is doing on your behalf. Include all commands and mention these tools.
