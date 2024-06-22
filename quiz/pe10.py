#H24126078 鄭雅云
#統計116

import curses
import random

def create_food(snake, obstacles, sh, sw, symbol):
    while True:
        food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        if food not in snake and food not in obstacles:
            return food, symbol

def create_obstacles(sh, sw):
    obstacles = []
    num_obstacles = (sh * sw) // 50  # 5% of the screen
    for _ in range(num_obstacles):
        length = random.randint(5, 10)
        if random.choice([True, False]):
            start_y = random.randint(1, sh - 2)
            start_x = random.randint(1, sw - length - 2)
            for i in range(length):
                obstacles.append([start_y, start_x + i])
        else:
            start_y = random.randint(1, sh - length - 2)
            start_x = random.randint(1, sw - 2)
            for i in range(length):
                obstacles.append([start_y + i, start_x])
    return obstacles

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(500)

    # Initialize snake
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    direction = curses.KEY_RIGHT

    # Create food and obstacles
    food, food_char = create_food(snake, [], sh, sw, 'π')
    special_food, special_food_char = create_food(snake, [], sh, sw, 'X')
    obstacles = create_obstacles(sh, sw)
    
    for obs in obstacles:
        win.addch(obs[0], obs[1], ' ', curses.A_REVERSE)

    win.addch(food[0], food[1], food_char)
    win.addch(special_food[0], special_food[1], special_food_char)

    paused = False
    normal_food_eaten = 0
    special_food_eaten = 0

    while True:
        next_key = win.getch()
        if next_key == -1:
            next_key = direction
        if next_key == 32:  # Space key to pause/unpause
            paused = not paused
            continue
        if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
            direction = next_key

        if paused:
            continue

        new_head = [snake[0][0], snake[0][1]]

        if direction == curses.KEY_DOWN:
            new_head[0] += 1
        if direction == curses.KEY_UP:
            new_head[0] -= 1
        if direction == curses.KEY_LEFT:
            new_head[1] -= 1
        if direction == curses.KEY_RIGHT:
            new_head[1] += 1

        # Wrap around screen boundaries
        new_head[0] %= sh
        new_head[1] %= sw

        if new_head in snake or new_head in obstacles:
            break

        snake.insert(0, new_head)

        if new_head == food:
            normal_food_eaten += 1
            food, food_char = create_food(snake, obstacles, sh, sw, 'π')
            win.addch(food[0], food[1], food_char)
        elif new_head == special_food:
            special_food_eaten += 1
            special_food, special_food_char = create_food(snake, obstacles, sh, sw, 'X')
            win.addch(special_food[0], special_food[1], special_food_char)
            if len(snake) > 1:
                snake.pop().pop()
        else:
            snake.pop() 

        win.clear()
        win.addch(food[0], food[1], food_char)
        win.addch(special_food[0], special_food[1], special_food_char)
        
        for obs in obstacles:
            win.addch(obs[0], obs[1], ' ', curses.A_REVERSE)

        for y, x in snake:
            win.addch(y, x, 'O')

        win.refresh()

    curses.endwin()
    print(f"Game Over! Normal food eaten: {normal_food_eaten}, Special food eaten: {special_food_eaten}")
    print("Reason: Snake hit an obstacle or itself!")

curses.wrapper(main)
