# Robot Bounded in Box
# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three
# instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
# Example 1:
#
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:
#
# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
# Example 3:
#
# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
# Constraints:
# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.
def true_false(test_):
    x = None
    y = None
    last_x = None
    last_y = None
    last_x_2 = None
    last_y_2 = None
    last_x_3 = None
    last_y_3 = None
    turn = "L"
    if len(set(list(test_))) == 1 and set(list(test_)) == {'G'}:
        return False
    if len(set(list(test_))) == 2 and list(test_).count('G') == list(test_).count('L'):
        return True
    if len(set(list(test_))) == 2 and list(test_).count('G') == list(test_).count('R'):
        return True
    while x != 0 or y != 0:
        if x is None:
            x = 0
            y = 0
        for letter in list(test_):
            if letter == "L":
                if turn == "L":
                    turn = "R"
                elif turn == "R":
                    turn = "-L"
                elif turn == "-L":
                    turn = "-R"
                elif turn == "-R":
                    turn = "L"
            if letter == "R":
                if turn == "L":
                    turn = "-R"
                elif turn == "R":
                    turn = "L"
                elif turn == "-L":
                    turn = "R"
                elif turn == "-R":
                    turn = "-L"
            if letter == "G":
                if turn == "L":
                    x += 1
                elif turn == "-L":
                    x -= 1
                elif turn == "R":
                    y += 1
                elif turn == "-R":
                    y -= 1
        if last_x is None:
            last_y = y
            last_x = x
        elif last_x_2 is None:
            last_y_2 = y
            last_x_2 = x
            if x == 0 and y == 0:
                return True
        elif last_x_3 is None:
            last_y_3 = y
            last_x_3 = x
            if x == 0 and y == 0:
                return True
        else:
            if abs(last_x_2) < abs(x) or abs(last_x_3) < abs(x) or abs(last_x) < abs(x) or abs(last_y) < abs(y) or abs(
                    last_y_2) < abs(y) or abs(last_y_3) < abs(y):
                return False
    return True


def true_false_2(test_):
    turn_left = {
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
    }
    turn_right = {
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
    }
    direction = (1, 0)
    x = 0
    y = 0
    for letter in list(test_):
        if letter == "L":
            direction = turn_left[direction]
        elif letter == "R":
            direction = turn_right[direction]
        elif letter == "G":
            x += direction[0]
            y += direction[1]
    if x == 0 and y == 0 or direction != (1, 0):
        return True
    return False


tests = [
    ("GGLLGG", True),
    ("GG", False),
    ("GL", True),
    ("GLRLL", True),
    ('GGGLLL', True),
    ('GGLGRG', False),
    ('LLLLL', True),
    ('R', True),
    ('RGRRR', False),
    ('RLG', False),
    ("GRG", True),
    ("GGGR", True),
    ('LRGR', True),
    ('GR', True)
]

for test in tests:
    print(true_false(test[0]), 'ok' if true_false(test[0]) == test[1] else 'Wrong!')
    print(true_false_2(test[0]), 'ok' if true_false_2(test[0]) == test[1] else 'Wrong!')
    print()
