# python3

"""
Input format:
    Input for one game turn:
        8 lines: one integer mountainH per line. 
        Each represents the height of one mountain given in the order of their index (from 0 to 7).
Output format:        
    Output for one game turn
        A single line with one integer for the index of which mountain to shoot.

"""

while True:
    m = 0
    index = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > m:
            m = mountain_h
            index = i

    # The index of the mountain to fire on.
    print(index)
