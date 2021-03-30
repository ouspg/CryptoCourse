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

## Task 4: MACs gone wrong

> This task might be extremely challenging, depending on your technical background. However, we try to focus on the cryptographic part here, while still bringing the example of whole partial system.

### Preface

Bob has been busy. He has been working on his side project; a web app where he is testing "new" method for maintaining user authentication with HTTP cookies on the website. He is using `sha256` hashes as message authentication codes ([MAC](https://en.wikipedia.org/wiki/Message_authentication_code)s) of the cookie content with included random prefix key, as secure method to be sure, that only his backend server can be the origin of them. 
Once he is satisfied on his work from the login part, he asks his friend, Alice who is much more experienced on this matter, to check on his work. He is going to open-source his work.

You can find the source code from the [app](app) directory.

Alice quickly notices that there are few implementation problems on the code. One is, that *security assumption of `sha256` hashes as secure signature on authentication on this case is wrong,* even thought it is one of the most used hashing algorithms. Hash algorithms in *Merkle–Damgård* family are vulnerable on [length extension attack.](https://en.wikipedia.org/wiki/Length_extension_attack) One could add more data on top of existing data, and calculate new valid signature, as long as the content length of the existing data is known, regardless if old data is unknown. The implementation fails here, when random prefix data is simply included with the actual data. However, it could be secure, when implemented correctly. See reference for [HMAC](https://docs.python-requests.org/en/master/user/advanced/#session-objects).

Pages 124-133 from the course book are related on this matter.

### The actual task

At first, badly selected hashing algorithm did not sound **that** bad, there is another flaw on the source code (see `security.py`) on `parse_session` method: it might not be perfect on parsing the cookie, and with combination of bad hashing algorithm for this case, it can lead for unexpected things. 

**The task here** is to implement length extension attack on the web application. 

Can you access route `/admin/top-secret` just by modifying the cookie of the guest user?

In this case, we have access for hashed password (or secret) of the admin user, which still should be normally unusable for authentication, but now it is, because of the selected hashing algorithm (and overall implementation).

> You should return source code and shortly explain main mechanic on here; what you did. You can use existing tools for calculating new signatures.


**Disclaimer:** don't use app as example for many cases. For password hashing, proper algorithm such as [Argon2](https://en.wikipedia.org/wiki/Argon2) with salting should be used, which resists brute forcing.

### Some general tips for the task

To set application running on your local machine, there is available `Docker` image:

Docker has been installed on the provided virtual machine.

If you are working on Python code, see [`requests`](https://docs.python-requests.org/en/master/) library for handling HTTP requests. [Session objects](https://docs.python-requests.org/en/master/user/advanced/#session-objects) could be useful on handling and accessing cookies.