# Bruteforcer

You are given a program `bruteforcer` which can be run using the following commands while in this directory
```bash
chmod +x bruteforcer #If the file is not marked as executable
./bruteforcer
```
The program prompts for an input when executed and will print out the flag on giving the correct password.

Also included is a `wordlist.txt` consisting of a list of around 5 million passwords; one of which is the above mentioned correct password. 
Your task is to write a script that automatically finds this correct password.
Checking each word sequentially in the provided wordlist, however, will take a lot of time due to the huge size of the wordlist.

This is where you can use the information on whether the password you provide is larger or smaller
([lexicographically](https://en.wikipedia.org/wiki/Lexicographic_order)) than the correct password. This information can be used to perform
a [binary search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search) over the wordlist and quickly find the answer.

Flag format: flag{...}

Solution to this is present in `script1.py`

# Notwordle

The description and aim of this challenge is similar to the `bruteforcer` challenge. <br>
Instead of giving the lexicographic order between the input and the actual password, 
the program in this challenge prints the number of characters you got right. 
You must leverage this information to figure out the correct password.

**Flag Format:** flag{...}

Solution to this is present in `script2.py`

# Tic-Tac-Toe

Run the game as :
```bash
chmod +x ttt #If the file is not marked as executable
./ttt
```
[ <b>NOTE</b> : The indices, i.e. rows and columns, are zero-indexed (the first element is referred by 0) ] <br>
<br>
You task is to create a program that always draws or wins against the given program. Repeating this 250 times will earn you the flag.

**Flag Format:** flag{...}
<br>
<br>
<br>
<br>
<details>
  <summary>Solution spoiler</summary>
  https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
</details>


Solution to this is present in `script3.py`
