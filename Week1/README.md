  # Challenge 1 (Zip Mania) Bash

This challenge is supposed to get you started with bash scripting </br>

* We will use `7zip` and `zip` for this challenge.
* Every time you extract the zip file, you get a new zip file and an ASCII text file containing the password(not encoded) to extract the new zip file.
* To unlock the 7zip/zip files, encode the password to base64, base32, hex, or maybe the text itself. (any one of them would be the correct encoding)
* You have to do this unzipping many times (Ummm... maybe I chose 690 but not sure xD) until you get the flag; hence you need to write a bash script for it

Flag format: flag{...}


# Challenge 2 (Web Mania) Linux

Proceed [here](https://www.cse.iitb.ac.in/~akshatka/) to get started with the challenge.</br>
Each webpage links you to other and so on. You need to write a script to automate this.</br>
At the end you get a [tar](https://www.geeksforgeeks.org/tar-command-linux-examples/) ball. It contains the further instruction.</br>
Some commands that you might need are `wget` `grep` `find` `tar` 

Flag Format: flag{...}

Solution to this challenge is present in `script2.sh`

  # Challenge 3 (env Pollution) Linux
We have provided you 3 [ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) files(compiled C codes)

In each level you need to perform some tasks to get the flag
- level1: get the [environment variables](https://www.geeksforgeeks.org/environment-variables-in-linux-unix/) in the spawned shell
- level2: launch the program with no environment variables
- level3: launch the program with an environment variable `CSeC=Awesome`; ensure that the [`argv[0]`](https://stackoverflow.com/a/3024202) is equal to `YoS`

PS: You may skip level3, since you will get to know more about it in the upcoming weeks.

Flag format: flag{...}
