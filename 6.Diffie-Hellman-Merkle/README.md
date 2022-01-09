# Week 6: Diffie-Hellman-Merkle

This week’s exercises focus on Diffie-Hellman-Merkle (mostly known as Diffie-Hellman) key exchange and the ElGamal cryptosystem. **Many of the problems include some mathematical concepts that are not thoroughly presented in the course book or material. Please contact course staff if you need any help with these exercises.**

## Grading

rou are eligible for the following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 1 |  Naive DH and MitM
Task 2 | 2 | DH with a very unsafe prime
Tasks 3.1 & 3.2 | 3 | ElGamal & malleability
Task 3.3| 4 | ElGamal & malleability

## Task 1: Naive DH and MitM ##

Diffie-Hellman key exchange can be thought of as one of the foundations of modern public cryptography. Any number of different parties can jointly establish a shared private key in a possibly insecure channel, if the method is correctly implemented.

However, originally the method (the simplest of DH protocols) did not provide any sort of authentication in key establishment and it was vulnerable to a man-in-the-middle attack.

*Diffie-Hellman is handled in the course book on pages 201-216.* 

Let's consider a situation where we have a third, unwanted party Eve, who is able to eavesdrop on the discussion of Bob and Alice. If Eve is also able to capture the messages and modify them, then she is able to establish two distinct key exchanges, without Alice or Bob acknowledging anything in the initial phase of the discussion.

In practice, Eve is then able to decrypt all of the ongoing traffic while she is also required to proxy all of the messages to remain undetected.

**Task 1.1.** Implement MitM attack

Take a look at figure 11-2 and 11-3 in the course book on pages 209-210, which describes the anonymous protocol (Note that modulus is missing from this abstraction, should be used on implementation!). Implement a scenario programmatically, where Alice and Bob attempt to establish key exchange, but instead Eve captures the messages, and establishes two distinct exchanges. Showcase how Eve can act as middle proxy and decrypt the messages sent by Alice or Bob. 

**We have a base for coding in Python that you could continue for easier implementation, see [diffie_hellman.py](diffie_hellman.py).**

During the implementation, use *safe* DH parameters. For private keys of Bob and Alice, select a prime which is large enough.

You should select generator *g* (consider performance) as base and public modulus p as a safe prime when number p = 2q + 1, where q is also prime. 

Established key is used on symmetric encryption with AES-CBC on this case.

**Task 1.2.** Explain shortly how selection of *g* and modulo *p* can affect eavesdropping. 


**Task 1.3.** How have modern systems (e.g. TLS) further solved the MitM problem?

> Include source code and possible references. Answer the questions.

## Task 2: DH with a very unsafe prime ##

As you recall from the lectures, you should always use a safe prime (i.e. prime p, where (p-1)/2 is also a prime) with DH key exchange. Let's see what happens when you deal with a **very** unsafe prime. You can also check page 215 from the course book. Also page 176 can contain some helpful hints.

You are given a large [prime number](t2_files/unsafe_p.txt) and a [generator](t2_files/generator.txt) of the group Z_p. Unfortunately, the prime p is very unsafe (i.e. p-1 has a lot of small factors). This means that it is possible that you end up in a small subgroup with your shared secret with Alice.

Alice has sent you her [public share](t2_files/unsafe_ga.txt) of the DH protocol. 

**2.1** Find out what is the order of Alice's share, i.e, *the smallest integer d for which Alice's share of the dth power equals 1 modulo p.*

**2.2** How many possibilities there are for your common shared secret with the given Alice's share? Does this number depend on your choice of your secret exponent? Why or why not?

**2.3** Find out what are the different factors of p-1. (Yes, I know factoring is hard, but here you can go with some trial and error. So, divide the value p-1 with some small primes until the division is no longer even and work your way towards 1). Based on this factorisation, state what other small subgroups can you easily find in the given group. How do you produce generators for such subgroups from the original generator?

**2.4.** What is the bit length of p and what level of security (approximately) could you expect from a prime of that size?

> Answer the questions above and provide any code that you have used to solve the problems. Reference outside sources.

## Task 3: ElGamal & Malleability ##
The purpose of this task is to introduce the ElGamal cryptosystem and to show how malleability works in this scenario.

You should familiarise yourself with the [ElGamal cryptosystem](https://en.wikipedia.org/wiki/ElGamal_encryption).

You are working in a multinational company and you have learned that the bookkeeping has been changing some key figures in reporting the revenues, taxes etc. to the authorities. In your position in the company you have been tasked with submitting the figures to the proper authorities. You would like to report the correct figures instead of the fake ones, but the numbers have been encrypted using ElGamal encryption. You have access to the public key [parameters](t3_files/parameters.txt) and the [encrypted values](t3_files/ciphertexts.txt). Each of the lines in the ciphertext file corresponds to the encryption of a single number in the reporting.

**3.1** Describe briefly how the malleability property of ElGamal may help you in defeating the immoral reporting of your company.

**3.2** What measures should be used in order to prevent this type of malleability? List at least 2 different methods.

> Answer the above questions and give code/pseudocode on the algorithms that you could use for Task 3.1. .

**3.3** You know that the differences between the fake report and the original are the following:
* The number on the first line has been multiplied by 1/6
* The number on the third line has been halved
* The number on the fourth line has been multiplied by 4
* The number on the sixth line is the product of the first and fourth line
* The number on the seventh line is the product of the 2nd, 3rd and 5th lines.
* The number on the eighth line is the product of the fourth and the seventh line.

Generate a new encrypted file that decrypts the numbers to their original values instead of the fake ones, while conforming to the other rules in the report.
All values in the ciphertexts should be in the range from 1 to p (the ElGamal modulus given in the [parameters.txt](t3_files/parameters.txt) file). The ciphertexts should be formatted as `(x, y)`, where x & y are integers.

You can check the correct hash values for the whole file and for each line separately in [here](t3_files/hash_solutions.txt). Use SHA256 hash on a file that has UTF-8 encoded values, one on each line separated with `\n` for the whole ciphertext file and a file with a single line without `\n` for the single line checks.

> Return the new encrypted file together with any code that you have used to achieve it. Reference any external sources that you have used.

