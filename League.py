E1, W1, PTS1, E2, W2, PTS2, E3, W3, PTS3, E4, W4, PTS4, E5, W5, PTS5, E6, W6, PTS6 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                                                                                     0, 0, 0, 0, 0, 0, 0
homeBet1, awayBet1, homeBet2, awayBet2, homeBet3, awayBet3, homeBet4, awayBet4, homeBet5, awayBet5,\
    homeBet6, awayBet6 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
Elyashiv = ["Elyashiv", E1, W1, PTS1, homeBet1, awayBet1]
David = ["David", E2, W2, PTS2, homeBet2, awayBet2]
Yuval = ["Yuval", E3, W3, PTS3, homeBet3, awayBet3]
Yehiam = ["Yehiam", E4, W4, PTS4, homeBet4, awayBet4]
Matanel = ["Matanel", E5, W5, PTS5, homeBet5, awayBet5]
Shmuel = ["Shmuel", E6, W6, PTS6, homeBet6, awayBet6]
players = [Elyashiv, Yuval]
running = True

while running:
    choice = 1
    print("""Welcome to the Tribuna league!
    +--------+----------------+--------------------+----------+
    |   Name |   Exact result |   Winning identity | PTS      |
    +========+================+====================+==========+""")
    print("|", Elyashiv[0], "|\t", Elyashiv[1], "\t|\t", Elyashiv[2], "\t|\t", Elyashiv[3])
    print("|", Yuval[0], "|\t", Yuval[1], "\t|\t", Yuval[2], "\t|\t", Yuval[3])

    print("""Please enter your number:
    1. Elyashiv
    2. David
    3. Yuval
    4. Yehiam
    5. Matanel
    6. Shmuel""")
    name = int(input())
    if name == 1:
        name = Elyashiv
        choice = int(input("Press 1 to bet, Press 2 to manage league: "))
        if choice == 1:
            pass
        elif choice == 2:
            RHome = int(input("Enter score of HOME team: "))
            RAway = int(input("Enter score of AWAY team: "))
            for player in players:
                if player[4] == RHome and player[5] == RAway:
                    player[1] += 1
                    player[2] += 1
                    player[3] += 3
                    print(player[0], "got exact result, and gain 3 points")
                elif (player[4] > player[5] and RHome > RAway) or (player[4] < player[5] and RHome < RAway) or \
                        (player[4] == player[5] and RHome == RAway):
                    player[2] += 1
                    player[3] += 1
                    print(player[0], "got identity, and gain 1 points")
    elif name == 2:
        name = "David"
    elif name == 3:
        name = Yuval
    elif name == 4:
        name = Yehiam
    elif name == 5:
        name = Matanel
    elif name == 6:
        name = Shmuel
    if choice != 2:
        print("Hello,", name[0])
        name[4] = int(input("Please enter the number of goals for the HOME team: "))
        name[5] = int(input("Please enter the number of goals for the AWAY team: "))
        print("Your bet is:", name[4], "-", name[5])

