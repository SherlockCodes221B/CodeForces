n=int(input())
games = str(input())
a = 0
d = 0
for x in games:
    if x == "A":
        a = a + 1
    elif x == "D":
        d = d + 1
if a > d:
    print("Anton")
elif a==d:
    print("Friendship")
else:
    print("Danik")
