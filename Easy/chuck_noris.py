# python3

"""
    Input format:
        The message consisting of N ASCII characters
    Output format:
        The encoded message
"""

message = input()

binary = ''
for i in message:
    temp = bin(ord(i))[2:]
    if len(temp) < 7:
        temp = (7 - len(temp)) * '0' + temp
    binary += temp

unary = ''
state = 0

while binary:
    ch = binary[0]
    if state == 0:
        if ch == '1':
            unary += '0 0'
            state = 1
        elif ch == '0':
            unary += '00 0'
            state = 2
        binary = binary[1:]
    elif state == 1:
        if ch == '1':
            unary += '0'
            binary = binary[1:]
        elif ch == '0':
            unary += ' '
            state = 0
    elif state == 2:
        if ch == '0':
            unary += '0'
            binary = binary[1:]
        elif ch == '1':
            unary += ' '
            state = 0
print(unary)
