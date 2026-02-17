# Monopoly EBank Manual
Written by qpx5997

### (UNFINISHED, USE THE `manual` COMMAND FOR A GUIDE TO HOW TO USE THE PROGRAM)

## Table of Contents

* [Part I: Introductory Chapters](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#part-i-introductory-chapters)
  * [Chapter 1: Introduction](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#chapter-1-introduction)
    * [About The Program](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#about-the-program)
    * [Why This Program?](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#why-this-program)
    * [Why This Manual?](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#why-this-manual)
  * [Chapter 2: Downloading](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#chapter-2-downloading)
* [Part II: Commands](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#part-ii-commands)
  * [Chapter 3: Quick Reference](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#chapter-3-quick-reference)
  * [Chapter 4: Commands for Managing Money](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#chapter-4-commands-for-managing-money)
    * [`reset`](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#reset)
    * [`add`](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#add)
  * [Chapter 5: Version History](https://github.com/qpx5997/monopoly_EBank/tree/main?tab=readme-ov-file#chapter-5-version-history))

# Part I: Introductory Chapters

## Chapter 1: Introduction
### About The Program
The Monopoly EBank is a command line interface that closely resembles the Monopoly Bank. The difference between the physical Bank and this program is that the EBank is entirely cashless and also has an infinite amount of money.

### Why This Program?
Whenever I play Monopoly, I have to turn off the fans and close the windows in the room so as to avoid the money flying around, making it sweltering hot inside. As for the air conditioner, I usually don't turn it on becuase it kind of was unnecessary i guess :/

It's also such a pain to count the money manually and give change and you know, stuff like that.

So I've created this program as a solution to these problems. Sure, other people obviously **have** created these sorts of programs before, but well I love programming and I want to try to make one myself.

And err idk, i hope you enjoy ig.

### Why This Manual?
And by that I mean, why put the manual *here* instead of *in* the program itself?

Because readability.

There used to be a `manual` command in the CLI showing how to use the program, and a `help` command giving you a quick reference to the commands. However, they were a bit hard to read.

The manual looked something like this:

```
--snip--
1. COMMANDS FOR MANAGING MONEY
reset: Resets all player money to M1500.
add: Adds money to the stated player from the bank.
EXAMPLE: add p1 50 -- Gives M50 to p1
subt: Subtracts money to the stated plater. That money goes to the bank.
EXAMPLE: subt p1 50 -- Subtracts M50 from p1
go: Gives M200 to the stated player. Used as a shortcut from "add p1 200".
EXAMPLE: go p1 -- Gives M200 to p1
set: Sets the stated player's money to the stated amount.
EXAMPLE: set p1 300 -- Sets p1's amount to M300.
Press enter to continue or type "quit" to return to the CLI.
--snip--
```

It *is* rather readable, but I felt that it would be better to put the manual in a `.md` file, as these types of files present their text like a Wikipedia article.

So, yeah, here is the manual, existing today.

## Chapter 2: Downloading

You may skip this chapter if you have already downloaded the program.

To download the program: (This assumes you're on Windows, for macOS, I'm not so sure but the steps should be similar)

1. Go to https://github.com/plz4x/monopoly_EBank.
2. Click the green "<> Code" button.
3. In the menu that appears, click "Download ZIP" at the bottom of the menu.
4. In your file explorer, right click on the ZIP file called `monopoly_EBank-main.zip` (it will most likely be in the "Downloads" folder) and click "Extract All".
5. If you see a window asking you where to put the extracted folder, just ignore it and click "Extract". 
6. The ZIP file will turn into a folder which will automatically open in another window. In it will be another folder called `monopoly_EBank-main`. Double-click the folder.
7. In the folder should be five files: `LICENSE.md`, `README.md`, `manual.md`, `Monopoly-EBank.py` and `pdata.json`. Double-click `Monopoly-EBank.py`.
8. Right click it and select "Open with..." and select any terminal program, like PowerShell or something. If you see this in the terminal:
```
Monopoly E-Bank v1.0, a Python program by qpx5997
Type "help" to get a quick command reference, or "manual" for how to use this program.
>>>
```
then you are good to go! You can start using the program.

**Note:** When you start the program, it will start with the default players: p1, p2, p3 and p4, all with M1500. You can change the player names with the `ren` command. More on that later.

# Part II: Commands

## Chapter 3: Quick Reference

If you already know the commands, and you only need a quick reference, refer to this chapter.

*Insert quick reference here*

## Chapter 4: Commands for Managing Money

### `reset`
**What it does:** Resets all the players and money.

#### Example usage
```
reset
```
Resets all the players and money. (Obviously. It's literally stated above.)

### `add`
**What it does:** Adds money to the stated player from the bank.

#### Example Usage
```
add p1 100
```
Adds M100 to p1.

## Chapter 5: Version history

v1.0 (26/10/2025): Initial release, can only handle money.

v1.1 (29/10/2025): Added player renaming and fixed a minor spelling error. Also did a bugfix.

v1.2 (31/10/2025): Did a bugfix.

v1.3 (07/11/2025): Added ltax and itax commands and did a bugfix.

v1.4 (17/02/2026): A minor edit where I changed the header to my new username. Forgot to update the version history command print in the program itself tho :\

v1.5 (17/02/2026): Changed tabs in the source code to spaces, fixed a bug, added a new chapter to the manual and added delp and addp commands. <-- CURRENT VERSION

v2.0 (FUTURE): Add property management.
