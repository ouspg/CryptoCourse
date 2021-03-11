# Week 2 Exercises

This week’s exercises focus on key generation, brute forcing and security assumptions.

First two tasks are heavily using OpenSSL from  thecommand-line, and the book [OpenSSL Cookbook 3ed Online](https://www.feistyduck.com/library/openssl-cookbook/online/) could be very useful.

## Environment

You should have access into Linux/Unix environment to be able to complete Tasks 1-2.

The course virtual machine is suitable.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Generating public keys with OpenSSL
Task 2 | 3 | Generating certificate signing requests with OpenSSL
Task 3 | 4 | Generating symmetric keys with limited randomness and brute forcing the key.
Task 4 | 5 | Security level analysis of your favorite application

## Task 1 

Generate RSA and ECDSA public keys of different lengths with OpenSSL. Use both legacy commands (genrsa & dsaparam/gendsa) and newer commands (genpkey) and compare the results and the time it takes to generate the keys.

## Task 2

Generate a certificate signing request (CSR) for one or more of the keys that you have generated in Task 1. Return the CSR(s) as a mark of completion of this task.

## Task 3

Pick a programming language and a cryptographic library. The course virtual machine includes Python 3 and PyCryptodome. Feel free to use any other languages you are more familiar with.

Pick a symmetric encryption algorithm (e.g. AES) and generate keys with limited randomness (10, 20 and 30 bits (or 1-4 bytes)  at least, you can go up from that if you want). 

Encrypt some data with the key, delete the key from memory and try to brute force the key to open the data. 

 * You can run the tests several times (10-1000) and compute the average time it takes to brute force the key.
 * You can work in pairs / small groups and provide the encrypted data as a challenge to your fellow students. What information do you need to give in addition to the encrypted data to make brute forcing possible?

> Document your results in a table, answer the questions and provide the source code. You can also add some screenshots of your work.


## Task 4

Pick an application (such as a secure messaging application, VPN system etc.) and identify its crypto schemes, key length, and respective security levels. Your analysis can be based on marketing material, blog posts, websites, research papers or code analysis (if the application has open source code).

Report your findings (with references to sources) in a brief (1-2 A4 pages) document. Use figures and/or tables, if necessary.

An example structure for this type of document could be

1. Introduction
    * The name and type of application (HW/SW, VPN/messaging/firewall/home appliance…)
    * The reason you picked this application
    * The intended use of the application

2. Cryptography
    * What (data) is protected?
    * What algorithms are used?
    * What key lengths?
    * What arguments (if any) are given in support of using the above algorithms and key lengths?
3. Analysis
    * What is the level of security provided in the system based on your analysis?
    * Are there any gaps and/or discrepancies between different cryptographic primitives?
    * (optional) How could the security of the cryptography be improved?
4. References
    * Give a list of all the reference material that you have used. Please reference these also in the text so that we can see, where each bit of information has been collected.
