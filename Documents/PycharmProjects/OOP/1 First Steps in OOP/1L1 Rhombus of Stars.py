# 1 Lab
# 1 First Steps in OOP

# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:


def rhombus_func(max):
    turn = max
    for i_ind in range(max):
        turn -= 1
        for interval in range(0, turn):
            print(" ", end="")
        for star_index in range(i_ind):
            print("*", end=" ")
        print("*")
    for i_ind in range(max-2, -1, -1):
        turn += 1
        for interval in range(0, turn):
            print(" ", end="")
        for star_index in range(i_ind):
            print("*", end=" ")
        print("*")

rhombus_func(int(input))