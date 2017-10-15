import os
import random
from itertools import permutations

os.system("clear")

global player_1, ai_human

class tac_Board():

    win_combo = [[1,2,3],[3,4,5],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    def __init__(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print("   |   |")
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("   |   |")
        print("____________")
        print("   |   |")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("   |   |")
        print("____________")
        print("   |   |")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))
        print("   |   |")


    @staticmethod
    def who_plays_first():
        if random.randint(0,1)== 1:
            choice = 'You'
            print ("You go First")
        else:
            if ai_human == "H":
                choice='Other'
                print ("Other go First")
            else:
                print ("Computer go First")
                choice ='Computer'
        return choice
            
    def get_Board_Copy(self):
    # Make a duplicate of the board list and return it the duplicate.
         dupeBoard = []
         for i in self.cells:
              dupeBoard.append(i)
              
         return dupeBoard
                    
    def update_board(self, cell_no, player):
        while not self.cells[cell_no]== " ":
            print("\nIt's Alreday occupied. Choose another cell no")
            cell_no = int(input("Choose another cell no. for "+player+"\n"))
        self.cells[cell_no] = player
           
   
    def is_winner1(self,mylist=[]):
        if len(mylist)<3:
            pass
        for combo in permutations(mylist, 3):
                    # loop through all possible combination of 3 from player_sq set
                    # return as tuples ex: (1,2,3), (3,2,1), (2,1,3)...
                    for wc in self.win_combo:
                        if combo == wc :
                            return True
        

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells +=1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
      
    def check_for_win(self,board,player):
       for wc in self.win_combo:
            result = True
                if board[wc] != player:
                    return False
            if result == True:
               return True
       return False

    def is_Space_Free(self):
        for i in range(1,10):
            if self.cells[i]!= " ":
                return True

    def ai_move(self,player,Board_Copy = []):
        if player == "X":
            Player_1 = "0"
        else:
            Player_1 = "X"

        #check for win
        for i in range(1,10):
             if self.cells[i] == " ":
                 Board_Copy[i] = player
                 if self.check_for_win(Board_Copy, player):
                     self.update_board(i,player)
                     return i
                     #break
                #Blocking the player
                 elif self.check_for_win(Board_Copy, Player_1):
                      self.update_board(i,player)
                      return i
                      break
                #If center is open, choose
                 elif self.cells[5]==" ":
                    #self.update_cell(5,player)
                      self.update_board(5,player)
                      return 5
                      break

                #Choose Random
                 else:
                    if self.cells[i] == " ":
                         self.update_board(i,player)
                         return i
    
        
obj_board = tac_Board()


def refresh_screen():
    #Clear screen
    os.system("clear")

    print("Tic-Tac-Toe World\n")

    #show the board
    obj_board.display()

#to restart again
def play_again():
    play_again = input("Do you want to restart? Y/N \n").upper()
    if(play_again != "Y" or play_again !="N"):
       print('Do you want to play again? "Y / N" ') 
    obj_board.reset()
    if play_again == 'N' or play_again == 'n':
        sys.exit()
    

#Players
Players ={'C': 'Computer',
          'H': 'Player 2' 
    }                   

#choose user input
Player_1= input("\nPlease choose O or X)")
if Player_1 == 'O' or Player_1 == 'X':
    print("You chose {0}".format(Player_1))
else:
    Player_1 = input("\nPlease from choose 0 or X)")

if Player_1 == "X":
            Player_2 = "0"
else:
            Player_2 = "X"
#select other user
ai_human = input('\nWhom you want to play against?\n Choose "C" to play against Computer or "H" against human ').upper()
while not (ai_human == 'C' or ai_human == 'H'):
   print('Do you want to play with Computer "C" or Human "H"?\n')
   ai_human = input().upper()

print("You Playing with "+ Players[ai_human]+"\nGood Luck!\n")

#list to store moves
list1 = []
list2 = []
while True: 

    #refresh_screen()
    player_first = obj_board.who_plays_first()
    game_is_playing = True
    while game_is_playing:
        if player_first =='You':

            #set user input
            X_choice = int(input("\n Please choose cell no 1-9.> "))
            list1.append(X_choice)

            #update board
            obj_board.update_board(X_choice,Player_1)
     
            refresh_screen()            
            #Check for Winner
            if obj_board.is_winner1(list1):
                    print("Congratulations! You are winner \n")
                    list1=[]
                    game_is_playing = False
                    play_again()
            #Check for Tie
            elif obj_board.is_tie():
                    print("This ends to a Tie game! \n")
                    game_is_playing = False
                    play_again()
            else:
                    player_first = 'Other'

        #set user input
        else:
            if ai_human == "H":
                  o_choice = int(input("Please choose cell no 1-9.>"))
                  list2.append(o_choice)

                  #update board
                  obj_board.update_board(o_choice,Player_2)
                  refresh_screen()
                  if obj_board.is_winner1(list2):
                            print("Congratulations! ", Players[ai_human]+" is winner \n")
                            list2 = []
                            game_is_playing = False
                            play_again()
                  #Check for Tie
                  elif obj_board.is_tie():
                            print("This ends to a Tie game! \n")
                            game_is_playing = False
                            play_again()
                  else:
                            player_first = 'You'
            else:
                    Board_copy = obj_board.get_Board_Copy()
                    o_choice = obj_board.ai_move(Player_2,Board_copy)
                    list2.append(o_choice)
                    refresh_screen()    

                    #Check for Winner
                    if obj_board.is_winner1(list2):
                        print( Players[ai_human] +" is winner \n")
                        list2 = []
                        game_is_playing = False
                        play_again()

                    #Check for Tie
                    elif obj_board.is_tie():
                        print("This ends to a Tie game! \n")
                        game_is_playing = False
                        play_again()
                    else:
                        player_first ='You'

