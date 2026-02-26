count_of_lower = 0
count_of_upper = 0
string = input()
for x in string:
    if x.islower():
        count_of_lower += 1
    else:
        count_of_upper += 1
if count_of_lower >= count_of_upper:
    print(string.lower())
if count_of_upper > count_of_lower:
    print(string.upper())