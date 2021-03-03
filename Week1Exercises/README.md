# Week 1 Exercises

This week’s exercises focus on classical ciphers and randomness.

Theory of the exercises are based mainly on the book [Serious Cryptography](https://nostarch.com/seriouscrypto)

Pages *1-38* are relevant for this exercise and might good to read beforehand.

## Environment

You should have access into Linux environment to be able to complete task 3.
Course virtual machine is suitable.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Fooling a perfect cipher
Task 2 | 3 | Vigenere cipher
Task 3 | 4-5 | Generating randomness and testing randomness


## Task 1: Fooling a perfect cipher

Recall that the one-time pad provides perfect secrecy i.e., there is nothing an adversary can learn from the cipher text even given unlimited computational resources. 

However, the perfect cipher provides no other guarantees and does not provide authentication.

You are given the following encryption of an ASCII encoded message "Hi Kimmo". Each row in the table represents one character in binary and hexadecimal format.

Binary | Hex
--|--
0b01101001 | 0x69
0b00010101 | 0x15
0b01011111 | 0x5F
0b01001110 | 0x4E
0b00100000 | 0x20
0b00011100 | 0x1C
0b10101101 | 0xAD
0b01100001 | 0x61


**Task 1.1** Produce a ciphertext that will decode into "No Rauli" under the same secret one-time pad as the original ciphertext was produced.

**Task 1.2** Produce a ciphertext that will decode into a 8 character ASCII string of your choice.

**Task 1.3** What is the secret one-time pad in binary?

> You should return possible source code for how you solved the secret and produced the new ciphertexts. You should also explain shortly the idea of of your method.

## Task 2: Vigenere cipher

The following text is an English text that has been encrypted by using an unknown key with a Vigenere cipher. All punctuation and whitespaces have been removed from the text before encryption.

```
TRLSHAXRNSVKIENUFMEGRVDANEELHOFNSLUGIEFZVATAAGCIYAGIFADWUDHFYIFPOWVSPUMBKOTUOBYYNQWZYEEHBFCYCRZUKIPDZFFOYDBPZTPRBRVRFRBFYESLSXUAALBFIIAVWORLYBAAIAYGWYVNFLCZKHRVBANDRQFQMEYDHUFNFPCFZVNWSMIENVGQJSZHBFFFGKSBFLVWWORLNQRYFRNODAJIGLCZZNTRTOIYCWCSIACKMFYELOSMUOAHHARSXLTALRVQONZLVWMFFESISOKIIHZKRDQUSEJMNVGELRIHWXCAAFSOFNFWWFLTRVORRIYXFQFFBXFRZEYGWNVLVHJQKHNWWFUORVWORLYICDRCBPAGEIGBKUUERITAITGRRQMEYRDYFRRHTRVCGLJQDENQGFFRRVWEKMNVGELRIHWXCAAFSUGLRDRRFRNUSUEVRQHUFNBICGIDVVQUGLVQODPCHOHGIEGROFKEAGBAKOAOMFFPHCNXVSNQRYRTUEIFRLFRHAKHRVCOZEGDZUDPYLQMKIBQGAWOHUKAIK
```

**Task 2.1** Decrypt the text. What is the secret key?

**Task 2.2** Where is the text from? Who wrote it? If you find the source, read the whole text/article/newsitem/book...


> Show your work (code and reasoning; how did you decrypt this?). You should not use existing tools which can solve this quite quickly. However, if you did, mentions these tools **and** make step-by-step report **why** Vigenere cipher was decryptable. 

## Task 3: Generating randomness

Generate randomness to different files using different tools that you have access to or manually. Analyse those files with [dieharder](https://linux.die.net/man/1/dieharder) . Report your findings.