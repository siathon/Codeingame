"""
    Input format:
        Initialization input:
            lightX lightY initialTX initialTY
            (lightX, lightY) indicates the position of the light.
            (initialTX, initialTY) indicates the initial position of Thor.
        Input for a game round:
        remainingTurns

    Output format:
        Output for a game round:
            A single line providing the move to be made: N NE E SE S SW W or NW

"""

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())

    if initial_tx == light_x:
        if initial_ty < light_y:
            initial_ty += 1
            print("S")
        else:
            initial_ty -= 1
            print("N")
    elif initial_tx < light_x:
        initial_tx += 1
        if initial_ty == light_y:
            print("E")
        elif initial_ty < light_y:
            initial_ty += 1
            print("SE")
        else:
            initial_ty -= 1
            print("NE")
    else:
        initial_tx -= 1
        if initial_ty == light_y:
            print("W")
        elif initial_ty < light_y:
            initial_ty += 1
            print("SW")
        else:
            initial_ty -= 1
            print("NW")
