# Week 4 Exercises

This week’s exercises focus on stream ciphers and hash functions.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Stream cipher usage
Task 2 | 3 | Partial collision of hash functions
Task 3 | 4 | Nonce reuse
Task 4 | 5 | MACs gone wrong

## Task 1: Stream cipher usage

Select a stream cipher and encrypt some text with the generated keystream by XORing the keystream to the plaintext.

**1.1.** Take the plaintext from Week 3 exercises task 3: "Move the tables to the patio as soon as possible!" and encrypt it with the keystream. Generate a ciphertext that will decrypt to "Move the chairs to the house as soon as possible!" under the same keystream (remember ASCII encoding etc.) Is there something similar in ciphertexts? Why/why not?

**1.2.** Encrypt a message of your choice with a key and a nonce of your choice. Use another key and the same nonce to encrypt another, slightly different message of your choice, e.g. change one letter to another. Can you spot any pattern in the cipher texts? Can you get any relation between the plaintexts out of the ciphertexts?

**1.3.** Compare the encryption speed/time of AES-CBC, AES-CTR and the stream cipher of your choice. Which is most efficient? Is the difference great?

> Return possible source code and answer the questions.

## Task 2: