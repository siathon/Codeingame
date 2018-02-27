# python3

"""
Input format:
    Line 1: Number N of elements which make up the association table.
    Line 2: Number Q of file names to be analyzed.
    N following lines: One file extension per line and the corresponding MIME type (separated by a blank space).
    Q following lines: One file name per line.
    
Output format:
    For each of the Q filenames, display on a line the corresponding MIME type.
    If there is no corresponding type, then display UNKNOWN.

"""

n = int(input())
q = int(input())
fileTypes = {}
for i in range(n):
    ext, mt = input().split()
    fileTypes[ext.lower()] = mt
for i in range(q):
    fname = input()
    dotIndex = fname.rfind('.')
    if dotIndex == -1:
        print('UNKNOWN')
    else:
        ext = fname[dotIndex+1:].lower()
        if ext in fileTypes:
            print(fileTypes[ext])
        else:
            print('UNKNOWN')
