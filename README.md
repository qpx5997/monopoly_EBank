# Monopoly EBank Manual
Written by qpx5997

### (UNFINISHED, USE THE `manual` COMMAND FOR A GUIDE TO HOW TO USE THE PROGRAM)

## Table of Contents

* [Part I: Introductory Chapters](#part-i-introductory-chapters)
  * [Chapter 1: Introduction](#chapter-1-introduction)
    * [About The Program](#about-the-program)
    * [Why This Program?](#why-this-program)
    * [Why This Manual?](#why-this-manual)
  * [Chapter 2: Downloading](#chapter-2-downloading)
* [Part II: Commands](#part-ii-commands)
  * [Chapter 3: Quick Reference](#chapter-3-quick-reference)
  * [Chapter 4: Money Management Commands](#chapter-4-money-management-commands)
    * [`reset`](#reset)
    * [`add`](#add)
    * [`subt`](#subt)
    * [`trans`](#trans)
    * [`go`](#go)
    * [`set`](#set)
    * [`itax`](#itax)
    * [`ltax`](#ltax)
    * [`vm`](#vm)
    * [`status`](#status)
    * [`mtransi`](#mtransi)
    * [`mtranso`](#mtranso)
  * [Chapter 5: Player Management Commands](#chapter-5-player-management-commands)
    * [`ren`](#ren)
    * [`addp`](#addp)
    * [`delp`](#delp)
  * [Chapter 6: Other Miscellaneous Commands](#chapter-6-other-miscellaneous-commands)
    * [`reset`](#reset)
    * [`help`](#help)
    * [`manual`](#manual)
    * [`changelog`](#changelog)
    * [`exit`](#exit)
  * [Chapter 7: Physical Management](#chapter-7-physical-management)
  * [Chapter 8: Version History](#chapter-8-version-history)

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

To download the program: (This assumes you're on Windows; for macOS, I'm not so sure but the steps should be similar)

1. Go to https://github.com/plz4x/monopoly_EBank.
2. Click the green "<> Code" button.
3. In the menu that appears, click "Download ZIP" at the bottom of the menu.
4. In your file explorer, right click on the ZIP file called `monopoly_EBank-main.zip` (it will most likely be in the "Downloads" folder) and click "Extract All".
5. If you see a window asking you where to put the extracted folder, just ignore it and click "Extract". 
6. The ZIP file will turn into a folder which will automatically open in another window. In it will be another folder called `monopoly_EBank-main`. Double-click the folder.
7. In the folder should be four files: `LICENSE.md`, `README.md` and `Monopoly-EBank.py`. Double-click `Monopoly-EBank.py`.
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

## Chapter 4: Money Management Commands

### `add`
**What it does:** Adds money to the specified player from the bank.

#### Example Usage
```
add p1 100
```
Adds M100 to p1.

### `subt`
**What it does:** Subtracts money to the specified player. That money goes to the bank.

#### Example Usage
```
subt p1 100
```
Subtracts M100 from p1.

### `trans`
**What it does:** Transfers money from one player to another.

#### Example Usage
```
trans p1 p2 100
```
Transfers M100 from p1 to p2.

### `go`
**What it does:** Adds M200 to the specified player. This is a shortcut to `add (PLAYER) 200`.

#### Example usage
```
go p1
```
Adds M200 to p1.

### `set`
**What it does:** Sets the specified player's money to the specified amount.

#### Example usage
```
set p1 1500
```
Sets p1's money to M1500.

### `itax`
**What it does:** Subtracts M200 from the specified player. This is a shortcut to `subt (PLAYER) 200`.

#### Example usage
```
itax p1
```
Subtracts M200 from p1.

### `ltax` or `stax`
**What it does:** Subtracts M100 from the specified player. This is a shortcut to `subt (PLAYER) 100`.

#### Example usage
```
ltax p1
```
```
stax p1
```
Both of these subtracts M100 from p1.

### `vm`
**What it does:** Shows the specified player's balance (amount of money they have).

#### Example usage
```
vm p1
```
Shows p1's balance.

```
vm ==all
```
Shows all players' balance.

### `status`
**What it does:** Shows the specified player's status. A status is a word to describe how much money they have (e.g. Impoverished, Affluent).

#### Example usage

```
status p1
```
Shows p1's status.

```
status ==all
```
Shows all players' statuses.

#### Ok but why does this even exist???

I thought it would be a funny addition. :)

### `mtransi`
**What it does:** Short for **m**ulti **trans**fer **i**ncoming. Transfers the specified amount from every player to the specified player.

#### Example usage

```
mtransi p1 10
```
Transfers M10 from every player to p1. If there are 3 people in the game (excluding p1), p1 will receive a total of M30.

### `mtranso`
**What it does:** Short for **m**ulti **trans**fer **o**utgoing. Transfers the specified amount from the specified player to every player.

#### Example usage

```
mtranso p1 50
```
Transfers M50 from p1 to every player. If there are 3 people in the game (excluding p1), p1 will transfer a total of M150.

## Chapter 5: Player Management Commands

### `ren`
**What it does:** Renames the specified player.

#### Example usage

```
ren p1 p5
```
Renames p1 to p5.

**NOTE 1:** Renaming a player to a name which has `==` in front of it (e.g. `ren p1 ==all`) will result in an error. Words with `==` in front of them are called **special keywords**, and they are reserved for special uses (e.g. `vm ==all`).
**NOTE 2:** Entering `ren p1 p5` and then `add p1 100` will result in an error as p1 has been renamed. Entering `add p5 100` instead will work.

### `addp`
**What it does:** Adds a player.

#### Example usage

```
addp p5 400
```
Adds player `p5` with M400.

```
addp p6
```
Adds player `p6` with M1500.

### `delp`
**What it does:** Deletes a player.

#### Example usage

```
delp p1
```

Deletes player `p1`.

## Chapter 6: Other Miscellaneous Commands

**The following commands all require only one argument. That is, for the reset command, just type `reset` and it will run.**

### `reset`
**What it does:** Displays a confirmation message. If confirmed, it resets all the players and money.

### `help`
**What it does:** Shows a quick overview of some commands.

### `manual`
**NOTE:** This command has been from v1.8 onwards. In versions of v1.7 and before, it shows a guide to the CLI, but from v1.8 onwards, it just displays a message to see the README for a guide.

### `changelog`
**What it does:** Shows the changelog.

### `exit`
**What it does:** Displays a confirmation message. If confirmed, it stops the program.

## Chapter 7: Physical Management

The following things still need to be managed physically on the board:
* properties;
* houses and hotels;
* board tokens;
* dice rolls;
* chance cards and community chest cards (though money effects can be managed in the CLI);
* jail and get out of jail free cards;
* mortgages;
* trading of items between players (though payments can be managed in the CLI)

## Chapter 8: Version history

v1.0 (26/10/2025): Initial release, can only handle money.

v1.1 (29/10/2025): Added player renaming and fixed a minor spelling error. Also did a bugfix.

v1.2 (31/10/2025): Did a bugfix.

v1.3 (07/11/2025): Added ltax and itax commands and did a bugfix.

v1.4 (17/02/2026): A minor edit where I changed the header to my new username. Forgot to update the version history command print in the program itself tho :\

v1.5 (17/02/2026): Changed tabs in the source code to spaces, fixed a bug, added a new chapter to the manual and added delp and addp commands.

v1.6 (22/02/2026): Did a bugfix involving unescaped quotes.

v1.7 (01/03/2026): Reserved special keywords and added the status command and comments.

v1.8 (05/04/2026): Did bugfixes and added mtransi and mtranso commands, confirmation messages and stax alternative command. <-- CURRENT VERSION

v2.0 (FUTURE): Add property management.