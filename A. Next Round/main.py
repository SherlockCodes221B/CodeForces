'''
The first line of the input contains two integers n and k (1 ≤ k ≤n ≤50) separated by a single space.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), 
where ai is the score earned by the participant who got the i-th place. 
The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).

'''
def main(participents_count,position,scores):
    total_advanced = 0
    for point in scores:
        if point >= scores[position-1] and point != 0:
            total_advanced += 1
    print(total_advanced)

if __name__ == "__main__":
    participents_count, position = map(int, input().split(' '))
    scores = list(map(int, input().split(' '))) 

    main(participents_count, position, scores)