# python3

"""
Input format:
    Line 1: N, the number of temperatures to analyze
    Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output format:
    Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.

"""

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print('0')
else:
    m = 5527
    temp = 0
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        abst = abs(t)
        if abst < m:
            temp = t
            m = abst
        elif abst == m:
            if t > temp:
                temp = t
                m = abst
    print(temp)
