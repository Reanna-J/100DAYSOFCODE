#Escaping the Maze
# Hurdle 3 Solution
# Platform: Reeborg's World
# Website: https://reeborg.ca
#
# How to run:
# 1. Open Reeborg's World
# 2. Select "Hurdle 3" from the world dropdown
# 3. Select Python as the language
# 4. Paste this code into the editor
# 5. Click the Run button

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
```
