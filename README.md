# CryptoCourse
Exercises for the course Cryptographic systems and their weaknessess 521149S

You can find the course from the [Moodle.]()

## Exercise requirements

Theory of the exercises are mainly based on the book [Serious Cryptography](https://nostarch.com/seriouscrypto). It is available in the library of the University of Oulu in [digital format](https://oula.finna.fi/Record/oy_electronic_oy.9917612964306252).

We will be also using the OpenSSL Cookbook which is available free on [here.](https://www.feistyduck.com/books/openssl-cookbook/)

Programming and command-line usage skills are expected.

Some of the exercises are requiring access for Linux environment. macOS might be suitable as well, but not fully tested.

Required software:

  * Python 3
    * [pycryptodome](https://github.com/Legrandin/pycryptodome) library for cryptographic operations 
  * `openssl` version 1.1.1f (31 Mar 2020). Examples from the OpenSSL Cookbook are based on this version, lower versions might be different and not bringing expected results.
  * [dieharder](https://webhome.phy.duke.edu/~rgb/General/dieharder.php) tool for random number generator (rng) testing
  * Code editor of your choice, `VSCodium` and `vim` are pre-installed.
  * Different programming languages, depending on your choice


### Provided virtual machine

Download urls for pre-configured virtual machine with Ubuntu 20 LTS can be found from the Moodle page.

There are two different versions; for VMware and Virtualbox. Download suitable for your needs. If you don't know which one, use VMware one which might bring better performance.

You can download VMware player from [here.](https://my.vmware.com/en/web/vmware/downloads/info/slug/desktop_end_user_computing/vmware_workstation_player/16_0)

Following credentials are used for virtual machine:
  * Username: `crypto`
  * Password: `crypto`

In case you have problems on getting it working, contact course assistants.

## Returning assignments 

The work will be done on the GitHub repository during the course.

You need to create private GitHub repository **from the url in Moodle page.**

Repository will be place for your work, and commit changes on there for corresponding folders.

Every week you need to return only URL for your repository, unless otherwise stated.

Check [cheat sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf) if you need a refresher on how to use Git. Some basic commands below

```
git add </path/filename>
git commit -m "<message>"
git push
```