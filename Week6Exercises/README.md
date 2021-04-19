
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

## Task 2: Message and signature verification? ##
In this task you need to find correct messages and signatures. You are given files XXX and YYY that contain the messages and signatures under some private keys corresponding to public keys in the file ZZZ.

**2.1** Match all messages with correct signatures and public keys.

>Provide the matching pairs and any code that you used as your answer.

**2.2** What potential vulnerabilities there are if only textbook version of RSA is used to sign many (different) messages with the same key?

>Answer the question in short textual form.

## Task 3: ##

## Task 4: Roll your own public key cryptosystem ##
In most of the courses on cryptography that you will attend, the instrcutor will tell you that you should not roll your own cryptographic systems. There are of course good reasons for this warning.

But now that we are on a course that will give you some hands on experience on cryptography, maybe a little exercise in building your own cryptosystems might be in order.

In this task you need to describe a public key cryptosystem based on a hard problem of your own choice.

**4.1** Describe your public key cryptography algorithm by answering the following questions in a few sentences.
 * What problem is the hard problem that your system is based on?
 * What evidence is there that the problem is hard?
 * How does one use the problem to encrypt/sign (choose one) messages?

**4.2** Write a short code/pseudocode of your implementation. Can you estimate or evaluate how complex the process of encrypting or signing a message will be?

**4.3** Assume the role of an attacker. Write a short analysis on the possible attacks on your scheme. You should at least consider attacks that have been discussed in the course material (side channels, man-in-the-middle, etc.)

**4.4** Do a quick search on [Google Scholar](https://scholar.google.com/) with suitable keywords (e.g. "the name of your problem" + "cryptography/encryption/signature"). Write a short summary of your findings. Has the problem been used for cryptography before? Have any of the proposed schemes been broken?
 >Answer the questions above and provide all references to outside sources in your reporting.
