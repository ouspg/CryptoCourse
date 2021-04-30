# Week 8 Exercises

This week’s exercises focus on TLS.

## Grading

You are eligible for following points from the exercise. Previous task(s) should be completed before going further.

Task #|Grade|Description|
-----|:---:|-----------|
Task 1 | 2 | Getting to know TLS versions
Task 2 | 3 | Getting to know the vulnerabilities of SSL/TLS
Task 3 | 4 | Testing TLS connections with OpenSSL
Task 4 | 5 | Downgrading attack

## Task 1: Getting to know TLS versions ##

In this task you will familiarise yourself with the TLS versions 1.1, 1.2. and 1.3.

**1.1** Find the RFC documents related to different TLS versions [1.1](https://tools.ietf.org/html/rfc4346), [1.2](https://tools.ietf.org/html/rfc5246), [1.3](https://tools.ietf.org/html/rfc8446). Read at least the parts that specify major differences to the previous version and the Mandatory cipher suites parts.

**1.2** List the major differences in the three different versions. Use a table with the different versions as columns and then label rows as you best see fit to demonstrate the differences.

> Answer the questions above. Reference any outside sources that you have used.

## Task 2: Getting to know the vulnerabilities of SSL/TLS ##

Go to the Common Vulenrabilities and Exposures (CVE) [website](https://cve.mitre.org/). Search for vulnerabilities in the TLS protocol and different versions (1.1, 1.2, 1.3).

**2.1** Which version has the most listed vulnerabilities in the CVE database?

**2.2** What is the most severe vulnerability listed for each version of TLS?

**2.3** What is the most recent vulnerability listed for each version of TLS?

> Answer the questions above. Reference any outside sources that you have used.

## Task 3: Testing TLS connections with OpenSSL ##

In this task you are to test a website of your choosing with the help of OpenSSL. The OpenSSL Cookbook section 2: [Testing TLS with OpenSSL](https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html) will be **very helpful** in this task.

**3.1** Choose a website that supports HTTPS/TLS. What versions of TLS are supported? What ciphersuites are supported? Are there any preferences set by the website?

**3.2** Test how low you can go with TLS connections (you can try even SSL, if you feel like it). What is the lowest version of TLS (or SSL) that is supported by the website?

**3.3** Go back to Task 2 and the different vulnerabilities listed for TLS. Does it seem that the website you are testing could be vulnerable to some of the known CVEs?

> Answer the questions and provide any code/scripts that you used in testing the systems. You can provide snippets of the TLS tests that you run with OpenSSL.


## Task 4: Downgrading attack ##

In this task you are to implement a downgrading attack on a TLS server.
