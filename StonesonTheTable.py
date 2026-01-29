n = input()
color_comb = str(input())
count = 0
for i in range(len(color_comb)-1):
    if color_comb[i] == color_comb[i+1]:
        count = count + 1
print(count)