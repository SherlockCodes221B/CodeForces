number, k = map(int, input().split())
for i in range(k):
    number_s = str(number)
    if number_s[-1] == "0":
        number = number // 10
    else:
        number = number - 1
print(number)

