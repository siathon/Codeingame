# python3

"""
Input format:
    Line 1: User's longitude (in degrees)
    Line 2: User's latitude (in degrees)
    Line 3: The number N of defibrillators located in the streets of Montpellier
    N next lines: a description of each defibrillator

Output format:
    The name of the defibrillator located the closest to the user’s position.


"""

import math


class Defibrillator:
    def __init__(self, number, name, lon, lat):
        self.number = number
        self.name = name
        self.lon = lon
        self.lat = lat

    def caldistance(self, lon, lat):
        x = (lon - self.lon) * math.cos((self.lat + lat) / 2)
        y = lat - self.lat
        self.distance = math.sqrt((x ** 2) + (y ** 2)) * 6371


lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
defibs = []
for i in range(n):
    defib = input()
    index = defib.find(';')
    number = defib[:index]
    defib = defib[index + 1:]
    index = defib.find(';')
    name = defib[:index]
    defib = defib[index + 1:]
    index = defib.find(';')
    defib = defib[index + 1:]
    index = defib.find(';')
    defib = defib[index + 1:]
    index = defib.find(';')
    lo = float(defib[:index].replace(',', '.'))
    la = float(defib[index + 1:].replace(',', '.'))
    defibs.append(Defibrillator(number, name, lo, la))
    defibs[i].caldistance(lon, lat)

index = 0
dis = float('inf')
for i in range(len(defibs)):
    if defibs[i].distance < dis:
        dis = defibs[i].distance
        index = i
print(defibs[index].name)
