# -*- coding: utf-8 -*-
"""
Spyder Editor

Comp 472 - X-Rudder Game Development
Python Script
Date Created: 2019-09-23

Author:
    - Jeffrey Tang
    - Hong Yi Wang
    - Ethan Tran
"""

"""
PS: We should create a main function to run all the functions required instead of calling each function one by one.

"""
# Just an example
def test_example():
    print("Welcome to X-Rudder game!AHHHHH")

def run_Game_Main_Function():
    # This function will contain all the other functions that needs to be run.
    test_example()
    Board = BoardClass()
    Board.print_board()
    #entry_selection()
    Board.addCoordinate("A1", "X")
    Board.print_board()

class BoardClass:
    def __init__(self):
        print("This is the board")
    
        # function to print/reset(?) the board
    def print_board(self):
        print("\nideal board:\n")
        print("10|_|_|_|_|_|_|_|_|_|_|_|_|")
        print(" 9|_|_|_|_|_|_|_|_|_|_|_|_|")
        print(" 8|_|_|_|_|_|_|_|_|_|_|_|_|")
        print(" 7|_|_|_|_|x|_|_|_|_|_|_|_|")
        print(" 6|_|_|_|_|_|o|x|_|_|_|_|_|")
        print(" 5|_|_|_|_|_|_|_|o|_|_|_|_|")
        print(" 4|_|_|_|_|_|_|_|_|_|_|_|_|")
        print(" 3|_|_|_|_|_|_|_|_|_|_|_|_|")
        print(" 2|_|_|_|_|_|_|_|_|_|_|_|_|")
        print(" 1|_|_|_|_|_|_|_|_|_|_|_|_|")
        print("   A B C D E F G H I J K L")
    
        print("")
    
        # printing board using double list - access to elements will be slower than dictionary
        double_list = [["A!", "B!", "C!"], ["A9", "B9", "C9"], ["A8", "B8", "C8"]]
        for xs in double_list:
            print("|".join(xs))
    
        print("")
    
        # proof of concept to show all the labelled tiles we'd have if implementing with dictionary
        # since a dictionary is used, modification of tiles when a player makes a move will be much
        # easier
        # for rule, checking, can check if certain keys have the same value for win condition?
        # all key, value pairs are manually defined... there has to be a better way to do this
        self.dictionary_poc = {
            "A10": "A!",
            "B10": "B!",
            "C10": "C!",
            "D10": "D!",
            "E10": "E!",
            "F10": "F!",
            "G10": "G!",
            "H10": "H!",
            "I10": "I!",
            "J10": "J!",
            "K10": "K!",
            "L10": "L!",
            "A9": "A9",
            "B9": "B9",
            "C9": "C9",
            "D9": "D9",
            "E9": "E9",
            "F9": "F9",
            "G9": "G9",
            "H9": "H9",
            "I9": "I9",
            "J9": "J9",
            "K9": "K9",
            "L9": "L9",
    
            "A8": "A8",
            "B8": "B8",
            "C8": "C8",
            "D8": "D8",
            "E8": "E8",
            "F8": "F8",
            "G8": "G8",
            "H8": "H8",
            "I8": "I8",
            "J8": "J8",
            "K8": "K8",
            "L8": "L8",
            "A7": "A7",
            "B7": "B7",
            "C7": "C7",
            "D7": "D7",
            "E7": "E7",
            "F7": "F7",
            "G7": "G7",
            "H7": "H7",
            "I7": "I7",
            "J7": "J7",
            "K7": "K7",
            "L7": "L7",
    
            "A6": "A6",
            "B6": "B6",
            "C6": "C6",
            "D6": "D6",
            "E6": "E6",
            "F6": "F6",
            "G6": "G6",
            "H6": "H6",
            "I6": "I6",
            "J6": "J6",
            "K6": "K6",
            "L6": "L6",
            "A5": "A5",
            "B5": "B5",
            "C5": "C5",
            "D5": "D5",
            "E5": "E5",
            "F5": "F5",
            "G5": "G5",
            "H5": "H5",
            "I5": "I5",
            "J5": "J5",
            "K5": "K5",
            "L5": "L5",
    
            "A4": "A4",
            "B4": "B4",
            "C4": "C4",
            "D4": "D4",
            "E4": "E4",
            "F4": "F4",
            "G4": "G4",
            "H4": "H4",
            "I4": "I4",
            "J4": "J4",
            "K4": "K4",
            "L4": "L4",
            "A3": "A3",
            "B3": "B3",
            "C3": "C3",
            "D3": "D3",
            "E3": "E3",
            "F3": "F3",
            "G3": "G3",
            "H3": "H3",
            "I3": "I3",
            "J3": "J3",
            "K3": "K3",
            "L3": "L3",
    
            "A2": "A2",
            "B2": "B2",
            "C2": "C2",
            "D2": "D2",
            "E2": "E2",
            "F2": "F2",
            "G2": "G2",
            "H2": "H2",
            "I2": "I2",
            "J2": "J2",
            "K2": "K2",
            "L2": "L2",
            "A1": "A1",
            "B1": "B1",
            "C1": "C1",
            "D1": "D1",
            "E1": "E1",
            "F1": "F1",
            "G1": "G1",
            "H1": "H1",
            "I1": "I1",
            "J1": "J1",
            "K1": "K1",
            "L1": "L1",
        }
    
        increment = 1
        for y in self.dictionary_poc:
            print(self.dictionary_poc[y], end='|')
            if increment % 12 == 0:
                print('')
            increment += 1
    
        print("")
    
        # final board
        # adding the row labels on each row will make tile checking more complex - we should discuss
        # if having labelled rows/columns is something we want to have
        self.board = {
            "A10": "10|_",
            "B10": "_",
            "C10": "_",
            "D10": "_",
            "E10": "_",
            "F10": "_",
            "G10": "_",
            "H10": "_",
            "I10": "_",
            "J10": "_",
            "K10": "_",
            "L10": "_",
            
            "A9": "9 |_",
            "B9": "_",
            "C9": "_",
            "D9": "_",
            "E9": "_",
            "F9": "_",
            "G9": "_",
            "H9": "_",
            "I9": "_",
            "J9": "_",
            "K9": "_",
            "L9": "_",
    
            "A8": "8 |_",
            "B8": "_",
            "C8": "_",
            "D8": "_",
            "E8": "_",
            "F8": "_",
            "G8": "_",
            "H8": "_",
            "I8": "_",
            "J8": "_",
            "K8": "_",
            "L8": "_",
            
            "A7": "7 |_",
            "B7": "_",
            "C7": "_",
            "D7": "_",
            "E7": "_",
            "F7": "_",
            "G7": "_",
            "H7": "_",
            "I7": "_",
            "J7": "_",
            "K7": "_",
            "L7": "_",
    
            "A6": "6 |_",
            "B6": "_",
            "C6": "_",
            "D6": "_",
            "E6": "_",
            "F6": "_",
            "G6": "_",
            "H6": "_",
            "I6": "_",
            "J6": "_",
            "K6": "_",
            "L6": "_",
            "A5": "5 |_",
            "B5": "_",
            "C5": "_",
            "D5": "_",
            "E5": "_",
            "F5": "_",
            "G5": "_",
            "H5": "_",
            "I5": "_",
            "J5": "_",
            "K5": "_",
            "L5": "_",
    
            "A4": "4 |_",
            "B4": "_",
            "C4": "_",
            "D4": "_",
            "E4": "_",
            "F4": "_",
            "G4": "_",
            "H4": "_",
            "I4": "_",
            "J4": "_",
            "K4": "_",
            "L4": "_",
            "A3": "3 |_",
            "B3": "_",
            "C3": "_",
            "D3": "_",
            "E3": "_",
            "F3": "_",
            "G3": "_",
            "H3": "_",
            "I3": "_",
            "J3": "_",
            "K3": "_",
            "L3": "_",
    
            "A2": "2 |_",
            "B2": "_",
            "C2": "_",
            "D2": "_",
            "E2": "_",
            "F2": "_",
            "G2": "_",
            "H2": "_",
            "I2": "_",
            "J2": "_",
            "K2": "_",
            "L2": "_",
            
            "A1": "1 |_",
            "B1": "_",
            "C1": "_",
            "D1": "_",
            "E1": "_",
            "F1": "_",
            "G1": "_",
            "H1": "_",
            "I1": "_",
            "J1": "_",
            "K1": "_",
            "L1": "_",
    
            "A0": "   A",
            "B0": "B",
            "C0": "C",
            "D0": "D",
            "E0": "E",
            "F0": "F",
            "G0": "G",
            "H0": "H",
            "I0": "I",
            "J0": "J",
            "K0": "K",
            "L0": "L",
        }
    
        increment = 1
        for y in self.board:
            print(self.board[y], end='|')
            if increment % 12 == 0:
                print('')
            increment += 1
    
    def entry_selection(self):
        #Human VS Human, Human VS Algorithm
        print("lmao help")
    
    def addCoordinate(self, coordinate, token):
        #Get user input stream and add coodrinates onto board
        #Has to alternated between X and O
        print("It's gonna be fun")
#        if coordinate is "A1" or "A2" or "A3" or "A4" or "A5" or "A6" or "A7" or "A8" or "A9" or "A10":
#            self.board[coordinate] = "1 |" + token
#        else:
#            self.board[coordinate] = token
        self.board["B2"] = "X"
        

run_Game_Main_Function()