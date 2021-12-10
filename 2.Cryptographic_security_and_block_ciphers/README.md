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
Task 3 | 3 | Forged cipher
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

## Task 2: Digital COVID Certificate

COVID-19 has been a nuisance of the past two years. 
Just recently, there has been a lot of discussion and usage of the COVID-19 Passport on verification of the vaccasine status, confirmation of recent Rapid Antigen Test (RAT) or Nucleic acid aplification test (NAAT) and confirmed recovery status.

But how does it work? In this exercise, we will take a brief look on practical public-key cryptography and its usage on certificate generation and signing.
We don't try to understand the underlying math and potential problems; at least yet.
Finally, we demonstrate a simple application of COVID-19 Password and how one could be created. 
How safe it is?

### Task 2.1. Public-key generation

The main advantage of public key cryptography was the requirement of two different keys; public key can be used for encryption but only the private key can decrypt the data. 
Hence, you can share the public key for everyone to secure the data, but only the owner of the private key can access it.

Public-key cryptography is not only limited for encryption; authentication is an another important concept.
Public keys can be used for creating *digital certificate* for the data; with purpose of verifying the origin of the data with the public key.
Compare also with *digital signature*; it verifies the authenticity of the data but not always the entity behind the data.

Your first task is to create different kind of public-private (also called asymmetric) key-pairs, by using different cryptographic algorithms.
Later some of these keys are used for creating the digital certificate.

#### Task 2.1.1. Generate RSA and ECDSA keys of different lengths with OpenSSL. Private keys are required for time measurement.

Use both legacy command `genrsa` and newer commands `genpkey` for creating the RSA keys.
For ECDSA keys, use `ecparam` command.

Compare the results and the time it takes to generate the keys.
It is recommended to try relatively high key length to notice difference (RSA).

*For ECDSA, use at least `secp256r1` curve, we will use these keys later on.*
For comparison, you could try to use `Curve25519` for ECDSA as well.

Note, that with legacy commands you are expected to generate RSA and DSA keys. With newer commands you should generate RSA and ECDSA keys.

We are mainly interested on the differences and practical use of OpenSSL on here - DSA/ECDSA can be considered as weak algorithms in these days, they are very dependent on the PRNG of the operating system when signing messages, while DSA being already officially deprecated by OpenSSL because of the low key length requirements.

You might need to use some additional commands, to generate the public keys only.

On Linux, you can measure time with time command. To see explanation of produced output, you can reference here.

#### Task 2.1.2. Different commands (legacy vs. new) might be using different Public-Key Cryptography Standards (PKCS) output format. Which ones have been used? What binary format is the newer one representing?

> Answer the questions and include all possible commands you used on your answers. Return your public keys (and public keys only!) as a mark of completion of this task.



OpenSSL Cookbook could be very useful in this exercise.




You can also take a look on the sample implementation of eHN-S protocol which is available [here.](https://github.com/ehn-dcc-development/ehn-sign-verify-python-trivial)


Format:
base45-encoded QR code and decoding CBOR to JSON
Base45 for QR required

Spec : https://github.com/ehn-dcc-development/hcert-spec
Finland test data: https://github.com/eu-digital-green-certificates/dgc-testdata/tree/main/FI




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
