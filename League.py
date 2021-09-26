from Player import Player
import datetime

HomeTeam = "Home Team"
AwayTeam = "Away Team"
endTimeBet = datetime.time.max.strftime("%H:%M:%S")

Elyashiv = Player("Elyashiv", 0, 0, 0, 0, 0)
David = Player("David", 0, 0, 0, 0, 0)
Yuval = Player("Yuval", 0, 0, 0, 0, 0)
Yehiam = Player("Yehiam", 0, 0, 0, 0, 0)
Matanel = Player("Matanel", 0, 0, 0, 0, 0)
Shmuel = Player("Shmuel", 0, 0, 0, 0, 0)

players = [Elyashiv, David, Yuval, Yehiam, Matanel, Shmuel]
running = True

while running:
    choice = 1
    print("""Welcome to the Tribuna league!
+---------+----------------+--------------------+----------+
|   Name  |   Exact result |   Winning identity |   PTS    |
+=========+================+====================+==========+""")

    players.sort(key=lambda x: x.get_points(), reverse=True)

    first = players[0]
    second = players[1]
    third = players[2]
    forth = players[3]
    fifth = players[4]
    sixth = players[5]

    print("|", first.get_name(), " |", first.get_exact_result(), "|", first.get_winning_identity(), "|", first.get_points(), "|")
    print("+---------+----------------+--------------------+----------+")
    print("|", second.get_name(), "|", second.get_exact_result(), "|", second.get_winning_identity(), "|", second.get_points(), "|")
    print("+---------+----------------+--------------------+----------+")
    print("|", third.get_name(), "|", third.get_exact_result(), "|", third.get_winning_identity(), "|", third.get_points(), "|")
    print("+---------+----------------+--------------------+----------+")
    print("|", forth.get_name(), "|", forth.get_exact_result(), "|", forth.get_winning_identity(), "|", forth.get_points(), "|")
    print("+---------+----------------+--------------------+----------+")
    print("|", fifth.get_name(), "|", fifth.get_exact_result(), "|", fifth.get_winning_identity(), "|", fifth.get_points(), "|")
    print("+---------+----------------+--------------------+----------+")
    print("|", sixth.get_name() + "|", sixth.get_exact_result(), "|", sixth.get_winning_identity(), "|", sixth.get_points(), "|")
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
            for i in players:
                if i.get_home_bet() == RHome and i.get_away_bet() == RAway:
                    i.set_exact_result(i.get_exact_result() + 1)
                    i.set_points(i.get_points() + 3)
                    print(i.get_name(), "got exact result, and gain 3 points")
                elif (i.get_home_bet() > i.get_away_bet() and RHome > RAway) or (i.get_home_bet() < i.get_away_bet() and RHome < RAway) or \
                        (i.get_home_bet() == i.get_away_bet() and RHome == RAway):
                    i.set_winning_identity(i.get_winning_identity() + 1)
                    i.set_points(i.get_points() + 1)
                    print(i.get_name(), "got identity, and gain 1 points")

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
        print("Hello,", name.get_name() + "!\nBet is open until " + str(endTimeBet))
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now < endTimeBet:
            name.set_home_bet(int(input("Please enter the number of goals for " + HomeTeam + ": ")))
            name.set_away_bet(int(input("Please enter the number of goals for " + AwayTeam + ": ")))
            print("Your bet is:", HomeTeam, name.get_home_bet(), "-", name.get_away_bet(), AwayTeam)
        else:
            print("Sorry," + name.get_name(), "time of bet has passed.")
