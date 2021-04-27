# Week 7 Exercises

This week’s exercises focus on Diffie-Hellman and elliptic curves.

You can find related information from the book in pages 163-199. 

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 |  Naive DH and MitM
Task 2 | 3 | DH with a very unsafe prime
Tasks 3.1 & 3.2 | 4 | ElGamal & malleability
Task 3.3| 5 | ElGamal & malleability

## Task 1: Naive DH and MitM ##

## Task 2: DH with a very unsafe prime ##

## Task 3: ElGamal & Malleability ##
The purpose of this task is to introduce the ElGamal cryptosystem and to show how malleability works in this.

You should familiarise yourself with the [ElGamal cryptosystem](https://en.wikipedia.org/wiki/ElGamal_encryption).

You are working in a multinational company and you have learned that the bookkeeping has been changing some key figures in reporting the revenues, taxes etc. to the authorities. In your position in the company you have been tasked with submitting the figures to the proper authorities. You would like to report the correct figures instead of the fake ones, but the numbers have been encrypted using ElGamal encryption. You have access to the public key parameters (parameters.txt) and the encrypted values (ciphertexts.txt). Each of the lines in the ciphertext file corresponds to the encryption of a single number in the reporting.

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
All values in the ciphertexts should be in the range from 1 to p (the ElGamal modulus given in the parameters.txt file.

> Return the new encrypted file together with any code that you have used to achieve it. Reference any external sources that you have used.

