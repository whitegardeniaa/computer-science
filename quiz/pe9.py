###H24126078 鄭雅云
###統計116

import random

def generate_path(N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly.

    maze = {}  ###先建立一個空字典
    for i in range(N):
        for j in range(M):
            maze[(i, j)] = 0  ###然後全部初始化為0

    cur_x, cur_y = 0, 0
    path = [[cur_x, cur_y]]

    while (cur_x != N-1 or cur_y != M-1): 
        if cur_x == N-1:  ###如果已經在最後一row，就往右走
            cur_y += 1
            path.append([cur_x, cur_y])
        elif cur_y == M-1:  ###如果已經在最後一col，就往下走
            cur_x += 1
            path.append([cur_x, cur_y])
        else:
            choice = random.choice(["right", "down"])  ###其他步數就random去選
            if choice == "right":
                cur_y += 1
                path.append([cur_x, cur_y])
            elif choice == "down":
                cur_x += 1
                path.append([cur_x, cur_y])

    path.append([cur_x, cur_y])

    for x, y in path:
        maze[(x, y)] = 2  ###題目說path叫做2
    
    return maze


def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

    obstacles = []
    while len(obstacles) != min_obstacles:
        coor_x = random.randint(0, N-1)
        coor_y = random.randint(0, M-1)
        if [coor_x, coor_y] not in obstacles and maze[(coor_x, coor_y)] != 2: ###建立障礙物但是不可以在路徑上
            obstacles.append([coor_x, coor_y])
    
    for x, y in obstacles:
        maze[(x, y)] = 1  ###題目說path叫做1

    return maze
    

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    while True:
        try:
            coor = list(map(int, input("Enter the coordinate to set an obstacle (i, j): ").split(",")))
            x, y = coor[0], coor[1]
            if not (0 <= x < N and 0 <= y < M):
                raise KeyError
        except (ValueError, KeyError):
            print("Invalid coordinates. Please input coordinates within the range.")
        else:
            if maze[(x, y)] == 2:
                print("Obstacle cannot be placed on the path.")
            elif maze[(x, y)] == 1:
                print("Obstacle already exists at this location.")
            else:
                maze[(x, y)] = 1
                print("Obstacle placed at", (x, y))
                break


def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    while True:
        try:
            coor = list(map(int, input("Enter the coordinate to remove an obstacle (i, j): ").split(",")))
            x, y = coor[0], coor[1]
            if not (0 <= x < N and 0 <= y < M):
                raise KeyError
        except (ValueError, KeyError):
            print("Invalid coordinates. Please input coordinates within the range.")
        else:
            if maze[(x, y)] == 2:
                print("Cannot remove obstacle from path cell.")
            elif maze[(x, y)] == 0:
                print("There's no obstacle at this location.")
            else:
                maze[(x, y)] = 0
                print("Obstacle removed at", (x, y))
                break


def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells.

    print("+" + "---+" * M)
    for i in range(N):  ###根據字典內容印出整個迷宮
        row_str = "|"
        for j in range(M):
            if maze[(i, j)] == 0:
                row_str += "   "
            elif maze[(i, j)] == 1:
                row_str += " X "
            elif maze[(i, j)] == 2:
                row_str += " O "
            row_str += "|"  ###這是最右邊的"|"
        print(row_str)
        print("+" + "---+" * M)


def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.
    while True:
        try:
            filename = input("Enter file name: ")
            if filename == "grid77.txt":
                n, m = 7, 7
            elif filename == "grid99.txt":
                n, m = 9, 9
            else:
                raise IOError
            f = open(filename, "r")
        except IOError:
            print("File not found. Please enter a valid file name.")
        else:
            break

    maze = generate_path(n, m)

    while True:
        try:
            min_ob = int(input("Enter the minimum number of obstacles (0-49): "))
            if not 0 <= min_ob <= 49:
                raise ValueError
        except ValueError:
            print("Invalid number of obstacles. Please enter a value between 0 and 56.")
        else:
            break

    maze = add_obstacles(maze, min_ob, n, m)
    print_maze(maze, n, m)
    
    while True:
        print("Options:\n1. Set obstacle\n2. Remove obstacle\n3. Print maze\n4. Exit")
        try:
            option = int(input("Enter your option: "))
            if option not in range(1, 5):
                raise ValueError
        except ValueError:
            print("Invalid option. Please choose a valid option.")
        else:
            if option == 1:
                set_obstacle(maze, n, m)
            elif option == 2:
                remove_obstacle(maze, n, m)
            elif option == 3:
                print_maze(maze, n, m)
            elif option == 4:
                break

if __name__ == "__main__":
    main()

