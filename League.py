firstPlace = "Elyashiv"
E1 = 3
W1 = 3
P1 = 3*E1 + W1
print("""
+--------+----------------+--------------------+----------+
|   Name |   Exact result |   Winning identity | PTS      |
+========+================+====================+==========+""")
print("|", firstPlace, "|\t", E1, "\t|\t", W1, "\t|\t", P1)

print("""Welcome to the Tribuna league!
Please enter your number:
1. Elyashiv
2. David
3. Yuval
4. Yehiam
5. Matanel
6. Shmuel""")
name = int(input())
if name == 1:
    name = "Elyashiv"
elif name == 2:
    name = "David"
elif name == 3:
    name = "Yuval"
elif name == 4:
    name = "Yehiam"
elif name == 5:
    name = "Matanel"
elif name == 6:
    name = "Shmuel"
print("Hello,", name)
home = input("Please enter the number of goals for the HOME team: ")
away = input("Please enter the number of goals for the AWAY team: ")
print("Your bet is:", home, "-", away, )
