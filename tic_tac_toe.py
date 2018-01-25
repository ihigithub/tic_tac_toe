# -*- coding: utf-8 -*-
# tic tac toe for 2 players

import string
import os
clear = lambda: os.system('cls')

string.ascii_lowercase
alphabet = list(string.ascii_lowercase)


def print_board():
    print "  \033[4m %s \033[0m \033[4m %s \033[0m \033[4m %s \033[0m " % (alphabet[0], alphabet[1], alphabet[2])
    print "1!\033[4m %s \033[0m!\033[4m %s \033[0m!\033[4m %s \033[0m!" % (game_matrix[0][0],game_matrix[0][1],game_matrix[0][2])
    print "2!\033[4m %s \033[0m!\033[4m %s \033[0m!\033[4m %s \033[0m!" % (game_matrix[1][0],game_matrix[1][1],game_matrix[1][2])
    print "3!\033[4m %s \033[0m!\033[4m %s \033[0m!\033[4m %s \033[0m!" % (game_matrix[2][0],game_matrix[2][1],game_matrix[2][2])


if __name__ == "__main__":

    start = True
    game_matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = ["1","2"]
    player_marker = ["X", "O"]
    counter = 0
    while start:

        print_board()
        prompt = "your turn player %s:" % player[counter%2]
        step = raw_input(prompt)
        if len(step)==2 and (step[0]) in ["1","2","3"] and step[1] in ["a","b","c"]:
            row = int(step[0])-1
            column_alphabet = step[1]
            column = alphabet.index(column_alphabet)
            if game_matrix[row][column] == " ":
                game_matrix[row][column] = player_marker[counter%2]
                counter += 1
            else:
                print "choose another cell"
        else:
            print "invalid cell"


        #player 1 wins
        if  game_matrix[0][0] == game_matrix[0][1] == game_matrix[0][2] == "X" or \
            game_matrix[1][0] == game_matrix[1][1] == game_matrix[1][2] == "X" or \
            game_matrix[2][0] == game_matrix[2][1] == game_matrix[2][2] == "X" or \
            game_matrix[0][0] == game_matrix[1][0] == game_matrix[2][0] == "X" or \
            game_matrix[0][1] == game_matrix[1][1] == game_matrix[2][1] == "X" or \
            game_matrix[0][2] == game_matrix[1][2] == game_matrix[2][2] == "X" or \
            game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] == "X" or \
            game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0] == "X":
            print "test player 1 wins"
            break
        #player 2 wins
        if  game_matrix[0][0] == game_matrix[0][1] == game_matrix[0][2] == "O" or \
            game_matrix[1][0] == game_matrix[1][1] == game_matrix[1][2] == "O" or \
            game_matrix[2][0] == game_matrix[2][1] == game_matrix[2][2] == "O" or \
            game_matrix[0][0] == game_matrix[1][0] == game_matrix[2][0] == "O" or \
            game_matrix[0][1] == game_matrix[1][1] == game_matrix[2][1] == "O" or \
            game_matrix[0][2] == game_matrix[1][2] == game_matrix[2][2] == "O" or \
            game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] == "O" or \
            game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0] == "O":
            print "test player 2 wins"
            break

        if counter == 8:
            print "touchée"
            break

# TODO: clear console at every new step
# TODO: computer vs human

