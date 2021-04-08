# Week 5 Exercises

This week’s exercises focus on keyed hashes and authenticated encryption.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Brute forcing a short authentication tag 
Task 2 | 3 | Timing attack
Task 3 | 4 | 
Task 4 | 5 | 

## Task 1: Brute forcing a short authentication tag

Choose a cryptographic library that supports the GCM and/or CCM modes of operation (with AES preferably). 

Choose the shortest possible tag length (1 or 2 bytes is enough, more than 4 may take a lot of time).

Compute an authenticated encryption of some message of your choosing. Then brute force another message that has the same authentication tag. 

Note that the messages do not need to make any sense i.e. the messages can be just arbitrary binary strings.

> Provide any source code, the key that you used and the two different messages with the same authentication value as your answer. 


## Task 2: Timing attack
In this task you will check for a potential timing attack in a cryptographic library of your choice.

***“Timing attacks on MAC verification” section of the course book (pages 140-142)  are very useful in this exercise.***
Pick a cryptographic programming library and a MAC implementation of your choice (CMAC, HMAC, whatever). Compute a MAC of a message for that MAC and a key of your choice.
Implement a timing attack on the MAC verification.

1. Change the MAC value in the first byte of the MAC and time the execution of the verification
2. Change the MAC value in the second byte and time the execution of the verification.
3. Repeat the change in byte value and the timing for all bytes of the MAC tag.

**2.1** Can you spot meaningful timing differences? You can run the above steps several times for each byte to get more statistical results. 

**2.2** If there are timing differences in some MAC verification implementation, how would you implement a MAC tag guessing attack to forge a tag on a message of your choice? 
> Answer the above questions and provide any source code you used in your work.


## Task 3:

## Task 4: 
