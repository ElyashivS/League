import datetime

E1, W1, PTS1, E2, W2, PTS2, E3, W3, PTS3, E4, W4, PTS4, E5, W5, PTS5, E6, W6, PTS6 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                                                                                     0, 0, 0, 0, 0, 0, 0
homeBet1, awayBet1, homeBet2, awayBet2, homeBet3, awayBet3, homeBet4, awayBet4, homeBet5, awayBet5, \
    homeBet6, awayBet6 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
HomeTeam = "Home Team"
AwayTeam = "Away Team"
Elyashiv = ["Elyashiv", E1, W1, PTS1, homeBet1, awayBet1]
David = ["David", E2, W2, PTS2, homeBet2, awayBet2]
Yuval = ["Yuval", E3, W3, PTS3, homeBet3, awayBet3]
Yehiam = ["Yehiam", E4, W4, PTS4, homeBet4, awayBet4]
Matanel = ["Matanel", E5, W5, PTS5, homeBet5, awayBet5]
Shmuel = ["Shmuel", E6, W6, PTS6, homeBet6, awayBet6]
endTimeBet = datetime.time.max.strftime("%H:%M:%S")

players = [Elyashiv, David, Yuval, Yehiam, Matanel, Shmuel]
running = True

while running:
    choice = 1
    print("""Welcome to the Tribuna league!
+---------+----------------+--------------------+----------+
|   Name  |   Exact result |   Winning identity |   PTS    |
+=========+================+====================+==========+""")

    players.sort(key=lambda x: x[3])
    players.reverse()

    first = players[0]
    second = players[1]
    third = players[2]
    forth = players[3]
    fifth = players[4]
    sixth = players[5]

    print("|", first[0], " |      ", first[1], "       |         ", first[2], "        |    ", first[3], "   |")
    print("+---------+----------------+--------------------+----------+")
    print("|", second[0], "|      ", second[1], "       |         ", second[2], "        |    ", second[3], "   |")
    print("+---------+----------------+--------------------+----------+")
    print("|", third[0], " |      ", third[1], "       |         ", third[2], "        |    ", third[3], "   |")
    print("+---------+----------------+--------------------+----------+")
    print("|", forth[0], "  |      ", forth[1], "       |         ", forth[2], "        |    ", forth[3], "   |")
    print("+---------+----------------+--------------------+----------+")
    print("|", fifth[0], "  |      ", fifth[1], "       |         ", fifth[2], "        |    ", fifth[3], "   |")
    print("+---------+----------------+--------------------+----------+")
    print("|", sixth[0] + "|      ", sixth[1], "       |         ", sixth[2], "        |    ", sixth[3], "   |")
    print("+=========+================+====================+==========+")

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
            for player in players:
                if player[4] == RHome and player[5] == RAway:
                    player[1] += 1
                    player[3] += 3
                    print(player[0], "got exact result, and gain 3 points")
                elif (player[4] > player[5] and RHome > RAway) or (player[4] < player[5] and RHome < RAway) or \
                        (player[4] == player[5] and RHome == RAway):
                    player[2] += 1
                    player[3] += 1
                    print(player[0], "got identity, and gain 1 points")

        elif choice == 3:
            HomeTeam = input("\tEnter the name of the HOME team: ")
            AwayTeam = input("\tEnter the name of the AWAY team: ")
        elif choice == 4:
            hour, minutes = int(input("Enter a hour: ")), int(input("Enter a minutes: "))
            endTimeBet = datetime.time(hour, minutes).strftime("%H:%M:%S")
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
        print("Hello,", name[0] + "!\nBet is open until " + str(endTimeBet))
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now < endTimeBet:
            name[4] = int(input("Please enter the number of goals for " + HomeTeam + ": "))
            name[5] = int(input("Please enter the number of goals for " + AwayTeam + ": "))
            print("Your bet is:", HomeTeam, name[4], "-", name[5], AwayTeam)
        else:
            print("Sorry," + name[0], "time of bet has passed.")
