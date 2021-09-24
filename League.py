E1, W1, PTS1, E2, W2, PTS2 = 0, 0, 0, 0, 0, 0
homeBet1, awayBet1, homeBet2, awayBet2 = None, None, None, None
Elyashiv = ["Elyashiv", E1, W1, PTS1, homeBet1, awayBet1]
Yuval = ["Yuval", E2, W2, PTS2, homeBet2, awayBet2]
players = [Elyashiv, Yuval]
running = True
while running:

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
            RHome = int(input("Enter score of HOME team:"))
            RAway = int(input("Enter score of AWAY team:"))
            for player in players:
                if player[4] == RHome and player[5] == RAway:
                    print(player[0], "got exact result, and gain 3 points")
    # elif name == 2:
    #     name = "David"
    elif name == 3:
        name = Yuval
    # elif name == 4:
    #     name = Yehiam
    # elif name == 5:
    #     name = Matanel
    # elif name == 6:
    #     name = Shmuel
    # TODO How do I NOT enter this when I manage league?
    print("Hello,", name[0])
    name[4] = int(input("Please enter the number of goals for the HOME team: "))
    name[5] = int(input("Please enter the number of goals for the AWAY team: "))
    print("Your bet is:", name[4], "-", name[5])

