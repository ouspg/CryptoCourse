# Week 2 Exercises


## Environment

You should have access into `openssl` toolkit, with recommended version of 1.1.1 at minimum to be able to complete tasks 1-2. In general, it is only available from the Linux/Unix based systems.

The course virtual machine is suitable.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

[Task](Task) #|Grade|Description|
-----|:---:|-----------|
Task 1 | 1 | Generating public keys with OpenSSL
Task 2 | 2 | Generating certificate signing requests with OpenSSL
Task 3 | 3 | Generating symmetric keys with limited randomness and brute forcing the key.
Task 4 | 4 | Security level analysis of your favorite application

## Task 1: Generating public keys with OpenSSL

OpenSSL can be used to generate different kind of asymmetric key-pairs. In this task, we will try out RSA,ECDSA and *legacy* DSA algorithm.

**Task 1.1.** Generate RSA and ECDSA/DSA keys of *different lengths* with OpenSSL. Private keys are required for time measurement.

Use both legacy commands (`genrsa` & `dsaparam/gendsa`) and newer commands (`genpkey`) and finally compare the results and the time it takes to generate the keys. It is recommended to try relatively high key length to notice difference (RSA).

Note, that with legacy commands you are expected to generate RSA and DSA keys. With newer commands you should generate RSA and ECDSA keys.

 We are mainly interested on the differences and practical use of OpenSSL on here - DSA/ECDSA can be considered as weak algorithms in these days, they are very dependent on the [PRNG of the operating system when signing messages](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm#Sensitivity), while DSA being already officially deprecated by OpenSSL because of the low key length requirements.

You might need to use some additional commands, to generate the public keys only.

On Linux, you can measure time with `time` command. To see explanation of produced output, you can reference [here.](https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1/556411#556411)

**Task 1.2.** Different commands (legacy vs. new) might be using different Public-Key Cryptography Standards (PKCS) output format. Which ones have been used? What binary format is the newer one representing?

**Task 1.3.** What command can you use to read generated private keys in text format?

> Answer the questions and include all possible commands you used on your answers. Return your public keys (and public keys only!) as a mark of completion of this task.


## Task 2: Generating certificate signing requests with OpenSSL

Generate a certificate signing request (CSR) for one or more of the keys that you have generated in the Task 1.

Double-check the certificate request by printing it in text format.

> Return the CSR(s) as a mark of completion of this task.

## Task 3: Generating symmetric keys with limited randomness and brute forcing the key.

Pick a programming language and a cryptographic library. The course virtual machine includes Python 3 and PyCryptodome. Feel free to use any other languages you are more familiar with. However, the course virtual machine does not have everything and you might need to install more by yourself.

Pick a symmetric encryption algorithm (e.g. AES) and generate keys with limited randomness (10, 20 and 30 bits (or 1-4 bytes)  at least, you can go up from that if you want). Remember that you need to still fullfil the required key length for selected encryption algorithm.

Encrypt some data with the key, delete the key from memory and try to brute force the key to open the data. 

 * You can run the tests several times (10-1000) and compute the average time it takes to brute force the key.
 * You can work in pairs / small groups and provide the encrypted data as a challenge to your fellow students. What information do you need to give in addition to the encrypted data to make brute forcing possible?

> Document your process and add results in a table, answer the questions and provide the source code. You can also add some screenshots of your work.

> Remember to mention the members of your group, in case one was formed.

