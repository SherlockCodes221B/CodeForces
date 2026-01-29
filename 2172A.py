'''
Three leading AI-powered creative assistants—Gemini, ChatGPT, and Claude—enter the first ever ASCII Art Contest, where they must impress a panel of human judges with their text-based masterpieces.

Each participant receives a score between 80 and 100 (inclusive). The organizers want to announce the final standing only if the judges' opinions are "close enough"; otherwise, they will ask the judges to reconsider.

Given the three integer scores of Gemini, ChatGPT, and Claude, determine the contest result:

If the maximum score and the minimum score differ by at least 10 points, print check again (the judging seems inconsistent, so the panel must re-evaluate).
Otherwise, print final X, where X is the median of the three scores (the score that would be in the middle if all three were sorted in non-decreasing order).
Input
A single line contains three integers g,c,ℓ
, representing the scores of Gemini, ChatGPT, and Claude respectively.

80≤g,c,ℓ≤100
Output
Print the required answer in a line.

'''

numbers = list(map(int, input().split()))
if max(numbers) - min(numbers) >= 10:
    print("check again")
else:
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    print(f"final {numbers[0]}")