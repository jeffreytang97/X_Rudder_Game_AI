# -*- coding: utf-8 -*-
"""
Spyder Editor

Comp 472 - X-Rudder Game Development
Python Script
Date Created: 2019-09-23

Authors:
    - Jeffrey Tang
    - Hong Yi Wang
    - Ethan Tran
"""

"""
PS: Create a main function to run all the functions required instead of calling each function one by one.

"""

from GameTree import Node

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

            
    def user_turn(self, moveToken, current_turn, placeToken, placeOrMove, stop_game, losing_on_move, limit_reached):
        
         while(moveToken + placeToken < 60):
                
                placeOrMove = input (current_turn + "'s turn: Press 1 to place a token or Press 2 to move a token.\n")
                
                # For invalid keys
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
                        print('Game Over! Player ' + current_turn + ' has won the game!!!')
                        break
                    elif losing_on_move == True:
                        if current_turn == 'X':
                            opposite_token = 'O'
                        else:
                            opposite_token = 'X'
                        
                        print('The token you moved made you lose the game... Therefore, ' + opposite_token + ' has won the game!!!')
                        break
                    elif (moveToken + placeToken) >= 60:
                        print('Game has ended without a winner! IT IS A TIE GAME!!!')
                        break
                  
                    # If limit of token or movement reached but game can still go on...
                    # Don't count as turn for a player if didn't use it yet
                    if limit_reached == False:
                        # Every player plays once per turn (move or place token)
                        if current_turn == 'X':
                            current_turn = 'O'
                        else:
                            current_turn = 'X'
                else:
                    print("Going back. \n")
                    
                    
                    
        
    """
    Human turn method
    It's the same as the user_turn, except there is no alternation of tokens. The token is set.
    If Human starts, Human will always be X. If Human go second, Human will always be O.
    CHECK TOKEN IN THE ARGUMENT.
    
    """
    def Human_turn(self, current_turn, moveTokenHuman, placeTokenHuman, stop_game, losing_on_move):
        
        placeOrMove = input (current_turn + "'s turn: Press 1 to place a token or Press 2 to move a token.\n")
        confirmChoice = 0
        
        """
        Confirmation Block for each choice.
        """
        if(placeOrMove == "1" or placeOrMove == "2"):
            while(confirmChoice != "1"):
                # This is to prevent taking option 2 when no token is available to be moved    
                if(placeTokenHuman < 1 and placeOrMove == "2"):
                    placeOrMove = input ("Your token has not been placed yet and cannot be moved. Therefore, please press 1 to place your token.\n")
                    while placeOrMove != "1":
                        placeOrMove = input("Please press 1 to place your token.\n")
                confirmChoice = input ("Are you sure? Press 1 to confirm. Press any other key to go back. \n")
                if(confirmChoice == 1):
                    break
                else:
                    while(placeOrMove != "1" or placeOrMove != "2" and confirmChoice != "1"):
                        placeOrMove = input("Please press a valid key. (1 for placing token, 2 to move a token)\n")
                        # This is to prevent taking option 2 when no token is available to be moved    
                        if(placeTokenHuman < 1 and placeOrMove == "2"):
                            placeOrMove = input ("Your token has not been placed yet and cannot be moved. Therefore, please press 1 to place your token.\n")
                            while placeOrMove != "1":
                                placeOrMove = input("Please press 1 to place your token.\n")
                        confirmChoice = input ("Are you sure? Press 1 to confirm. Press any other key to go back. \n")
                        if(confirmChoice == 1):
                            break
        else:
            while(placeOrMove != "1" and placeOrMove != "2" and confirmChoice != "1"):
                placeOrMove = input("Please press a valid key. (1 for placing token, 2 to move a token)\n")
                # This is to prevent taking option 2 when no token is available to be moved    
                if(placeTokenHuman < 1 and placeOrMove == "2"):
                    placeOrMove = input ("Your token has not been placed yet and cannot be moved. Therefore, please press 1 to place your token.\n")
                    while placeOrMove != "1":
                        placeOrMove = input("Please press 1 to place your token.\n")
                confirmChoice = input ("Are you sure? Press 1 to confirm. Press any other key to go back. \n")
                if(confirmChoice == 1):
                    break
        """
        Confirmation Block ends here
        """            

        # When player selected to add a token   
        if placeOrMove == "1":
            if placeTokenHuman < 15:
                # limit_reached = False
                coordinate = input("Please input your coordinate (X's turn): \n")
                token = current_turn
                stop_game = self.coordinate_selection(coordinate, token)
                placeTokenHuman += 1
            else:
                print("Sorry, you have reached the maximum amount of token.\n")
                # limit_reached = True
        
        # When player selected to move a token           
        elif placeOrMove == "2":
            print('Number of moves used by you: ', moveTokenHuman+1)
            if moveTokenHuman < 15:
                stop_game, losing_on_game = self.coordinate_move(current_turn)
                moveTokenHuman += 1
                # limit_reached = False
            else:
                print("Sorry, we have reached the maximum total amount of moves permitted which is 15.\n")
                # limit_reached = True
                
        
        """
        Return values to check the Winning conditions.
        """
        return moveTokenHuman, placeTokenHuman, stop_game, losing_on_move
        
    """
    LIST THAT WILL CONTAIN COORDINATES OF TOKEN PLACED BY THE AI
    """
    coordinateListAI = []
    
    """The AI's turn method. Will call the Heuristic + Minimax methods"""
    def AI_turn(self, current_node, is_max, depth, tree_board, first_run, alpha, beta, moveTokenAI, placeTokenAI, current_turn):
        
        """
        Would need a way to track if AI did a MOVE or PLACE operation.
        Once that's found, will use the heuristic functions we created and the tree for it to make a decision.
        Once everything is done and the AI has made a move,
        return the moveTokenAI and placeTokenAI.
        
        """
        if is_max is True:
            token = 'X'
        else:
            token = 'O'
        stop_game = False

        """
        If the place token has reached 15, the AI cannot place anymore tokens, so it'd have to start moving tokens.        
        """
        # generate tree based on last played move
        self.generate_tree(current_node, is_max, depth, tree_board, first_run)
        # generated tree is run through alpha-beta
        best_heuristic = self.alpha_beta(current_node, depth, alpha, beta, is_max)

        if placeTokenAI <= 15:
            """
            Tree generation, heuristic, find the optimal coordinate.
            Save the coordinate in List.
            Place the coordinate.
            Increment placeTokenAI
            """
            AI_coordinate_placement = ''
            for branch_node in current_node.children:
                # alternatively, if best_heuristic - 0.1 <= elf.calculate_heuristic(branch_node) <= best_heuristic + 0.1
                if self.calculate_heuristic(branch_node) == best_heuristic:
                    AI_coordinate_placement = branch_node.potential_coordinate

            placeTokenAI += 1
            stop_game = self.addCoordinate(AI_coordinate_placement, token)

        else:
            """
            Tree generation, heuristic, find the optimal coordinate.
            Go through the List, check 2 tiles left, 2 tiles right. See if there are same token on those. If at least 1, go to next element in List.
            Finds the coordinate where it does not have any same type of token in 2 tiles left and 2 tiles right. Save that coordinate in variable.
            Update new coordinate (optimal coordinate) at that index in List.
            Move coordinate saved in variable to the optimal coordinate.
            Increment moveTokenAI
            """
            
            AI_coordinate_place = ''
            for branch_node in current_node.children:
                if(self.calculate_heuristic(branch_node) == best_heuristic):
                    AI_coordinate_place = branch_node.potential_coordinate
            
            dict = self.board
            for coordinate in self.coordinateListAI:
                letter, number = self.seperate_coordinate_values(coordinate)
                two_tiles_left = chr(ord(letter) - 2)
                two_tiles_right = chr(ord(letter) + 2)
                left_coor = two_tiles_left + str(number)
                right_coor = two_tiles_right + str(number)
                if(right_coor in dict):
                    if(dict.get(right_coor) == current_turn or dict.get(left_coor) == current_turn):
                        old_coor = coordinate
                        self.coordinateListAI[coordinate] = AI_coordinate_place #UPDATE TO THE NEW OPTIMAL COORDINATE. 
                        """Move the token in old coor to the Optimal coor."""
                        dict[dict.get(old_coor)] = "_"
                        dict[dict.get(AI_coordinate_place)] = current_turn
                        moveTokenAI += 1

        # 1. generate tree
        # 2. minimax on tree
        # 3. minimax returns the best heuristic to go for --> find the node that has this heuristic and go for it
        # can't figure out #3????????
        

        return placeTokenAI, moveTokenAI, stop_game
        
    
    def playerChoice(self):
        
        choice = input("Press 1 to play against another player. Press any key to play against the ai: \n")
        
        if choice is "1":
            print("Player against player chosen. The first player will be X and the second player will be O \n")
            moveToken = 0
            current_turn = 'X'
            placeToken = 0
            placeOrMove = '0'
            stop_game = False
            losing_on_move = False
            limit_reached = False

            self.user_turn(moveToken, current_turn, placeToken, placeOrMove, stop_game, losing_on_move, limit_reached)
        else:
            print("Player against ai chosen \n")

            choose_turn = input("Press 1 if you want to play first (X). Press any other key if you want to play second (O): \n")
            if choose_turn == '1':
                # MAX = User = X, MIN = computer AI = 0
                print("You are X. Computer AI will be O. You start.")
                moveTokenHuman = 0
                moveTokenAI = 0
                #current_turn = 'X'
                placeTokenHuman = 0
                placeTokenAI = 0
                placeOrMove = 0
                stop_game = False
                losing_on_move = False
                limit_reached = False

                """
                Thought of using the sum of moveToken and placeToken parity to check if it's Human or AI turn.
                THIS CASE: HUMAN GOES 1ST, AI GOES 2ND.
                If mod 2 = 0 -> Human turn and Human is X, else AI turn (AI is O).
                Number of total turn stays the same 60. 
                
                Will separate Place and Move counts for Human and for AI.
                
                """

                # initialize tree_board
                tree_board = BoardClass()
                tree_board.create_board()
                
                while(moveTokenHuman + moveTokenAI + placeTokenHuman + placeTokenAI < 60):
                    """
                    Once the game starts, the human will be X
                    """
                    if((moveTokenHuman + placeTokenHuman + moveTokenAI + placeTokenAI) % 2 == 0):
                        current_turn = 'X'
                        moveTokenHuman, placeTokenHuman, stop_game, losing_on_move = self.Human_turn(current_turn, moveTokenHuman, placeTokenHuman, stop_game, losing_on_move)

                    else:
                        tree_board = self.board
                        current_node = Node(tree_board, None)
                        current_turn = 'O'
                        self.AI_turn(current_node, False, 3, tree_board, False, float('inf'), float('-inf'), moveTokenAI, placeTokenAI, 'O')
                        self.print_board()

                        """
                        WILL NEED TO CALL THE AI HERE.
                        """



                    """
                    Below will check the condition of the game if it has ended and who's the winner.
                    Takes in the returned values from the method "Human_turn" and verify with the conditions below.
                    CHECKING THE CONDITION WILL NOT BE DONE INSIDE THE "Human_turn" METHOD. 
                    """                   
                    # Check if game has ended
                    if stop_game is True:
                        print('Game Over! Player ' + current_turn + ' has won the game!!!')
                        break
                    elif losing_on_move is True:
                        if current_turn == 'X':
                            opposite_token = 'O'
                        else:
                            opposite_token = 'X'
                        
                        print('The token you moved made you lose the game... Therefore, ' + opposite_token + ' has won the game!!!')
                        break
                    elif (moveTokenHuman + placeTokenHuman + moveTokenAI + placeTokenAI) >= 60:
                        print('Game has ended without a winner! IT IS A TIE GAME!!!')
                        break
                    
                    print(moveTokenHuman + moveTokenAI + placeTokenHuman + placeTokenAI)

            else:
                """
                AI WILL START FIRST.
                HUMAN GOES SECOND
                """
                # initialize tree_board
                tree_board = BoardClass()
                tree_board.create_board()
                tree_board = self.board
                root_node = Node(tree_board, None)

                # MAX = Computer AI = X, MIN = user = 0
                print("You are O. Computer AI will be X. Computer AI starts")
                
                moveTokenHuman = 0
                moveTokenAI = 0
                #current_turn = 'X'
                placeTokenHuman = 0
                placeTokenAI = 0
                placeOrMove = 0
                stop_game = False
                losing_on_move = False
                limit_reached = False
                first_run_AI = True
                
                
                """
                Thinking of calling the AI_turn here for it to make the first move and increments the moveTokenAI or placeTokenAI so that the sum becomes ODD.
                Since it's ODD, then goes in While loop and check ODD
                IF ODD, Human turn -> O
                Else EVEN, AI Turn -> X
                """
                
                while(moveTokenHuman + moveTokenAI + placeTokenHuman + placeTokenAI < 60):
                    """
                    Once the game starts, the human will be O
                    """
                    if((moveTokenHuman + placeTokenHuman + moveTokenAI + placeTokenAI) % 2 != 0):
                        current_turn = 'O'
                        moveTokenHuman, placeTokenHuman, stop_game, losing_on_move = self.Human_turn(current_turn, moveTokenHuman, placeTokenHuman, stop_game, losing_on_move)

                    else:
                        current_turn = 'X'
                        tree_board = self.board
                        current_node = Node(tree_board, 'E10')

                        if first_run_AI is True:
                            self.AI_turn(current_node, True, 3, tree_board, first_run_AI, float('inf'), float('-inf'), moveTokenAI, placeTokenAI, 'O')
                            self.print_board()
                            first_run_AI = False
                        else:
                            self.AI_turn(current_node, True, 3, tree_board, first_run_AI, float('inf'), float('-inf'), moveTokenAI, placeTokenAI, 'O')
                            self.print_board()

                    """
                        WILL NEED TO CALL THE AI_turn HERE.
                        """



                    """
                    Below will check the condition of the game if it has ended and who's the winner.
                    Takes in the returned values from the method "Human_turn" and verify with the conditions below.
                    CHECKING THE CONDITION WILL NOT BE DONE INSIDE THE "Human_turn" METHOD. 
                    """                   
                    # Check if game has ended
                    if stop_game == True:
                        print('Game Over! Player ' + current_turn + ' has won the game!!!')
                        break
                    elif losing_on_move == True:
                        if current_turn == 'X':
                            opposite_token = 'O'
                        else:
                            opposite_token = 'X'
                        
                        print('The token you moved made you lose the game... Therefore, ' + opposite_token + ' has won the game!!!')
                        break
                    elif (moveTokenHuman + placeTokenHuman + moveTokenAI + placeTokenAI) >= 60:
                        print('Game has ended without a winner! IT IS A TIE GAME!!!')
                        break
                    
                    print(moveTokenHuman + moveTokenAI + placeTokenHuman + placeTokenAI)
                  
                
    
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
        # Logic: Since the counter tokens are in the middle of the X formed, we either get the token from the tile below, if it exists, and then we check
        # if from there an X is formed. If so, the movement of that counter token made you lose.
        column, row = self.seperate_coordinate_values(sourceCoor)
        if token_to_move is 'X':
            opposite_token = 'O'
        elif token_to_move is 'O':
            opposite_token = 'X'
            
        #
        if row == '1':
            # If row is 1, we have to get the tile above the one we moved because 1 is the lowest number. It would go out of boudaries if lower
            new_row_above = int(row)+1
            losing_on_move = self.check_losing_on_move(column, new_row_above, opposite_token)
        else:
            # for this case, row 2 to 10, we always check below the token counter location
            new_row_below = int(row)-1
            losing_on_move = self.check_losing_on_move(column, new_row_below, opposite_token)
        #-----------------------------------------------------------------------------------------------#
        
        # Now, add the token to the destination coordinate
        stop_game = self.addCoordinate(destinationCoor, token_to_move)
        self.print_board()
        
        return stop_game, losing_on_move
    
    def check_losing_on_move(self, column, new_row, opposite_token):
        target_coord = column + str(new_row)
        place_token_flag = False                                                                           # Flag = false when move, true when add token
        losing_on_move = self.check_winning_condition(target_coord, opposite_token, place_token_flag)
        return losing_on_move
    
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
        place_token_flag = True
        # Everythime a token is added on the board, need to check if a player won.
        stop_game = self.check_winning_condition(coordinate, token, place_token_flag)
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
    
    
    def check_X_condition(self, X_bottom_left_coord, X_upper_left_coord, X_bottom_right_coord, X_upper_right_coord, X_center_coord, token, place_token_flag):
        
        condition = False
        dict = self.board
        
        # if there is no token at that coordinate, or that the coordinate to check the X condition does not exist, we pass and condition = false
        if token == "_":
            pass
        
        elif ((X_bottom_left_coord in dict) and (X_upper_left_coord in dict) and (X_bottom_right_coord in dict) and (X_upper_right_coord in dict) and (X_center_coord in dict)):
            # Now that we have all the coordinates, check with the board to see if a X has been formed with the tokens.
            if self.board[X_bottom_left_coord] == token and self.board[X_upper_left_coord] == token and self.board[X_bottom_right_coord] == token and self.board[X_upper_right_coord] == token and self.board[X_center_coord] == token:
                
                if place_token_flag == True:
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
                    if (self.board[left_coord] and self.board[right_coord]) == opposite_token:
                        # means that the player trying to form the X did not win yet because he got countered by the opposite player
                        condition = False
                    else:
                        condition = True
                else:
                    condition = True
                
        return condition

    # if flag is true, then we want to evaluate the X counter, if false, don't evaluate the X counter
    def check_winning_condition(self, coordinate, token, place_token_flag):
        
        """For this function, we check the surroundings of the location of the token added. If an X is formed, there is a winner depending 
            on whether it is a legal winning condition or not"""
        
        stop_game = False
        
        if token == "_":
            pass
        else:
            column, row = self.seperate_coordinate_values(coordinate)
            
            # To get column C if we added a token in column A for example
            two_on_the_right_column = chr(ord(column) + 2)
            # To get move 2 column to the left
            two_on_the_left_column = chr(ord(column) - 2)
            # To get middle column of the formed X on left
            X_one_column_left = chr(ord(column) - 1)
            # To get the middle column of the formed X on right
            X_one_column_right = chr(ord(column) + 1)
            # to get the coordinates of two rows above
            two_row_up = int(row) + 2
            # to get the coordinates of two rows below
            two_row_down = int(row) - 2
            # To get the center tile of the possible X formed above
            X_one_row_up = int(row) + 1
            # to get the center tile of the possible X formed below
            X_one_row_down = int(row) - 1
            
            
            """
            1- Check bottom left X possibility
            2- Check bottom right X possibility
            3- Check top left X possibility
            4- Check top right X possibility
            5- Check middle X possibility
            """
            
            # Check bottom left X possibility
            X_bottom_left_coord_1 = two_on_the_left_column + str(two_row_down)
            X_upper_left_coord_1 = two_on_the_left_column + row
            X_bottom_right_coord_1 = column + str(two_row_down)
            X_upper_right_coord_1 = column + row
            X_center_coord_1 = X_one_column_left + str(X_one_row_down)
            stop_game_1 = self.check_X_condition(X_bottom_left_coord_1, X_upper_left_coord_1, X_bottom_right_coord_1, X_upper_right_coord_1, X_center_coord_1, token, place_token_flag)
            
            # Check bottom right
            X_bottom_left_coord_2 = column + str(two_row_down)
            X_upper_left_coord_2 = column + row
            X_bottom_right_coord_2 = two_on_the_right_column + str(two_row_down)
            X_upper_right_coord_2 = two_on_the_right_column + row
            X_center_coord_2 = X_one_column_right + str(X_one_row_down)
            stop_game_2 = self.check_X_condition(X_bottom_left_coord_2, X_upper_left_coord_2, X_bottom_right_coord_2, X_upper_right_coord_2, X_center_coord_2, token, place_token_flag)
            
            # Check top left
            X_bottom_left_coord_3 = two_on_the_left_column + row
            X_upper_left_coord_3 = two_on_the_left_column + str(two_row_up)
            X_bottom_right_coord_3 = column + row
            X_upper_right_coord_3 = column + str(two_row_up)
            X_center_coord_3 = X_one_column_left + str(X_one_row_up)
            stop_game_3 = self.check_X_condition(X_bottom_left_coord_3, X_upper_left_coord_3, X_bottom_right_coord_3, X_upper_right_coord_3, X_center_coord_3, token, place_token_flag)
            
            # Check top right
            X_bottom_left_coord_4 = column + row
            X_upper_left_coord_4 = column + str(two_row_up)
            X_bottom_right_coord_4 = two_on_the_right_column + row
            X_upper_right_coord_4 = two_on_the_right_column + str(two_row_up)
            X_center_coord_4 = X_one_column_right + str(X_one_row_up)
            stop_game_4 = self.check_X_condition(X_bottom_left_coord_4, X_upper_left_coord_4, X_bottom_right_coord_4, X_upper_right_coord_4, X_center_coord_4, token, place_token_flag)
            
            # Check middle
            X_bottom_left_coord_5 = X_one_column_left + str(X_one_row_down)
            X_upper_left_coord_5 = X_one_column_left + str(X_one_row_up)
            X_bottom_right_coord_5 = X_one_column_right + str(X_one_row_down)
            X_upper_right_coord_5 = X_one_column_right + str(X_one_row_up)
            X_center_coord_5 = column + row
            stop_game_5 = self.check_X_condition(X_bottom_left_coord_5, X_upper_left_coord_5, X_bottom_right_coord_5, X_upper_right_coord_5, X_center_coord_5, token, place_token_flag)
            
            if stop_game_1 == True or stop_game_2 == True or stop_game_3 == True or stop_game_4 == True or stop_game_5 == True:
                stop_game = True
            
        return stop_game
    
    """ ****************************** AI MATERIAL ******************************"""

    # returns an int for number of winning combinations for a given tile
    def determine_possibilities_for_one_tile(self, node):
        coordinate = node.potential_coordinate
        column, row = self.seperate_coordinate_values(coordinate)
        max_token = 'X'
        min_token = 'O'

        # To get column C if we added a token in column A for example
        two_on_the_right_column = chr(ord(column) + 2)
        # To get move 2 column to the left
        two_on_the_left_column = chr(ord(column) - 2)
        # To get middle column of the formed X on left
        X_one_column_left = chr(ord(column) - 1)
        # To get the middle column of the formed X on right
        X_one_column_right = chr(ord(column) + 1)
        # to get the coordinates of two rows above
        two_row_up = int(row) + 2
        # to get the coordinates of two rows below
        two_row_down = int(row) - 2
        # To get the center tile of the possible X formed above
        X_one_row_up = int(row) + 1
        # to get the center tile of the possible X formed below
        X_one_row_down = int(row) - 1
    
        """
        1- Check bottom left X possibility
        2- Check bottom right X possibility
        3- Check top left X possibility
        4- Check top right X possibility
        5- Check middle X possibility
        """
        
        # Check bottom left X possibility
        X_bottom_left_coord_1 = two_on_the_left_column + str(two_row_down)
        X_upper_left_coord_1 = two_on_the_left_column + row
        X_bottom_right_coord_1 = column + str(two_row_down)
        X_upper_right_coord_1 = column + row
        X_center_coord_1 = X_one_column_left + str(X_one_row_down)
        
        # Check bottom right
        X_bottom_left_coord_2 = column + str(two_row_down)
        X_upper_left_coord_2 = column + row
        X_bottom_right_coord_2 = two_on_the_right_column + str(two_row_down)
        X_upper_right_coord_2 = two_on_the_right_column + row
        X_center_coord_2 = X_one_column_right + str(X_one_row_down)
        
        # Check top left
        X_bottom_left_coord_3 = two_on_the_left_column + row
        X_upper_left_coord_3 = two_on_the_left_column + str(two_row_up)
        X_bottom_right_coord_3 = column + row
        X_upper_right_coord_3 = column + str(two_row_up)
        X_center_coord_3 = X_one_column_left + str(X_one_row_up)
        
        # Check top right
        X_bottom_left_coord_4 = column + row
        X_upper_left_coord_4 = column + str(two_row_up)
        X_bottom_right_coord_4 = two_on_the_right_column + row
        X_upper_right_coord_4 = two_on_the_right_column + str(two_row_up)
        X_center_coord_4 = X_one_column_right + str(X_one_row_up)
        
        # Check middle
        X_bottom_left_coord_5 = X_one_column_left + str(X_one_row_down)
        X_upper_left_coord_5 = X_one_column_left + str(X_one_row_up)
        X_bottom_right_coord_5 = X_one_column_right + str(X_one_row_down)
        X_upper_right_coord_5 = X_one_column_right + str(X_one_row_up)
        X_center_coord_5 = column + row
        
        # Assume the program will check for all the X formed possibilities in the surroundings
        # calculating for X (max) token
        poss_counter_1, counter_density_1, X_block_1 = self.check_surrounding_X_possibilities(max_token, node.potential_board, X_bottom_left_coord_1, X_upper_left_coord_1, X_bottom_right_coord_1, X_upper_right_coord_1, X_center_coord_1)
        poss_counter_2, counter_density_2, X_block_2 = self.check_surrounding_X_possibilities(max_token, node.potential_board,X_bottom_left_coord_2, X_upper_left_coord_2, X_bottom_right_coord_2, X_upper_right_coord_2, X_center_coord_2)
        poss_counter_3, counter_density_3, X_block_3 = self.check_surrounding_X_possibilities(max_token, node.potential_board,X_bottom_left_coord_3, X_upper_left_coord_3, X_bottom_right_coord_3, X_upper_right_coord_3, X_center_coord_3)
        poss_counter_4, counter_density_4, X_block_4 = self.check_surrounding_X_possibilities(max_token, node.potential_board,X_bottom_left_coord_4, X_upper_left_coord_4, X_bottom_right_coord_4, X_upper_right_coord_4, X_center_coord_4)
        poss_counter_5, counter_density_5, X_block_5 = self.check_surrounding_X_possibilities(max_token, node.potential_board,X_bottom_left_coord_5, X_upper_left_coord_5, X_bottom_right_coord_5, X_upper_right_coord_5, X_center_coord_5)

        # add all the counters for one tile together
        possibilities_counter = poss_counter_1 + poss_counter_2 + poss_counter_3 + poss_counter_4 + poss_counter_5
        # take the highest tile density as the potential density when calculating the heuristic of placing a tile
        poss_density = max(counter_density_1, counter_density_2, counter_density_3, counter_density_4, counter_density_5)
        # take the highest block value for same reason as above?
        X_block = max(X_block_1, X_block_2, X_block_3, X_block_4, X_block_5)

        # calculating for O (min) token
        opposite_poss_counter_1, opposite_counter_density_1, opposite_X_block_1 = self.check_surrounding_X_possibilities(min_token, node.potential_board,X_bottom_left_coord_1, X_upper_left_coord_1, X_bottom_right_coord_1, X_upper_right_coord_1, X_center_coord_1)
        opposite_poss_counter_2, opposite_counter_density_2, opposite_X_block_2 = self.check_surrounding_X_possibilities(min_token, node.potential_board,X_bottom_left_coord_2, X_upper_left_coord_2, X_bottom_right_coord_2, X_upper_right_coord_2, X_center_coord_2)
        opposite_poss_counter_3, opposite_counter_density_3, opposite_X_block_3 = self.check_surrounding_X_possibilities(min_token, node.potential_board,X_bottom_left_coord_3, X_upper_left_coord_3, X_bottom_right_coord_3, X_upper_right_coord_3, X_center_coord_3)
        opposite_poss_counter_4, opposite_counter_density_4, opposite_X_block_4 = self.check_surrounding_X_possibilities(min_token, node.potential_board,X_bottom_left_coord_4, X_upper_left_coord_4, X_bottom_right_coord_4, X_upper_right_coord_4, X_center_coord_4)
        opposite_poss_counter_5, opposite_counter_density_5, opposite_X_block_5 = self.check_surrounding_X_possibilities(min_token, node.potential_board,X_bottom_left_coord_5, X_upper_left_coord_5, X_bottom_right_coord_5, X_upper_right_coord_5, X_center_coord_5)

        # add all the counters for one tile together
        opposite_possibilities_counter = opposite_poss_counter_1 + opposite_poss_counter_2 + opposite_poss_counter_3 + opposite_poss_counter_4 + opposite_poss_counter_5
        # take the highest tile density as the potential density when calculating the heuristic of placing a tile
        opposite_poss_density = max(opposite_counter_density_1, opposite_counter_density_2, opposite_counter_density_3, opposite_counter_density_4, opposite_counter_density_5)
        # take the highest block value for same reason as above?
        opposite_X_block = max(opposite_X_block_1, opposite_X_block_2, opposite_X_block_3, opposite_X_block_4, opposite_X_block_5)

        # return the number of possibilities to form an X for one tile.
        return possibilities_counter, poss_density, X_block, opposite_possibilities_counter, opposite_poss_density, opposite_X_block

    def check_surrounding_X_possibilities(self, token, potential_board, X_bottom_left_coord, X_upper_left_coord, X_bottom_right_coord, X_upper_right_coord, X_center_coord):
        dict = potential_board
        opposite_token = None
        poss_density = 0
        poss_counter = 0
        X_block = 0

        if token == 'X':
            opposite_token = 'O'
        elif token == 'O':
            opposite_token = 'X'

        if (X_bottom_left_coord and X_upper_left_coord and  X_bottom_right_coord and X_upper_right_coord and X_center_coord) in dict:

            # If the surroundings X is empty or does not contain the opposite token, +1 possibility
            if dict.get(X_bottom_left_coord) == ("_" or token) and dict.get(X_upper_left_coord) == ("_" or token) and dict.get(X_bottom_right_coord) == ("_" or token) and dict.get(X_upper_right_coord) == ("_" or token) and dict.get(X_center_coord) == ("_" or token):
                poss_counter += 1

            # section to measure how close a player is to forming an X
            if dict.get(X_bottom_left_coord) == token:
                poss_density += 1
            if dict.get(X_upper_left_coord) == token:
                poss_density += 1
            if dict.get(X_bottom_right_coord) == token:
                poss_density += 1
            if dict.get(X_upper_right_coord) == token:
                poss_density += 1
            if dict.get(X_center_coord) == token:
                poss_density += 1

            # section to measure if an opponent can block an X
            column, row = self.seperate_coordinate_values(X_center_coord)
            left_coord = chr(ord(column) - 1) + row
            right_coord = chr(ord(column) + 1) + row
            if left_coord == opposite_token:
                X_block += 1
            if right_coord == opposite_token:
                X_block += 1

        else:
            # out of the board
            pass

        return poss_counter, poss_density, X_block

    # store counter values in a list? or int?
    # if token with highest density has opposing token on either side on centre, return opposing value
    def block_x(self, max_state_density, min_state_density, max_blocked, min_blocked):
        to_block = 0
        blocked = 0

        # checking if a tile is worth blocking
        # these values probably need to be changed
        if max_state_density >= 3:
            if max_blocked == 1:
                to_block -= 2
            elif max_blocked == 2:
                to_block -= 3

        if min_state_density >= 3:
            if min_blocked == 1:
                to_block += 2
            elif min_blocked == 2:
                to_block += 3
                
        # these values probably need to be changed
        if max_blocked == 1:
            blocked -= 0.2
        if max_blocked == 2:
            blocked -= 0.2
        if max_blocked == 1:
            blocked += 0.2
        if max_blocked == 2:
            blocked += 0.2
        
        block_value = to_block + blocked
        
        return block_value

    # e(n) = number of X possibilities - number of O possibilities
    # We must check all the possibilities for all the tokens on the board
    # then, we calculate the heuristic value and we will select on which tile to be moved or placed.
    def calculate_heuristic(self, node):
        max_winning_configs, max_state_density, max_blocked, min_winning_configs, min_state_density, min_blocked = self.determine_possibilities_for_one_tile(node)

        # the number of possible winning configurations
        # add functionality to check multiple tiles for radius checking in future - maybe with for loop
        winning_configs = 0.2 * (max_winning_configs - min_winning_configs)

        # how close a player is to a winning state
        state_density = 0.3 * (max_state_density - min_state_density)

        # how close a player is to blocking another player
        block_state = 0.5 * self.block_x(max_state_density, min_state_density, max_blocked, min_blocked)

        heuristic = winning_configs + state_density + block_state

        return heuristic

    def alpha_beta(self, node, depth, alpha, beta, maximizing_player):
        if depth == 0 or node.children == []:
            return self.calculate_heuristic(node)
        if maximizing_player:
            value = float('-inf')
            for child in node.children:
                value = max(value, self.alpha_beta(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    # beta cut-off
                    break
            return value
        else:
            value = float('inf')
            for child in node.children:
                value = min(value, self.alpha_beta(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    # alpha cut-off
                    break
            return value

    """ pseudocode algorithm for depth-limited minimax and alpha-beta pruning - will need to credit this in the report

    function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if α ≥ β then
                break (* β cut-off *)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if α ≥ β then
                break (* α cut-off *)
        return value

    (* Initial call *)
    alphabeta(origin, depth, −∞, +∞, TRUE)
    """

    # function for generating a tree of depth 3 for possible moves for max and min
    # nodes will contain the coordinate or the key value of the board dictionary
    # a second board is created that is a copy of the actual game board
    # this board is used to help generate the tree that will be used by alpha-beta
    # this function currently only generates trees for placing tokens... NOT moving tokens
    def generate_tree(self, current_node, is_max, depth, tree_board, first_run):
        for potential_tile in tree_board:
            if potential_tile is not current_node.potential_coordinate:
                if potential_tile == "_":
                    # once a depth of 3 is reached for potential nodes, reset the tree_board and depth
                    # for other branches
                    if depth == 0 and first_run is True:
                        tree_board = self.board
                        depth = 3
                        while depth > 0:
                            if is_max is True:
                                tree_board[potential_tile] = 'X'
                                child_node = Node(tree_board, potential_tile)
                                current_node.add_child(child_node)
                                depth -= 1
                                self.generate_tree(child_node, not is_max, depth, tree_board, False)
                            elif is_max is False:
                                tree_board[potential_tile] = 'O'
                                child_node = Node(tree_board, potential_tile)
                                current_node.add_child(child_node)
                                depth -= 1
                                self.generate_tree(child_node, not is_max, depth, tree_board, False)

    # want to keep tiles for depth of 3 when traversing possibilities
    # cases: start of the game, tree is generated root node for max
    #      : tree is generated with max at the top of depth (Max's turn)
    #      : tree is generated with min at the top of depth (Min's turn)


run_Game_Main_Function()










