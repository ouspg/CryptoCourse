
# Week 6 Exercises

This week’s exercises focus on hard problems and the RSA cryptosystem.

You can find related information from the book in pages 163-199. 

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | RSA encryption and signatures with OpenSSL 
Task 2 | 3 | Message and signature verification?
Task 3 | 4 | Textbook RSA signature forgery
Task 4 | 5 | Roll your own public key cryptosystem

## Task 1: RSA encryption and signatures with OpenSSL ##

In this task you need to encrypt and sign a message with RSA. The [OpenSSL Cookbook](https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html) may be helpful in this task. You can also find more concise presentations  on who to do this on the command line with the help of your favorite search engine. The command most useful here is `rsautl`.

**1.1** Generate an RSA key of suitable length OR use one that you have previously generated. Generate a message and encrypt it using the public key.
> Provide the key and the message as your answer. Also show the commands that you used to encrypt the message.

**1.2** Use RSA to sign the message. 
> Provide the public key, the message and the signature as your answer. Also show the commands you used to generate the singature.

## Task 2: Message and signature verification? ##
In this task you need to find correct messages and signatures. You are given file `messages.txt` and folder `signatures` that contain the messages and signatures under some private keys corresponding to public keys in the folder `public_keys`.

**2.1** Match all messages with correct signatures and public keys.

>Provide the matching pairs and any code that you used as your answer.

|Message row|Public key|Signature file(s)|
--- | --- | --- 
|1   |example.pem|example.sign|
|2   |           |            |
|3   |           |            |
|4   |           |            |
|5   |           |            |
|6   |           |            |
|7   |           |            |
|8   |           |            |
|9   |           |            |
|10  |           |            |
|11  |           |            |
|12  |           |            |
|13  |           |            |
|14  |           |            |
|15  |           |            |
|16  |           |            |
|17  |           |            |
|18  |           |            |
|19  |           |            |
|20  |           |            |

**2.2** What potential vulnerabilities there are if only textbook version of RSA is used to sign messages?

>Answer the question in short textual form.

## Task 3: Textbook RSA signature forgery

Mallory wants the highest grade from the Cryptology University course. To get that he needs signed positive confirmation from his professor - Alice. Unfortunately Alice knows that he has not been very hardworking student (Mallory has been just spending all days thinking about incoming May Day instead of studying) and obviously she is not going to sing with her private key any message with positive implications. However, Mallory realizes that Alice may sign other types of confirmations, negative or neutral ones (and even the gibberish ones!).

**Read pages 188-189 from course book.** You might want to find out more from external sources also, it is quite simplified on the book.

**Task 1.1.** Forging the valid signature

Use  binary (from [files](files) folder) of this task to make Alice "sign" some neutral, negative or other kind of message (does not matter if it is little "gibberish" text, Alice will happily sign quite lot of things, until certain limit: the message content must have `_n` prefix (ASCII encoded) to describe neutral/negative clause of the message.

RSA key length is 4096 bits in this case. You can find the public key in [files](files) folder as well.

You have now some message that has been successfully signed by Alice. Now, forge message that has some kind of positive implication of its content (so it could be interpreted as "positive confirmation from professor"). In practice, message should have at least `_p` prefix to describe positive alignment! Message can contain something more as well; it does not necessary change the difficulty of the task.

 Forge valid signature for that message (obviously you cannot ask that from the binary, because Alice would not never sign that kind of message). *This is pure textbook RSA case - no hashing or padding used.*

In the end, you can easily check with public key that your answer is correct.

**Task 1.2.** We required only two bytes of real information. What if we need to provide a valid understandable message in whole for Alice for signing at first? How this and the length of the message affects the difficulty of process?

> Describe shortly the process and include any code, forged message and signature in your answer. Remember to reference any external sourced used on your solution!

## Task 4: Roll your own public key cryptosystem ##
In most of the courses on cryptography that you will attend, the instrcutor will tell you that you should not roll your own cryptographic systems. There are of course good reasons for this warning.

But now that we are on a course that will give you some hands on experience on cryptography, maybe a little exercise in building your own cryptosystems might be in order.

In this task you need to describe a public key cryptosystem based on a hard problem of your own choice. **The system that you describe does not need to be secure or to contain a security proof**. Of course, if you can do that, it might get you some extra credit + a publication in a conference :)

**4.1** Describe your public key cryptography algorithm by answering the following questions in a few sentences.
 * What problem is the hard problem that your system is based on?
 * What evidence is there that the problem is hard?
 * How does one use the problem to encrypt/sign (choose one) messages?

**4.2** Write a short code/pseudocode of your implementation. Can you estimate or evaluate how complex the process of encrypting or signing a message will be?

**4.3** Assume the role of an attacker. Write a short analysis on the possible attacks on your scheme. You should at least consider attacks that have been discussed in the course material (side channels, man-in-the-middle, etc.)

**4.4** Do a quick search on [Google Scholar](https://scholar.google.com/) with suitable keywords (e.g. "the name of your problem" + "cryptography/encryption/signature"). Write a short summary of your findings. Has the problem been used for cryptography before? Have any of the proposed schemes been broken?
 >Answer the questions above and provide all references to outside sources in your reporting.
