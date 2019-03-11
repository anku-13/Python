#
# CS 224 Spring 2019
# Programming Assignment 2
#
# Your wonderful, pithy, erudite description of the assignment.
#
# Author: Julia Froegel
# Date: March 13, 2019
#

from random import randint
import copy
import platform
# colors - black white red green purple and orange
game_pattern = []
print_pattern = True

def create_new_game() :
    return [randint(0,5) for _ in range(4)]

def get_guess() :
    guess = raw_input("Guess Peg Colors: _ _ _ _ : \n[B|W|R|G|P|O]   : ").split(" ")
    switcher = {
        "B" : 0,
        "W" : 1,
        "R" : 2,
        "G" : 3,
        "P" : 4,
        "O" : 5
    }
    for i, color in enumerate(guess) :
        guess[i] = switcher.get(color);
    return guess;

def evaluate_guess(pattern) :
    global game_pattern
    b = 0
    w = 0
    gp = copy.deepcopy(game_pattern)
    for i, color in enumerate(pattern) :
        if color == gp[i] :
            b += 1
            gp[i] = -1
    for i, color in enumerate(pattern) :
        if color in gp :
            w += 1
    return [6 for _ in range(b)] + [7 for _ in range(w)]

def print_board(guessed_board) :
    switcher = {
        0 : " \033[1;30;47mB \033[1;36;40m",
        1 : "\033[1;37;40m W \033[1;36;40m",
        2 : "\033[1;31;40m R \033[1;36;40m",
        3 : "\033[1;32;40m G \033[1;36;40m",
        4 : "\033[1;35;40m P \033[1;36;40m",
        5 : "\033[1;33;40m O \033[1;36;40m",
        6 : " \033[1;30;47mb \033[1;36;40m",
        7 : "\033[1;37;40m w \033[1;36;40m"
    }
    print("________________________________")
    for guess in guessed_board :
        print("|"+" ".join([switcher.get(x) for x in guess[0]])+"|"+" ".join([switcher.get(x) for x in guess[1]]))
    print("________________________________")

def game_code() :
    global game_pattern
    print("\033[1;36;40m ___________MASTERMIND___________")
    guessed_board = []
    guess = []
    game_pattern = create_new_game()
    if print_pattern:
        print_board([[(game_pattern),[]]])
    while(guess != game_pattern) :
        guess = get_guess()
        pegs = evaluate_guess(guess)
        guessed_board.append([guess, pegs])
        print_board(guessed_board)
    print("YOU WIN!!! \033[1;0;40m")

def main() :
    if platform.system() == "Windows" :
        import colorama ## adds asnsi color escape sequences for windows
        colorama.init()
        game_code()
        colorama.deinit()
    else :
        game_code()

if __name__ == "__main__" :
    main()
