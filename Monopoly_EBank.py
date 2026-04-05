print("""Monopoly E-Bank v1.8, a Python program by qpx5997
Type "help" to get a quick command reference, or "manual" for how to use this program.""")

money = {
    "p1": 1500,
    "p2": 1500,
    "p3": 1500,
    "p4": 1500
}

while True:
    cmd = input(">>> ")
    cmd_split = cmd.split(" ") # Splits the command into multiple list items
    if cmd_split[0] == "reset":
        while True:
            option = input("Are you sure you want to reset? [y/n] ")
            if option.lower() == "y":
                # reset money (to 1500), properties
                money = {
                "p1": 1500,
                "p2": 1500,
                "p3": 1500,
                "p4": 1500
                }
                print("All player money has been reset to M1500.")
                break
            elif option.lower() == "n":
                break
            else:
                print("Please enter Y or N.")
        continue
    
    elif cmd_split[0] == "manual":
        print("""This command has been depracated as of v1.8.
For a guide to this CLI, view the README included in this foloder, or go to https://github.com/qpx5997/monopoly_EBank/blob/main/README.md.""")
        
    elif cmd_split[0] == "changelog":
        print("""PROGRAM CHANGELOG
v1.0 (26/10/2025): Initial release, can only handle money.
v1.1 (29/10/2025): Added player renaming and fixed a minor spelling error. Also did a bugfix.
v1.2 (31/10/2025): Did a bugfix.
v1.3 (07/11/2025): Added ltax and itax commands and did a bugfix.
v1.4 (17/02/2026): A minor edit where I changed the header to my new username. Forgot to update the version history command print in the program itself tho :\
v1.5 (17/02/2026): Changed tabs in the source code to spaces, fixed a bug, added a new chapter to the manual and added delp and addp commands.
v1.6 (22/02/2026): Did a bugfix involving unescaped quotes.
v1.7 (01/03/2026): Reserved special keywords and added the status command and comments. 
v1.8 (05/04/2026): Did bugfixes and added mtransi and mtranso commands, confirmation messages and stax alternative command. <-- CURRENT VERSION
v2.0 (FUTURE): Add property management.""")
        continue
        
    elif cmd_split[0] == "help":
        print("""QUICK COMMAND HELP
reset: Resets all money and properties.
add p1 100: Adds M100 to p1.
subt p1 100: Subtracts M100 from p1.
go p1: Gives M200 to p1.
set p1 2000: Sets p1's money to M2000.
trans p1 p2 10: Transfers M10 from p1 to p2.
vm p1: Shows p1's money.
vm ==all: Shows every player's money.
ren p1 someone: Renames p1 to someone.
exit: Quits the program.""")
        continue
        
    elif cmd_split[0] == "exit":
        while True:
            option = input("Are you sure you want to reset? [y/n] ")
            if option.lower() == "y":
                quit()
            elif option.lower() == "n":
                break
            else:
                print("Please enter Y or N.")
        continue
    
    try:
        if cmd_split[0] == "add":
            money[cmd_split[1]] += int(cmd_split[2]) # Adds money
            print(f"""M{cmd_split[2]} added to {cmd_split[1]}.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}""") # This print line displays command data; how much money was added, etc.
        
        elif cmd_split[0] == "subt":
            money[cmd_split[1]] -= int(cmd_split[2])
            print(f"""M{cmd_split[2]} subtracted from {cmd_split[1]}.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}""")
            
        elif cmd_split[0] == "trans":
            money[cmd_split[2]] += int(cmd_split[3])
            money[cmd_split[1]] -= int(cmd_split[3])
            print(f"""M{cmd_split[3]} transferred from {cmd_split[1]} to {cmd_split[2]}.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}
{cmd_split[2]}'s current balance: M{money[cmd_split[2]]}""")
        
        elif cmd_split[0] == "go":
            money[cmd_split[1]] += 200
            print(f"""M200 added to {cmd_split[1]}.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}""")
        
        elif cmd_split[0] == "set":
            money[cmd_split[1]] = int(cmd_split[2])
            print(f"""{cmd_split[1]}'s money set to M{cmd_split[2]}.""")
    
        elif cmd_split[0] == "vm":
            if cmd_split[1] == "==all":
                print(f"""ALL PLAYER CURRENT BALANCE:

{money}""")
            else:
                print(f"""{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}""")
                
        elif cmd_split[0] == "ren": # The if-clauses exist because if it ran like normal and someone typed only 2 arguments the program would end up deleting the player
            if cmd_split[2].startswith("=="):
                print("ERROR: Cannot rename a player name to a special keyword")
                continue
            if len(cmd_split) < 3:
                print(f"ERROR: Only {len(cmd_split)} argument(s) were given for command {cmd}")
            else:
                money[cmd_split[2]] = money.pop(cmd_split[1])
                print(f"""{cmd_split[1]} renamed to {cmd_split[2]}.
{cmd_split[2]}'s current balance: M{money[cmd_split[2]]}""")

        elif cmd_split[0] == "itax" or cmd_split[0] == "stax":
            money[cmd_split[1]] -= 200
            print(f"""M200 subtracted from {cmd_split[1]}.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}""")
            
        elif cmd_split[0] == "ltax":
            money[cmd_split[1]] -= 100
            print(f"""M100 subtracted from {cmd_split[1]}.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}""")

        elif cmd_split[0] == "addp":
            if len(cmd_split) > 2:
                money[cmd_split[1]] = int(cmd_split[2])
            elif len(cmd_split) <= 2:
                money[cmd_split[1]]  = 1500
            print(f"Player \"{cmd_split[1]}\" added with M{money[cmd_split[1]]}.")

        elif cmd_split[0] == "delp":
            money.pop(cmd_split[1])
            print(f"Player \"{cmd_split[1]}\" deleted.")

        elif cmd_split[0] == "mtransi":
            for player in money:
                if player != cmd_split[2]:
                    money[cmd_split[1]] += int(cmd_split[2])
                    money[player] -= int(cmd_split[2])
            print(f"""M{cmd_split[2]} transferred from each player to {cmd_split[1]}.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}
Enter vm ==all for all players' current balance.""")

        elif cmd_split[0] == "mtranso":
            for player in money:
                if player != cmd_split[2]:
                    money[cmd_split[1]] -= int(cmd_split[2])
                    money[player] += int(cmd_split[2])
            print(f"""M{cmd_split[2]} transferred from {cmd_split[1]} to each player.
{cmd_split[1]}'s current balance: M{money[cmd_split[1]]}
Enter vm ==all for all players' current balance.""")

        elif cmd_split[0] == "status":
            if cmd_split[1] == "==all":
                for player in money:
                    if money[player] < 0:
                        status = "Bankrupt (why are you still here???)"
                    elif money[player] == 0:
                        status = "Penniless, literally"
                    elif money[player] <= 30:
                        status = "Generally broke"
                    elif money[player] <= 100:
                        status = "Destitute"
                    elif money[player] <= 350:
                        status = "Impoverished"
                    elif money[player] <= 500:
                        status = "Poor"
                    elif money[player] <= 800:
                        status = "Lower Middle Class"
                    elif money[player] <= 1000:
                        status = "Upper Middle Class"
                    elif money[player] <= 1300:
                        status = "Affluent"
                    elif money[player] <= 1600:
                        status = "Upper Affluent"
                    elif money[player] <= 1900:
                        status = "Rich"
                    elif money[player] <= 2500:
                        status = "Really Rich"
                    elif money[player] <= 1000000:
                        status = "Filthy Rich"
                    elif money[player] <= 1000000000:
                        status = "Millionaire"
                    elif money[player] <= 1000000000000:
                        status = "Billionaire"
                    else:
                        status = "Cheater"

                    print(f"{player}'s status: {status}")

            else:
                if money[cmd_split[1]] < 0:
                    status = "Bankrupt (why are you still here???)"
                    # i know this giant if clause isnt too good but im just not too good at programming ok??
                    # REMINDER TO SELF: when changing one, make sure to apply it to the other giant if-building too
                elif money[cmd_split[1]] == 0:
                    status = "Penniless, literally"
                elif money[cmd_split[1]] <= 30:
                    status = "Generally broke"
                elif money[cmd_split[1]] <= 100:
                    status = "Destitute"
                elif money[cmd_split[1]] <= 350:
                    status = "Impoverished"
                elif money[cmd_split[1]] <= 500:
                    status = "Poor"
                elif money[cmd_split[1]] <= 800:
                    status = "Lower Middle Class"
                elif money[cmd_split[1]] <= 1000:
                    status = "Upper Middle Class"
                elif money[cmd_split[1]] <= 1300:
                    status = "Affluent"
                elif money[cmd_split[1]] <= 1600:
                    status = "Upper Affluent"
                elif money[cmd_split[1]] <= 1900:
                    status = "Rich"
                elif money[cmd_split[1]] <= 2500:
                    status = "Really Rich"
                elif money[cmd_split[1]] <= 1000000:
                    status = "Filthy Rich"
                elif money[cmd_split[1]] <= 1000000000:
                    status = "Millionaire"
                elif money[cmd_split[1]] <= 1000000000000:
                    status = "Billionaire"
                else:
                    status = "Cheater"

                print(f"{cmd_split[1]}'s status: {status}")

        elif cmd_split[0] == "#:":
            pass # comments

        else:
            print(f"ERROR: Unknown command \"{cmd_split[0]}\"")
            
    except KeyError:
        if cmd_split[0] == "trans":
            print(f"ERROR: Nonexistent transfer origin/destination \"{cmd_split[1]} {cmd_split[2]}\"")
        else:
            print(f"ERROR: Nonexistent player \"{cmd_split[1]}\"")

    except ValueError:
        if cmd_split[0] == "trans":
            print(f"ERROR: Invalid money value \"{cmd_split[3]}\"")
        else:
            print(f"ERROR: Invalid money value \"{cmd_split[2]}\"")

    except IndexError:
        print(f"ERROR: Only {len(cmd_split)} argument(s) were given for command {cmd}")