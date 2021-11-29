# Quantum computing 

This week’s exercises focus on quantum computing, post-quantum cryptography and feedback on the course.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 1 | Feedback on the course
Task 2 | 2| Quantum circuits and algorithms
Task 3.1 & 3.2 | 3 | Post-quantum Cryptography
Task 3.3 | 4 | Post-quantum Cryptography
Task 3 alt. | 3-4 | Security level analysis of your favorite application

## Task 1: Feedback on the course ##
Now in the final week we'd like to get your feedback on the course. Please answer the questions below. **Note that you can give also anonymous feedback through the University official [feedback pages](http://palaute.oulu.fi/).**

* What did you like about the lectures?
* What would you improve on the lectures?
* What did you like about the exercises?
* How would you improve the exercises?
* Did you miss some type of an exercise or some content as an exercise?
* What was missing from the course (i.e. what more would you have wanted from the course)?
* What was the worst part of the course in your opinion?
* Freeform feedback on the course

> Answer the questions above.

## Task 2: Quantum circuits and algorithms ##
In this task you wil try out some quantum computing yourself. Go to [the IBM quantum computer simulator](https://quantum-computing.ibm.com/composer/files/new). 

**2.1** Try out some quantum circuits (just fool around, attach a screenshot of your most artistic one. Make sure that the different probabilities are shown in the picture.) Explain shortly what the circuit does (to the best of your understanding). 

**2.2** Go to the “Composer docs & tutorials” (left hand panel, lowest option) and find the model for Grover’s algorithm. Modify the given circuit in such a way that the circuit will find the other alternatives (the example finds 00, you should find 10, 01 and 11). Explain how you modified the circuit.

> Answer the questions above. Reference any outside sources that you have used.

## Task 3: 

In this week, you have two options for the final assignment. They are equal for acquiring the maximum grade.

### Post-quantum Cryptography (Option 1)
In this task you will learn more about post-quantum cryptography. 
Go to the [NIST PQC website](https://csrc.nist.gov/projects/post-quantum-cryptography) and look at the finalists of the PQC standardisation (Round 3 finalist candidates, not alternate candidates). 

**3.1** Answer the following questions:
* What hard problems are the candidates based on?
* What security levels are the candidates aiming for? (NIST has specified [five](https://csrc.nist.gov/CSRC/media/Projects/Post-Quantum-Cryptography/documents/call-for-proposals-final-dec-2016.pdf) pages 16-17)
* What parameters sizes do the candidates have? Key size, signature size, key generation time, signature generation time, verification time etc?

**3.2** Look for any implementations of the finalists e.g. via Google. What systems/libraries/applications support these? Can you find a rationale for the decision to support a specific method?

**3.3** Pick a finalist candidate. Do a search on [Google Scholar](scholar.google.com) with the candidate name and some additional suitable search terms (e.g. 'post-quantum cryptography'). How many results can you find? Are there any attacks on or weaknessess in the proposed scheme? If there are, explain these very briefly.

> Answer the questions above. Reference any outseide sources. For task 3.3 please list your query terms.  

### Security level analysis of your favorite application (Option 2)

Pick an application (such as a secure messaging application, VPN system etc.) and identify its crypto schemes, key length, and respective security levels. Your analysis can be based on marketing material, blog posts, websites, research papers or code analysis (if the application has open source code).

Report your findings (with references to sources) in a brief (2-3 A4 pages) document. Use figures and/or tables, if necessary.

An example structure for this type of document could be

1. Introduction
    * The name and type of application (HW/SW, VPN/messaging/firewall/home appliance…)
    * The reason you picked this application
    * The intended use of the application

2. Cryptography
    * What (data) is protected?
    * What algorithms are used?
    * What key lengths?
    * What arguments (if any) are given in support of using the above algorithms and key lengths?
3. Analysis
    * What is the level of security provided in the system based on your analysis?
    * Are there any gaps and/or discrepancies between different cryptographic primitives?
    * (optional) How could the security of the cryptography be improved?
4. References
    * Give a list of all the reference material that you have used. Please reference these also in the text so that we can see, where each bit of information has been collected.

> You can also make a separate PDF document, and upload it into your repository, if you want. Remember to reference for it.
