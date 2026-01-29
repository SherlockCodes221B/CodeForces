k, n ,w = input().split()
k = int(k)
n = int(n)
w = int(w)
total_amount_needed = 0
i = 1
while i <= w:
    total_amount_needed += (i*k)
    i = i + 1
if total_amount_needed >= n:
    needed_amount_to_borrow = total_amount_needed - n
    print(needed_amount_to_borrow)
else:
    print(0)