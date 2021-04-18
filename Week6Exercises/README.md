
# Week 6 Exercises

This week’s exercises focus on hard problems and the RSA cryptosystem.

You can find related information from the book in pages 163-199. 

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | RSA encryption and signatures with OpenSSL 
Task 2 | 3 | Message and signature verification?
Task 3 | 4 | Math problems?
Task 4 | 5 | Roll your own public key crypto?

## Task 1: RSA encryption and signatures with OpenSSL ##

In this task you need to encrypt and sign a message with RSA. The [OpenSSL Cookbook](https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html) may be helpful in this task. You can also find more concise presentations  on who to do this on the command line with the help of your favorite search engine. The command most useful here is `rsautl`.

**1.1** Generate an RSA key of suitable length OR use one that you have previously generated. Generate a message and encrypt it using the public key.
> Provide the key and the message as your answer. Also show the commands that you used to encrypt the message.

**1.2** Use RSA to sign the message. 
> Provide the public key, the message and the signature as your answer. Also show the commands you used to generate the singature.

## Task 2: ##
In this task you need to find correct messages and signatures. You are given files XXX and YYY that contain the messages and signatures under some private keys corresponding to public keys in the file ZZZ.

**2.1** Match all messages with correct signatures and public keys.

>Provide the matching pairs and any code that you used as your answer.

**2.2** What potential vulnerabilities there are if only textbook version of RSA is used to sign many (different) messages with the same key?

>Answer the question in short textual form.

## Task 3: ##

## Task 4: ##
