# python3

"""
    Input format:
        Initialization input:
            Line 1: the number surfaceN of points used to draw the surface of Mars.
            Next surfaceN lines: a couple of integers landX landY providing the coordinates of a ground point.
        Input for a game round:
        A single line with 7 integers: X Y hSpeed vSpeed fuel rotate power

    Output format:
        Output for a game round:
            A single line with 2 integers: rotate power

"""

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. (0 to 2999)
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # 2 integers: rotate power.
    if v_speed <= -39:
        print("0 4")
    else:
        print("0 3")
