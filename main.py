from Player import Player
import datetime
import json

HomeTeam = "Home Team"
AwayTeam = "Away Team"
writeToTable = ""
bets = ""
abc = json.load(open('data.json'))


# Elyashiv = Player("Elyashiv", 0, 0, 0, 0, 0, datetime.time.max.strftime("%H:%M:%S"))
# David = Player("David", 0, 0, 0, 0, 0, None)
# Yuval = Player("Yuval", 0, 0, 0, 0, 0, None)
# Yehiam = Player("Yehiam", 0, 0, 0, 0, 0, None)
# Matanel = Player("Matanel", 0, 0, 0, 0, 0, None)
# Shmuel = Player("Shmuel", 0, 0, 0, 0, 0, None)

# Elyashiv.endTimeBet = abc[0]['endTimeBet']
# from_json = [Elyashiv, David, Yuval, Yehiam, Matanel, Shmuel]


with open('data.json', 'r') as data_file:
    json_data = data_file.read()

from_json = json.loads(json_data)

a = []  # Init an empty list
for i in from_json:  # Convert from "dict" type (like JSON) to Object type of Player
    s = Player(**i)
    a.append(s)

# Fill the object fields
Elyashiv = a[0]
David = a[1]
Yuval = a[2]
Yehiam = a[3]
Matanel = a[4]
Shmuel = a[5]

choice = 1
welcomeLine = """Welcome to the Tribuna league!
+---------+----------------+--------------------+----------+
|  Name   |  Exact result  |  Winning identity  |   PTS    |
+=========+================+====================+==========+"""

a.sort(key=lambda x: x.get_points(), reverse=True)

for i in a:
    writeToTable += i.get_stats() + "\n"
print(welcomeLine)
print(writeToTable)

print("""Please enter your number:
    1. Elyashiv
    2. David
    3. Yuval
    4. Yehiam
    5. Matanel
    6. Shmuel""")
name = int(input("\t"))
if name == 1:
    name = Elyashiv
    choice = int(input("""\t1. Bet
    2. Enter result of a game
    3. Enter next game teams
    4. Enter end time of betting
    """))
    if choice == 1:
        pass
    elif choice == 2:
        RHome = int(input("Enter score of HOME team: "))
        RAway = int(input("Enter score of AWAY team: "))
        for i in a:
            if i.get_home_bet() == RHome and i.get_away_bet() == RAway:
                i.set_exact_result(i.get_exact_result() + 1)
                i.set_points(i.get_points() + 3)
                print(i.get_name(), "bet", i.get_home_bet(), "-", i.get_away_bet(), "and got exact result!"
                                                                                    " good job. 3 points :)")
            elif (i.get_home_bet() > i.get_away_bet() and RHome > RAway) or \
                    (i.get_home_bet() < i.get_away_bet() and RHome < RAway) or \
                    (i.get_home_bet() == i.get_away_bet() and RHome == RAway):
                i.set_winning_identity(i.get_winning_identity() + 1)
                i.set_points(i.get_points() + 1)
                print(i.get_name(), "bet", i.get_home_bet(), "-", i.get_away_bet(), "and got identity. 1 point.")
            else:
                print(i.get_name(), "bet", i.get_home_bet(), "-", i.get_away_bet(), "and got nothing :D")

    elif choice == 3:
        HomeTeam = input("\tEnter the name of the HOME team: ")
        AwayTeam = input("\tEnter the name of the AWAY team: ")
    elif choice == 4:
        hour, minutes = int(input("Enter a hour: ")), int(input("Enter a minutes: "))
        Elyashiv.endTimeBet = datetime.time(hour, minutes).strftime("%H:%M:%S")

        print("The end time of the bet has updated to", Elyashiv.endTimeBet)

elif name == 2:
    name = David
elif name == 3:
    name = Yuval
elif name == 4:
    name = Yehiam
elif name == 5:
    name = Matanel
elif name == 6:
    name = Shmuel
if choice == 1:
    print("Hello," + name.get_name() + "!\nBet is open until " + str(Elyashiv.endTimeBet))
    now = datetime.datetime.now().strftime("%H:%M:%S")
    if now < Elyashiv.endTimeBet:
        name.set_home_bet(int(input("Please enter the number of goals for " + HomeTeam + ": ")))
        name.set_away_bet(int(input("Please enter the number of goals for " + AwayTeam + ": ")))
        bets += "\n" + name.get_name() + " bet is: " + str(HomeTeam) + " " + str(name.get_home_bet()) \
                + " - " + str(name.get_away_bet()) + " " + str(AwayTeam)
        print(bets)

    else:
        print("Sorry " + name.get_name() + ", time of bet has passed.")

j = json.dumps([o.dump() for o in a])  # Write data in JSON format

f = open("data.json", "w")
f.write(j)
f.close()
