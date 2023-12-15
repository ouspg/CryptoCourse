# Week 2: Cryptographic security and block ciphers

This week’s exercises focus on block ciphers, public-private key generation and practical use of certificates.

*Pages 53-75* from the course book could be helpful for block cipher related assignments. It is available in the library of the University of Oulu in [digital format](https://oula.finna.fi/Record/oy_electronic_oy.9917612964306252).

Second and third task are heavily using [OpenSSL](https://www.openssl.org/) from the command-line, and the book [OpenSSL Cookbook 3ed Online](https://www.feistyduck.com/library/openssl-cookbook/online/) could be very useful.

## Environment

You should have access to the Linux/Unix environment to be able to complete the final task.

The course virtual machine is suitable.

## Grading

You are eligible for the following points from the exercise. Previous task(s) should be completed before going further.

[Task](Task) #|Grade|Description|
-----|:---:|-----------|
Task 1 | 1 | Modes of operation
Task 2 | 2 | Key generation
Task 3 | 3 | Forged cipher (alternative for 2.2 and 2.3)
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

## Task 2: Key generation

Let's have a look at how private and public keys are generated using OpenSSL.


### Task 2.1. Public and private key generation

The main advantage of public key cryptography was the requirement of two different keys; public key can be used for encryption but only the private key can decrypt the data. 
The public key can be derived from the private key but not the other way around (at least with the current state-of-the-art algorithms).
Hence, you can share the public key for everyone to secure the data, but only the owner of the private key can access it.

Public-key cryptography is not only limited for the encryption; authentication is another important concept.
Private keys can be used for creating *the digital certificate* for the data; with the purpose of verifying the entity behind the authentication (ownership) by using the corresponding public key.
Compare with *digital signature*: it verifies the authenticity of the data but not always the entity behind the data.

We will go more in details about public-private key cryptography later on the course.

Your first task is to create different kinds of public-private (also called asymmetric) key-pairs, by using different cryptographic algorithms.
Later some of these keys are used for creating the digital certificate.

#### Task 2.1.1 Generate RSA, ECDSA and EdDSA keys with OpenSSL. Both public and private keys are required.

Use both legacy command `genrsa` and newer command `genpkey` for creating the RSA keys.
For ECDSA keys, use the `ecparam` command.
OpenSSL Cookbook could be very useful in this exercise.

Compare the results and the time it takes to generate the keys.
It is recommended to try relatively high key lengths to notice differences (RSA).

For ECDSA, use the `secp256r1` curve as it is used as base for certificates later on.
For comparison, use `Curve25519` for ECDSA key generation as well.
Finally, generate `EdDSA` keys, by also using `Curve25519` to construct so-called `Ed25519` keys.

Note that with legacy commands you are expected to generate only RSA keys. With newer commands you should generate other keys.

We are mainly interested about the differences and practical use of OpenSSL here .
You might need to use some additional commands, to generate the public keys only.

On Linux, you can measure time with the `time` command.

#### Task 2.1.2. Different commands (legacy vs. new) might be using different Public-Key Cryptography Standards (PKCS) output formats. Which ones have been used?

#### Task 2.1.3. What are the practical differences between the curves `secp256r1` and `Curve25519`? 

#### Task 2.1.4. Can you notice significant time differences between tested algorithms on key generation?

#### Task 2.1.5. Why can the DSA/ECDSA algorithm be considered as problematic or even "weak"? Why is EdDSA (especially Ed25519) considered as a better alternative?

> Answer the questions and include all possible commands you used in your answers. Return your public keys (and public keys only!) as a mark of completion of this task.



## Task 3: Forged cipher

In this task you will do a similar attack as in Week 1 Task 1, but against a real world secure encryption scheme. The message below is encrypted with AES (a secure standard for symmetric encryption) using a provably secure mode of operation. Yet, you should be able to modify the message according to the task below.

You have managed to intercept the following encrypted message:

`a7896ad1b2f7da8d40b33d1438e04a839a88b5c9a97625fe5017a5e1fb542072595d804d5ad1a3af11ea7244a39d76cde1`

You have information that tells you it is the unauthenticated encryption of the following message: 

`Move the tables to the patio as soon as possible!`

The intelligence also tells you that the encryption is done using AES encryption in Counter mode with a 128 bit key and an unknown (but fixed) initialization vector (IV). They also use plain ASCII encoding of their text before the actual encryption.

**Task 3.1.** Your challenge is to provide a ciphertext that decrypts to:

`Move the chairs to the house as soon as possible!`

Ciphertext should be in a similar format than the original one. You can check that you have produced the correct one, comparing it to the following sha256 hash:

> `102f853f3e0f38fa7ba7448e6933acaaec5c1bd975c93fc65bff4faa94d2ca34`

**Task 3.2.** What was the flaw here? Are we actually using block cipher here?

**Task 3.3.** What limitations do you have on modifying the ciphertext?

> Include possible source code for producing the ciphertext and answer the questions.

## Task 4: Padding oracle

Failed CBC encryption implementation could lead to catastrophic consequences. Implementation failure could be as little as telling when decryption of a given ciphertext is successful or not, by checking if decryption provides plaintext with valid padding.

Take a look at the padding oracle attack in the course book, on page 74.

You are given a ciphertext and an executable binary as a command-line application which demonstrates the interface for possible bigger software implementation. Make a padding oracle attack and decrypt the given ciphertext. 

Provided binary uses `AES-128` encryption with `PKCS#7` padding. Initialization vector is in the ciphertext as a prefix.

Binary is named as `decryptor` in the [files](files) folder. It is expected to be executed on a glibc enabled Linux environment. Ciphertext is in raw binary format in the same folder.

> Return source code and the decrypted text. Describe shortly, how you could avoid this attack by using different methods.

> If you are using existing tools for making the attack, you **need to write additionally step-by-step** guide, how the attack works in this context; what the tool is doing on your behalf. Include all commands and mention these tools.
