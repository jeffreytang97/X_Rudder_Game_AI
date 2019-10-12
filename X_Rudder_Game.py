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
PS: Create a main function to run all the functions required instead of calling each function one by one.

"""

import sys

# Just an example
def initiate_game():
    print("Welcome to X-Rudder game! AHHHHH")

def run_Game_Main_Function():
    # This function will contain all the other functions that needs to be run.
    initiate_game()
    Board = BoardClass()
    Board.create_board()
    Board.print_board()
    Board.playerChoice()

class BoardClass:
    def __init__(self):
        print("Here is the board")
    
        # function to print/reset(?) the board
    def create_board(self):
        # print("\nideal board:\n")
        # print("10|_|_|_|_|_|_|_|_|_|_|_|_|")
        # print(" 9|_|_|_|_|_|_|_|_|_|_|_|_|")
        # print(" 8|_|_|_|_|_|_|_|_|_|_|_|_|")
        # print(" 7|_|_|_|_|x|_|_|_|_|_|_|_|")
        # print(" 6|_|_|_|_|_|o|x|_|_|_|_|_|")
        # print(" 5|_|_|_|_|_|_|_|o|_|_|_|_|")
        # print(" 4|_|_|_|_|_|_|_|_|_|_|_|_|")
        # print(" 3|_|_|_|_|_|_|_|_|_|_|_|_|")
        # print(" 2|_|_|_|_|_|_|_|_|_|_|_|_|")
        # print(" 1|_|_|_|_|_|_|_|_|_|_|_|_|")
        # print("   A B C D E F G H I J K L")
        #
        # print("")
        #
        # # printing board using double list - access to elements will be slower than dictionary
        # double_list = [["A!", "B!", "C!"], ["A9", "B9", "C9"], ["A8", "B8", "C8"]]
        # for xs in double_list:
        #     print("|".join(xs))
        #
        # print("")
    
        # proof of concept to show all the labelled tiles we'd have if implementing with dictionary
        # since a dictionary is used, modification of tiles when a player makes a move will be much
        # easier
        # for rule, checking, can check if certain keys have the same value for win condition?
        # all key, value pairs are manually defined... there has to be a better way to do this
        # self.dictionary_poc = {
        #     "A10": "A!",
        #     "B10": "B!",
        #     "C10": "C!",
        #     "D10": "D!",
        #     "E10": "E!",
        #     "F10": "F!",
        #     "G10": "G!",
        #     "H10": "H!",
        #     "I10": "I!",
        #     "J10": "J!",
        #     "K10": "K!",
        #     "L10": "L!",
        #     "A9": "A9",
        #     "B9": "B9",
        #     "C9": "C9",
        #     "D9": "D9",
        #     "E9": "E9",
        #     "F9": "F9",
        #     "G9": "G9",
        #     "H9": "H9",
        #     "I9": "I9",
        #     "J9": "J9",
        #     "K9": "K9",
        #     "L9": "L9",
        #
        #     "A8": "A8",
        #     "B8": "B8",
        #     "C8": "C8",
        #     "D8": "D8",
        #     "E8": "E8",
        #     "F8": "F8",
        #     "G8": "G8",
        #     "H8": "H8",
        #     "I8": "I8",
        #     "J8": "J8",
        #     "K8": "K8",
        #     "L8": "L8",
        #     "A7": "A7",
        #     "B7": "B7",
        #     "C7": "C7",
        #     "D7": "D7",
        #     "E7": "E7",
        #     "F7": "F7",
        #     "G7": "G7",
        #     "H7": "H7",
        #     "I7": "I7",
        #     "J7": "J7",
        #     "K7": "K7",
        #     "L7": "L7",
        #
        #     "A6": "A6",
        #     "B6": "B6",
        #     "C6": "C6",
        #     "D6": "D6",
        #     "E6": "E6",
        #     "F6": "F6",
        #     "G6": "G6",
        #     "H6": "H6",
        #     "I6": "I6",
        #     "J6": "J6",
        #     "K6": "K6",
        #     "L6": "L6",
        #     "A5": "A5",
        #     "B5": "B5",
        #     "C5": "C5",
        #     "D5": "D5",
        #     "E5": "E5",
        #     "F5": "F5",
        #     "G5": "G5",
        #     "H5": "H5",
        #     "I5": "I5",
        #     "J5": "J5",
        #     "K5": "K5",
        #     "L5": "L5",
        #
        #     "A4": "A4",
        #     "B4": "B4",
        #     "C4": "C4",
        #     "D4": "D4",
        #     "E4": "E4",
        #     "F4": "F4",
        #     "G4": "G4",
        #     "H4": "H4",
        #     "I4": "I4",
        #     "J4": "J4",
        #     "K4": "K4",
        #     "L4": "L4",
        #     "A3": "A3",
        #     "B3": "B3",
        #     "C3": "C3",
        #     "D3": "D3",
        #     "E3": "E3",
        #     "F3": "F3",
        #     "G3": "G3",
        #     "H3": "H3",
        #     "I3": "I3",
        #     "J3": "J3",
        #     "K3": "K3",
        #     "L3": "L3",
        #
        #     "A2": "A2",
        #     "B2": "B2",
        #     "C2": "C2",
        #     "D2": "D2",
        #     "E2": "E2",
        #     "F2": "F2",
        #     "G2": "G2",
        #     "H2": "H2",
        #     "I2": "I2",
        #     "J2": "J2",
        #     "K2": "K2",
        #     "L2": "L2",
        #     "A1": "A1",
        #     "B1": "B1",
        #     "C1": "C1",
        #     "D1": "D1",
        #     "E1": "E1",
        #     "F1": "F1",
        #     "G1": "G1",
        #     "H1": "H1",
        #     "I1": "I1",
        #     "J1": "J1",
        #     "K1": "K1",
        #     "L1": "L1",
        # }
    
        # final board
        # adding the row labels on each row will make tile checking more complex - we should discuss
        # if having labelled rows/columns is something we want to have

        self.board = {
            "R10": "10",
            "A10": "_",
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

            "R9": " 9",
            "A9": "_",
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

            "R8": " 8",
            "A8": "_",
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

            "R7": " 7",
            "A7": "_",
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

            "R6": " 6",
            "A6": "_",
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
            
            "R5": " 5",
            "A5": "_",
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

            "R4": " 4",
            "A4": "_",
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
            
            "R3": " 3",
            "A3": "_",
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

            "R2": " 2",
            "A2": "_",
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

            "R1": " 1",
            "A1": "_",
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

            "R0": "  ",
            "CA": "A",
            "CB": "B",
            "CC": "C",
            "CD": "D",
            "CE": "E",
            "CF": "F",
            "CG": "G",
            "CH": "H",
            "CI": "I",
            "CJ": "J",
            "CK": "K",
            "CL": "L",
        }

    def print_board(self):
        increment = 1
        for y in self.board:
            print(self.board[y], end='|')
            if increment % 13 == 0:
                print('')
            increment += 1
    
    def playerChoice(self):
        
        choice = input("Press 1 to player against another player. Press any to play against the computer: \n")            
        
        if choice is "1":
            print("Player against player game mode. The first player will be X and the second player will be O \n")
            moveToken = 0
            current_turn = 'X'
            placeToken = 0
            placeOrMove = '0'
            stop_game = False
            losing_on_move = False
            limit_reached = False

            while(moveToken + placeToken < 60):
                
                placeOrMove = input (current_turn + "'s turn: Press 1 to place a token or Press 2 to move a token.\n")

                while placeOrMove != "1" and placeOrMove != "2":
                    placeOrMove = input("Please press a valid key. (1 for placing token, 2 to move a token)\n")

                confirmChoice = input ("Are you sure? Press 1 to confirm. Press any other key to go back. \n")

                if(confirmChoice == "1"):                                 
                    # This is to prevent taking option 2 when no token is available to be moved    
                    if placeToken < 2 and placeOrMove == "2":
                            placeOrMove = input ("Your token has not been placed yet and cannot be moved. Therefore, please press 1 to place your token.\n")
                            while placeOrMove != "1":
                                placeOrMove = input("Please press 1 to place your token.\n")       
                        
                    # When player selected to add a token   
                    if placeOrMove is "1":
                        if(placeToken < 30):
                            limit_reached = False
                            if current_turn == 'X':
                                coordinate = input("Please input your coordinate (X's turn): \n")
                                token = "X"
                                stop_game = self.coordinate_selection(coordinate, token)
                                placeToken += 1
                            elif current_turn == 'O':
                                coordinate = input("Please input your coordinate (O's turn): \n")
                                token = "O"
                                stop_game = self.coordinate_selection(coordinate, token)
                                placeToken += 1
                        else:
                            print("Sorry, you have reached the maximum amount of token.\n")
                            limit_reached = True
                            
                    # When player selected to move a token       
                    elif placeOrMove is "2":
                        
                        print('Number of moves used by both players combined: ', moveToken+1)
                        
                        if(moveToken < 30):
                            stop_game, losing_on_move = self.coordinate_move(current_turn)
                            moveToken += 1
                            limit_reached = False
                        else:
                            print("Sorry, we have reached the maximum total amount of moves permitted which is 30.\n")
                            limit_reached = True
                        
                                            # Check if game has endeds    
                    if stop_game == True:
                        print('There is a winner in this game!!!')
                        break
                    elif losing_on_move == True:
                        print('The token you moved made you lose the game... There is a winner in this game')
                  
                    # If limit of token or movement reached but game can still go on...
                    # Don't count as turn for a player if didn't use it yet
                    if limit_reached == False:
                        # Every player plays once per turn (move or place token)
                        if current_turn == 'X':
                            current_turn = 'O'
                        else:
                            current_turn = 'X'
                        
                else:
                    print("Going Back. \n")

        else:
             print("Playing against computer \n")
             
    
    def coordinate_move(self, current_turn):
        dict = self.board
        flag_source = True
        flag_dest = True
       
         # First, check if the right token is selected.
        sourceCoor = input("Please enter the coordinate of the token you wish to move. \n")
        while flag_source:
            # Check if source coordinates exists on the board first
            if sourceCoor in dict:
                if dict.get(sourceCoor) == "X" and current_turn == 'X':
                    flag_source = False
                elif dict.get(sourceCoor) == "O" and current_turn == 'O':
                    flag_source = False
                
            if flag_source is True:
                sourceCoor = input("Please enter a valid coordinate that contains an " + current_turn + "'s token.\n")
                
        # Now, after the token has been selected, check if the destination coordinate is valid
        destinationCoor = input("Please enter the coordinate you wish to move to. \n")
        while flag_dest:
            if destinationCoor in dict:
                if dict.get(destinationCoor) == "_":
                    flag_dest = False
        
            if flag_dest is True:
                destinationCoor = input("Please enter a destination coordinate that is valid. \n")        
        
        token_to_move = dict.get(sourceCoor)
        # Change the current tile to "_" since we are going to move the token.
        stop_game = self.addCoordinate(sourceCoor, "_")                 # This stop_game boolean will be overwritten by the one below
        
        #-----------------------------------------------------------------------------------------------#
        # for this case, we want to check if a token movement will influence in his loss or not
        # If for example, O has been moved and that it was acting as a counter for an X formed by the other player, he will therefore lose.
        column, row = self.seperate_coordinate_values(sourceCoor)
        if token_to_move is 'X':
            opposite_token = 'O'
        elif token_to_move is 'O':
            opposite_token = 'X'
        # get the tile below the location of the token to be moved
        new_row = int(row)-1
        target_coord = column + str(new_row)
        flag = False
        losing_on_move = self.check_winning_condition(target_coord, opposite_token, flag)
        #-----------------------------------------------------------------------------------------------#
        
        # Now, add the token to the destination coordinate
        stop_game = self.addCoordinate(destinationCoor, token_to_move)
        self.print_board()
        
        return stop_game, losing_on_move
    
    
    def coordinate_selection(self, coordinate, token):

        # Human VS Human, Human VS Algorithm
        dict = self.board
        flag = True
        
        # while Flag is false, ask user to enter valid coordinates
        while flag:
            
            # If coordinate key exist in Dictionary
            # Check if the coordinate has already a value (X or O)
            if coordinate in dict:              
                if dict.get(coordinate) is "_":
                    flag = False

            if flag is True:
                coordinate = input("Please enter a valid coordinate: \n")    
            
        # Calling member function within a class, gotta use self
        stop_game = self.addCoordinate(coordinate, token)
        self.print_board()
        return stop_game
        
        
    def addCoordinate(self, coordinate, token):
        # Get user input stream and add coodrinates onto board
        # Has to alternated between X and O
        # changed the board so that you no longer need to check for tiles with "1 |"

        self.board[coordinate] = token
        flag = True
        # Everythime a token is added on the board, need to check if a player won.
        stop_game = self.check_winning_condition(coordinate, token, flag)
        return stop_game
    
    def seperate_coordinate_values(self, coordinate):
        # column = letters
        # row = numbers
        if len(coordinate) <= 2:
            column, row = coordinate
        else:
            column, row_element1, row_element2 = coordinate
            row = row_element1 + row_element2
        
        return column, row
    
    
    def check_X_condition(self, token, X_bottom_left_coord, X_upper_left_coord, X_bottom_right_coord, X_upper_right_coord, X_center_coord, flag):
        
        condition = False
        
        if token == "_":
            pass
        
        # Now that we have all the coordinates, check with the board to see if a X has been formed with the tokens.
        elif (self.board[X_bottom_left_coord] and self.board[X_upper_left_coord] and self.board[X_bottom_right_coord] and self.board[X_upper_right_coord] 
            and self.board[X_center_coord]) == token:
            
            if token is 'X':
                opposite_token = 'O'
            elif token is 'O':
                opposite_token = 'X'

            # get the middle coordinates of the possible X formed and check to see if the opposite player has countered the winning condition
            left_column, row = self.seperate_coordinate_values(X_bottom_left_coord)
            right_column, row = self.seperate_coordinate_values(X_bottom_right_coord)
            middle_row = int(row) + 1
            left_coord = left_column + str(middle_row)
            right_coord = right_column + str(middle_row)
            
            # Check if it is a legal winning condition
            if (self.board[left_coord] and self.board[right_coord]) == opposite_token and flag == True:
                # means that the player trying to form the X did not win yet because he got countered by the opposite player
                condition = False
            else:
                condition = True
                
        return condition
        

    # if flag is true, then we want to evaluate the X counter, if false, don't evaluate the X counter
    def check_winning_condition(self, coordinate, token, flag):
        
        """For this function, we check the surroundings of the location of the token added. If an X is formed, there is a winner depending 
            on whether it is a legal winning condition or not"""
        
        stop_game = False
        
        column, row = self.seperate_coordinate_values(coordinate)
        
        # To get column C if we added a token in column A for example
        two_on_the_right_column = chr(ord(column) + 2)
        # To get move 2 column to the left
        two_on_the_left_column = chr(ord(column) - 2)
        # To get middle column of the formed X on left
        X_center_column_left = chr(ord(column) - 1)
        # To get the middle column of the formed X on right
        X_center_column_right = chr(ord(column) + 1)
        # to get the coordinates of two rows above
        two_row_up = int(row) + 2
        # to get the coordinates of two rows below
        two_row_down = int(row) - 2
        # To get the center tile of the possible X formed above
        X_middle_row_up = int(row) + 1
        # to get the center tile of the possible X formed below
        X_middle_row_down = int(row) - 1
        
        #----------------------- Case 1: Winning conditions for 3 tiles for each LEFT corners on the board (A1,A2,B2,A9,A10,B10) -------------------- #
        if column == 'A' or column == 'B':
            # 3 tiles bottom left corner
            if row == '1' or (row == '2' and column == 'A'):
                # get the coordinates of all the 4 corners of the tiles where an X can be formed.
                X_bottom_left_coord = column + row
                X_upper_left_coord = column + str(two_row_up)
                X_bottom_right_coord = two_on_the_right_column + row
                X_upper_right_coord = two_on_the_right_column + str(two_row_up)
                X_center_coord = X_center_column_right + str(X_middle_row_up)
                stop_game = self.check_X_condition(token, X_bottom_left_coord, X_upper_left_coord, X_bottom_right_coord, X_upper_right_coord, X_center_coord, flag)
                
            # 3 tiles upper left corner
            elif (row == '9' and column == 'A') or row == '10':
                X_bottom_left_coord = column + str(two_row_down)
                X_upper_left_coord = column + row
                X_bottom_right_coord = two_on_the_right_column + str(two_row_down)
                X_upper_right_coord = two_on_the_right_column + row 
                X_center_coord = X_center_column_right + str(X_middle_row_down)
                stop_game = self.check_X_condition(token, X_bottom_left_coord, X_upper_left_coord, X_bottom_right_coord, X_upper_right_coord, X_center_coord, flag)
            
        #--------------------- Case 2: Winning conditions for 3 tiles for each RIGHT corners on the board (L1,L2,K2,L9,L10,K10) ----------------- #
        if column == 'K' or column == 'L':
            # 3 tiles bottom right corner
            if row == '1' or (row == '2' and column == 'L'):
                X_bottom_left_coord = two_on_the_left_column + row
                X_upper_left_coord = two_on_the_left_column + str(two_row_up)
                X_bottom_right_coord = column + row
                X_upper_right_coord = column + str(two_row_up)
                X_center_coord = X_center_column_left + str(X_middle_row_up)
                stop_game = self.check_X_condition(token, X_bottom_left_coord, X_upper_left_coord, X_bottom_right_coord, X_upper_right_coord, X_center_coord, flag)
                
            # 3 tiles upper right corner
            elif (row == '9' and column == 'L') or row == '10':
                # get the coordinates of all the 4 corners of the tiles where an X can be formed.
                X_bottom_left_coord = two_on_the_left_column + str(two_row_down)
                X_upper_left_coord = two_on_the_left_column + row
                X_bottom_right_coord = column + str(two_row_down)
                X_upper_right_coord = column + row
                X_center_coord = X_center_column_left + str(X_middle_row_down)
                stop_game = self.check_X_condition(token, X_bottom_left_coord, X_upper_left_coord, X_bottom_right_coord, X_upper_right_coord, X_center_coord, flag)
                
                
        #--------------------------- Case 2: -------------------------------- #
        
        
                
        return stop_game
    
run_Game_Main_Function()










