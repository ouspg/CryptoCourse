# Cryptographic systems and their weaknesses 521149S

Exercises for the course Cryptographic systems and their weaknesses 521149S

## Contents

Course will go through basic concepts of cryptography, definitions and concepts of cryptographic security and testing these through programming. Showing different cryptographic weaknesses and demonstrating different implementations of these through programming. Basics of quantum computing and post-quantum cryptography.

You can find the course from [Moodle.](https://moodle.oulu.fi/) (FIXME!)

## Exercise requirements

Theory of the exercises are mainly based on the book [Serious Cryptography](https://nostarch.com/seriouscrypto). It is available in the library of the University of Oulu in [digital format](https://oula.finna.fi/Record/oy_electronic_oy.9917612964306252).

We will be also using the OpenSSL Cookbook which is available free on [here.](https://www.feistyduck.com/books/openssl-cookbook/) You can use the HTML version without registration.

Programming and command-line usage skills are required.

Some of the exercises require access to the Linux environment. macOS might be suitable as well, but not fully tested.

Required software:

  * Python 3
    * [PyCryptodome](https://github.com/Legrandin/pycryptodome) library for cryptographic operations 
  * `openssl` version 1.1.1f (31 Mar 2020). Examples from the OpenSSL Cookbook are based on this version; lower versions might be different and not bringing expected results.
  * [dieharder](https://webhome.phy.duke.edu/~rgb/General/dieharder.php) tool for random number generator (rng) testing
  * Code editor of your choice, `VSCodium` and `vim` are pre-installed.
  * Git for assignment management. Web GUI usage is also allowed.
  * Different programming languages, depending on your choice

Some additional software requirements might appear during the course.

### Provided virtual machine

Download urls for pre-configured virtual machines with Ubuntu 20 LTS can be found from the Moodle page.

There are two different versions; for VMware and Virtualbox. Download suitable for your needs. If you don't know which one, use VMware one which might bring better performance.

You can download VMware Player from [here.](https://my.vmware.com/en/web/vmware/downloads/info/slug/desktop_end_user_computing/vmware_workstation_player/16_0)

Following credentials are used for the virtual machine:

  * Username: `crypto`
  * Password: `crypto`

In case you have problems on getting it working, contact course assistants.

## Returning assignments 

The work will be done on the GitHub repository during the course.

You need to create a private GitHub repository **from the url in the Moodle page.** This will require a GitHub account.

Repository will be the place for your work, and you should commit changes on there for the corresponding folders.

*If you lost your repository, you can find it under organization [CryptoCourse-2022](https://github.com/CryptoCourse-2022) (FIXME!) once logged in.*

Every week you need to return only the URL of your repository for the assignment return box, unless otherwise stated. Remember that there are also mandatory questionnaires.

 **Deadline is always before the next supported exercise session!**

Check the [cheat sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf) if you need a refresher on how to use Git. Some basic commands can be found below.

```
git add </path/filename>
git commit -m "<message>"
git push
```
