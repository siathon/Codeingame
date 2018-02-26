# python3

"""
    Casablanca’s hippodrome is organizing a new type of horse racing: duals.
    During a dual, only two horses will participate in the race.
    In order for the race to be interesting, it is necessary to try to select two horses with similar strength.

    Input format:
        The message consisting of N ASCII characters
    Output format:
        The encoded message
"""

n = int(input())
horses = []
for i in range(n):
    horses.append(int(input()))

horses.sort()
difference = float('inf')
for i in range(1, n):
    temp = horses[i] - horses[i-1]
    if abs(temp) < difference:
        difference = temp
print(difference)
