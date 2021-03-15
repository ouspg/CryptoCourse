# Week 1 Exercises

This week’s exercises focus on classical ciphers and randomness.

Theory of the exercises are based mainly on the book [Serious Cryptography](https://nostarch.com/seriouscrypto). It is available in the library of the University of Oulu in [digital format](https://oula.finna.fi/Record/oy_electronic_oy.9917612964306252).

*Pages 1-38* are relevant for this exercise and might be good to read beforehand.

## Environment

You should have access into Linux/Unix environment to be able to complete Task 3.

The course virtual machine is suitable.

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

You are given the following encryption of an ASCII encoded message "Hi Kimmo". Each row in the table represents one character in binary and hexadecimal format. This task expects that the original form of the one-time pad has been used with bitwise exclusive OR.

Binary | Hex
--|--
0b01101001 | 0x69
0b00010101 | 0x15
0b01011111 | 0x5f
0b01001110 | 0x4e
0b00100000 | 0x20
0b00011100 | 0x1c
0b10101101 | 0xad
0b01100001 | 0x61


**Task 1.1** Produce a ciphertext that will decode into "No Rauli" under the same secret one-time pad as the original ciphertext was produced.

**Task 1.2** Produce a ciphertext that will decode into a 8 character ASCII string of your choice. Can you produce longer ciphertexts than 8 characters? Why/why not?

**Task 1.3** What is the secret one-time pad in binary format (8 x 8 bit)? How malleability applies on a one-time pad?

> You should return possible source code for how you solved the secret and produced the new ciphertexts. Answer the questions and **also** explain shortly the idea of your method.

Obviously we are not going to give you correct key to check your answer, but here is bit more cryptographic way. This might be applied on the future as well. You can verify that your key is correct, by combining single hexadecimal string from binary values, and calculating sha256 hash for the final string with `openssl` on Linux, for example if we combine given encrypted message:

```shell
 echo -n "0x69155f4e201cad61" | openssl dgst -sha256
```

Note `0x` prefix in the string and lowercase format. `-n` flag prevents appending new line in the end. Possible leading zeros in hex values are included. UTF-8 encoding has been used. Everything matters!

Correct hash for the key is `0de7672884e0d76c02387ef14360770ec923fd34f87d3303d082ec2da7a8741e`

## Task 2: Vigenere cipher

The following text is an English text that has been encrypted by using an unknown key with a Vigenere cipher. All punctuation and whitespaces have been removed from the text before encryption.

```
TRLSHAXRNSVKIENUFMEGRVDANEELHOFNSLUGIEFZVATAAGCIYAGIFADWUDHFYIFPOWVSPUMBKOTUOBYYNQWZYEEHBFCYCRZUKIPDZFFOYDBPZTPRBRVRFRBFYESLSXUAALBFIIAVWORLYBAAIAYGWYVNFLCZKHRVBANDRQFQMEYDHUFNFPCFZVNWSMIENVGQJSZHBFFFGKSBFLVWWORLNQRYFRNODAJIGLCZZNTRTOIYCWCSIACKMFYELOSMUOAHHARSXLTALRVQONZLVWMFFESISOKIIHZKRDQUSEJMNVGELRIHWXCAAFSOFNFWWFLTRVORRIYXFQFFBXFRZEYGWNVLVHJQKHNWWFUORVWORLYICDRCBPAGEIGBKUUERITAITGRRQMEYRDYFRRHTRVCGLJQDENQGFFRRVWEKMNVGELRIHWXCAAFSUGLRDRRFRNUSUEVRQHUFNBICGIDVVQUGLVQODPCHOHGIEGROFKEAGBAKOAOMFFPHCNXVSNQRYRTUEIFRLFRHAKHRVCOZEGDZUDPYLQMKIBQGAWOHUKAIK
```

**Task 2.1** Decrypt the text. What is the secret key? How many permutations were used? The course book can be very helpful.

**Task 2.2** Where is the text from? Who wrote it? If you find the source, read the whole text/article/newsitem/book...


> Show your work (code and reasoning; how did you decrypt this?) and answer the questions. You should not use existing tools which can solve this quite quickly. However, if you did, mention these tools, the commands you used **and** make a step-by-step report **why Vigenere cipher was decryptable**. 

## Task 3: Generating randomness

<p align="right">
<img src="img/random.png" alt="Random number. Source: XKCD="100px" align="right"/>
</p>

Randomness has a critical role in most of the cases to achieve *semantic security.* However, there is a difference between randomness and predictability as seen from the XKCD picture on the right; both should be noted.

There are many available tools and methods to generate randomness, but are they truly cryptographically unpredictable?

Some available software methods which **might or might not be** cryptographically unpredictable:

  * Python's programming language `random` library
  * C language's `rand` and `drand48`
  * `Math.random()` in JavaScript
  * `java.util.Random` in Java
  * Devices `/dev/urandom` and `/dev/random` on *nix systems
  * Bash function `$RANDOM`
  * [BCryptGenRandom](https://docs.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) on Windows. (legacy CryptGenRandom is **deprecated.**)
  * System.Security.Cryptography.RandomNumberGenerator on [C# .NET](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.randomnumbergenerator?view=net-5.0) on Windows
  * [Get-Random](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-random?view=powershell-7.1) on PowerShell
  * `openssl rand` method

**Task 3.1** What is the difference between `/dev/urandom` and `/dev/random` devices? Note also the [recent change on Kernel.](https://lore.kernel.org/lkml/20200131204924.GA455123@mit.edu/)

**Task 3.2** Generate randomness into different files using different methods that you have access to or manually (dice, smashing keyboard maybe?) You are not limited to a given list. **Use at least four** different methods. For non-manual methods, generate at least 1 megabyte of randomness.

**Task 3.3** Analyse those files with [dieharder](https://linux.die.net/man/1/dieharder). Report your findings. What is the meaning of p-value and null hypothesis in this context? Can you describe why tests are passed/not passed? Which methods seem to provide randomness with high entropy? If you have been using generic software libraries, results might not be good and can be very similar. What could be the reason?

For Debian based Linux, you can install it as :
```shell
apt-get update && apt-get install dieharder
```

**Task 3.4** Which methods from the given list are considered as cryptographically unpredictable? Why?

*It should be noted that it is possible to design a cryptographically
weak PRNG that will fool any statistical test e.g. dieharder, therefore it cannot be fully trusted as measurement of security.*

> Include all commands and possible source code(s) in your report. Answer the questions and clarify your findings.
