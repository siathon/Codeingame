# python3

"""
Input format:
    Line 1: the width L of a letter represented in ASCII art. All letters are the same width.
    Line 2: the height H of a letter represented in ASCII art. All letters are the same height.
    Line 3: The line of text T, composed of N ASCII characters.
    Following lines: the string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Represented in ASCII art.

Output format:
    The text T in ASCII art.
    The characters a to z are shown in ASCII art by their equivalent in upper case.
    The characters that are not in the intervals [a-z] or [A-Z] will be shown as a question mark in ASCII art.

Input example:
4
5
ZA
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #

"""

l = int(input())
h = int(input())
t = input()
ch = []
for i in t:
    c = ord(i)
    if c > 90 or c < 65:
        c = 91
    c -= 65
    ch.append(c)
print(ch)
row = []
out = []
for i in range(h):
    row = input()
    temp = ''
    for j in ch:
        temp += row[j*l:(j+1)*l]
    out.append(temp)
for i in out:
    print(i)
