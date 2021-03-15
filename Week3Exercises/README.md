# Week 3 Exercises

This week’s exercises focus on block ciphers.

*Pages 53-75* from the course book could be helpful for this exercise. It is available in the library of the University of Oulu in [digital format](https://oula.finna.fi/Record/oy_electronic_oy.9917612964306252).

## Environment

You should have access into Linux/Unix environment to be able to complete the final task.

The course virtual machine is suitable.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Modes of operation
Task 2 | 3 | Wrong model type of attack
Task 3 | 4 | Forged cipher
Task 4 | 5 | Padding oracle

## Task 1: Modes of operation

Pick a programming language and a crypto library that supports AES.

Take a short message with two identical message blocks (e.g. all zeroes).

Encrypt this message using three different modes of operation ECB, CBC and CTR. Compare the encryptions of the first and second message blocks.

## Task 2: Wrong model type of attack


## Task 3: Forged cipher

## Task 4: Padding oracle

Failed CBC encryption implementation could lead for catastrophic consequences. Implementation fail could be as little as telling when decryption of given ciphertext is successful or not, by checking on if decryption provides plaintext with valid padding.

Take a look for padding oracle attack in the course book, on the page 74.

You are given a ciphertext and binary as a command-line application which is demonstrating the interface for possible bigger software implementation. Make a padding oracle attack and decrypt the given ciphertext. 

Provided binary is using `AES-128` encryption with `PKCS#7` padding. Initialization vector is in the ciphertext as prefix.

Binary is named as `decryptor` in the [files](files) folder. Ciphertext is in raw binary format in the same folder.

> Return source code and the decrypted text. Describe shortly, how you could avoid this attack by using different methods.

> If you are using existing tools for making the attack, you **need to write additionally step-by-step** guide, how the attack works in this context; what the tool is doing on your behalf. Include all commands and mention these tools.