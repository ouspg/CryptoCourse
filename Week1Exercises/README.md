# Week 1 Exercises

This week’s exercises focus on classical ciphers and randomness.

Theory of the exercises are based on the book [Serious Cryptography](https://nostarch.com/seriouscrypto)

Pages 1-38 are relevant for this exercise and might good to read beforehand.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Fooling a perfect cipher
Task 2 | 3-4 | Generating randomness and testing randomness
Task 3 | 5 | Vigenere cipher


## Task 1: Fooling a perfect cipher

Recall that the one-time pad provides perfect secrecy i.e., there is nothing an adversary can learn from the cipher text even given unlimited computational resources. 

However, the perfect cipher provides no other guarantees and does not provide authentication.

You are given the following encryption of an ASCII encoded message “Hi Kimmo”. Each row in the table represents one character in binary and hexadecimal format.

Binary | Hex
--|--
01101001 | 69
00010101 | 15
01011111 | 5F
01001110 | 4E
00100000 | 20
00011100 | 1C
10101101 | AD
01100001 | 61

### Task 1.1 

Produce a ciphertext that will decode into “No Rauli” under the same secret one-time pad as the original ciphertext was produced.

### Task 1.2

Produce a ciphertext that will decode into a 7 character ASCII string of your choice.

### Task 1.3

What is the secret one-time pad in binary?
