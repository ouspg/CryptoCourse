# Week 5 Exercises

This week’s exercises focus on keyed hashes and authenticated encryption.

You can find related information from the book in pages 127-162. 

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Brute forcing a short authentication tag 
Task 2 | 3 | Timing attack
Task 3 | 4 | Short cycles in GHASH
Task 4 | 5 | Forging CBC-MAC messages

## Task 1: Brute forcing a short authentication tag

Choose a cryptographic library that supports the GCM and/or CCM modes of operation (with AES preferably). 

Choose the shortest possible tag length (1 or 2 bytes is enough, more than 4 may take a lot of time).

Compute an authenticated encryption of some message of your choosing. Then brute force another message that has the same authentication tag. 

Note that the messages do not need to make any sense i.e. the messages can be just arbitrary binary strings.

> Provide any source code, the key that you used and the two different messages with the same authentication value as your answer. You can showcase time used for brute forcing for example by using tables.


## Task 2: Timing attack

In this task we will implement a side-channel attack on MAC verification on target application. More precisely, implement a timing attack for the following scenario. 

***“Timing attacks on MAC verification” section of the course book (pages 140-142)  are very useful in this exercise.***

Mallory has managed to eavesdrop Bob and Alice. They have a joint project for investing on some company, in a big time. They know that the stock of this company is about to jump like a really big, soon. You are desperate to know which company, but they did not said it aloud.

You know that Bob is using message service for sending authenticated encrypted messages with Alice, but it is implemented bit poorly. It verifies if message tag is valid before forwarding messages for receiver, secondly, it might not implement best practices on verifying tags; it might be open for side-channel attacks. Thirdly, it has been reusing IV and key-pairs, leading for ciphertext forgery. Uh-oh.

Mallory has managed to forge following message, but he is missing authentication key for creating the valid tag. He does not know the total length of the tag as well. It changes daily. However, he knows that it is **hexstring with  length of even number**, e.g. `2e4c5b'.

```
Hey, what were the exact details of the company, just double-checking the address etc. Can you send email copy for bob2@bob2.com. It is not encrypted, so i delete it ASAP!

Best Regards,
Bob
```

See ciphertext in [files](files) folder.

Mallory thinks, that he could attempt timing attack for the server to forge valid tag.

Binary application is simulating server. See binary in [files/authenticator](files/authenticator). Run it on Linux (it requires glibc library) Check help for possible arguments.
```
./authenticator --help
```

**Disclaimer: you should never store encryption/tag keys in binary as in this case, someone always is able to extract them, even if the binary is obfuscated.**

Application accepts data in following JSON format:
```
{
    "sender": "Bob",
    "receiver": "Alice",
    "data": "<base64 encoded binary ciphertext>",
    "tag": "<hexstring>" 
}
```

The workflow of attack is something like this:

  1. Change the MAC value in the first byte of the MAC and time the execution of the verification
  2. Change the MAC value in the second byte and time the execution of the verification.
  3. Repeat the change in byte value and the timing for all bytes of the MAC tag.

Note, that there might be noise in the time.

**Can you figure out how Alice responded?**

> Answer the above questions and provide any source code you used in your work.

## Task 3: Short cycles in GHASH 
In this task you will see how the GHASH function in the GCM mode has a problem with some short cycles in the hash function.

>"For example, the value H = 10d04d25f93556e69f58ce2f8d035a4 belongs to a cycle of length five, as it satisfies H^5 = H, and therefore H^e = H for any e that is a multiple of five (the very definition of cycle with respect to fifth powers). Consequently, in the preceding expression of the final GHASH value Xn, swapping the blocks Cn (multiplied to H) and the block Cn – 4 (multiplied to H 5) will leave the authentication tag unchanged, which amounts to a forgery.” 

You can use [this paper](https://eprint.iacr.org/2011/202.pdf) as a starting point.

**3.1** Find a short cycle in the GHASH function. Give the value that belongs to a cycle and the length of the cycle.

**3.2** Demonstrate the possibility to generate a forgery by rearranging message blocks within a short cycle. That is show how the message can be changed and the hash value still remains the same.

>Provide any source code that you used and answer the questions

## Task 4: Forging CBC-MAC messages

CBC-MAC was one of the first block-cipher based implementations for calculating message authentication tag . As it later turned out, it was far away from secure method without further enchantments. Short CBC-MAC intro can be found from the course book on the page 134.

In this task we will take a look for the original CBC-MAC based message authentication. Your task is to demonstrate how you can somehow forge authenticated messages at least partially without knowing the original authentication key, while they still seems to come from valid sender. 

Demonstration should happen as following:

  * You have generator, e.g. client for HTTP server. Creates tags for messages, sends messages.
  * You have consumer, e.g. HTTP server. Receives messages.Validates tags for messages.

Select CBC-MAC implementation for tags. Initialization vector (IV) is used at first.

Client and server have some public protocol what you know, but some content is expected to change. 

For example making bank transaction:

```
from=alice;to=bob=amount=40;
```

We don't need to encrypt the content, we only generate MAC tags to validate authenticated senders. We can keep everything very simple on this demo.

You should act as man-in-the middle party; you can receive, modify and forward messages further, from generator to consumer. Initialization vector is always transmitted with message and is *therefore* freely modifiable. 

E.g. `message || IV || MAC`

**What limitations you have modifying the message in such a way, that tag is still valid? Let's expect that we are getting the first message, we need to modify that and have no other information. How encryption algorithm block size affects here? *Demonstrate some messages with the created environment.***

At this point, you have probably noticed the issue. Let's fix it.

Consider following situation: you are able to capture following messages:

`(a), (b) and (a||b)` with their related CBC-MACs.

**What kind of messages you are able to forge, if message length is not limited, based on these messages? Demonstrate few of them. They don't need to make sense in this case.**

Let's 'fix' this problem in a way, that receiver accepts only fixed length messages. Further, we now encrypt the data, but accidentally use *the same key* for CBC-MAC and CBC encryption.

**What blocks you are able to modify without receiver noticing and why?**

> Show your code and answer the questions.
