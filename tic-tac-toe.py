#tic-tac-toe game 
import subprocess 
import sys

def screen_refresh():
    subprocess.run('clear')

    if len(pMoves)%2 == 0:              #It checks to see who's turn it is based on the number of moves played
        print(p1.name+"'s turn\n")
    else:
        print(p2.name+"'s turn\n")

    screen=[one, two, three]            #one, two and three are the lists which are the 1st, 2nd and 3rd rows respectively
    for i in screen:                    #This loop prints out the rows
        for j in range(5):              
            print(i[j], end=" ")        #The end = " " statement is so that all the contents of one, two, and three stay in the same line

        print("\n")

class Player:
    name = ''

    def __init__(self, sign):
        self.sign = sign                #sign means you know, 'X' or 'O'
        self.movement = set()           #This varaible is to track each player's moves. The reason for why it is a set is explained below

    def addMove(self, co_ord):
        self.movement.add(co_ord)       #This function adds the co-ordinate that the player has played to 'movement' variable
    
    def moves(self, co_ords):           #This function takes the co-ordinates and changes the list one, two or three accordingly.
        running = True
        try:                            #This is inside a try block because if the player just hits enter without typing anything, it gave an error.
            if co_ords[0] == '1':
                if co_ords[1] == '1':
                    one[1] = self.sign
                elif co_ords[1] == '2':
                    one[2] = self.sign
                elif co_ords[1] == '3':
                    one[3] = self.sign
                else:
                    input("Enter valid co-ordinates (PRESS ENTER TO CONTINUE)")
                    return False
    
            elif co_ords[0] == '2':
                if co_ords[1] == '1':
                    two[1] = self.sign
                elif co_ords[1] == '2':
                    two[2] = self.sign
                elif co_ords[1] == '3':
                    two[3] = self.sign
                else:
                    input("Enter valid co-ordinates (PRESS ENTER TO CONTINUE)")
                    return False
        
            elif co_ords[0] == '3':
                if co_ords[1] == '1':
                    three[1] = self.sign
                elif co_ords[1] == '2':
                    three[2] = self.sign
                elif co_ords[1] == '3':
                    three[3] = self.sign
                else:
                    input("Enter valid co-ordinates (PRESS ENTER TO CONTINUE)")
                    return False
        
            elif co_ords[0] == 'q':
                ans = input("Are you sure? (y/n)  ")
                if ans == 'y':
                    running = False
                    subprocess.run('clear')
                    sys.exit()
        
            else:
                input("Enter valid co-ordinates (PRESS ENTER TO CONTINUE)")
                return False

            return True

        except:
            if running == True:
                input("Enter valid co-ordinates (PRESS ENTER TO CONTINUE)")
                return False
            
            else:
                sys.exit()

one=['|','_','_','_','|']
two=['|','_','_','_','|']
three=['|','_','_','_','|']

subprocess.run('clear')

choice = input("a)X \nb)O \nPlayer1, Choose: ")
if choice == 'a':
    p1 = Player('X') 
    p2 = Player('O')
elif choice == 'b':
    p1 = Player('O') 
    p2 = Player('X')

p1.name = input("\nPlayer1's name: ")
p2.name = input("\nPlayer2's name: ")

running = True
pMoves = []     #This list stores all the moves played by all the players

winning = [                     #This list contains all the winning co-ordinates
    ['11','12','13'],
    ['21','22','23'],
    ['31','32','33'],

    ['11','22','33'],
    ['13','22','31'],

    ['11','21','31'],
    ['12','22','32'],
    ['13','23','33']
]

while running:
    screen_refresh()

    co_ord = input("Enter co-ordinates: ")
    co_ords = list(co_ord)
    if len(co_ords) > 2:        #Checks for validity of data
        input("Enter valid co-ordinates (PRESS ENTER TO CONTINUE)")
        continue

    if co_ord in pMoves:        #This condition is to make sure that they don't enter the same co-ordinates twice. This is one of the uses for pMoves list
        input("Move already played (PRESS ENTER TO CONTINUE)")
    else:
        if len(pMoves)%2 == 0:
            valid = p1.moves(co_ords)
            if valid:
                p1.addMove(co_ord)
                pMoves.append(co_ord)

                for move in winning:
                    if sorted(list(set(move)&p1.movement)) == move:     #This is the reason movement is a set. This performs an intersection of the player's movements and the lists inside the 
                        screen_refresh()                                #winning list and if the intersection is equal to the move in 'winning', that means the player has played the necessary 
                        input(p1.name+" wins!!!!")                      #co-ordinates to win, hence declares the player as the winner
                        sys.exit()

        else:
            valid = p2.moves(co_ords)
            if valid:
                p2.addMove(co_ord)
                pMoves.append(co_ord)

                for move in winning:
                    if sorted(list(set(move)&p2.movement)) == move:
                        screen_refresh()
                        input(p2.name+" wins!!!!")
                        sys.exit()

    pMoves.sort()
    if sorted(pMoves) == ['11', '12','13','21','22','23','31','32','33']:   #This condition checks if all the possible moves have been played by the players and if it is, declares the match as a 
        screen_refresh()                                                    #draw
        input("DRAW :(")
        sys.exit()

