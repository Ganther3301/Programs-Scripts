#tic-tac-toe game 
import subprocess 
import sys

def screen_refresh():
    subprocess.run('clear')

    if len(pMoves)%2 == 0:
        print(p1.name+"'s turn\n")
    else:
        print(p2.name+"'s turn\n")

    screen=[one, two, three]
    for i in screen:
        for j in range(5):
            print(i[j], end=" ")

        print("\n")

class Player:
    name = ''

    def __init__(self, sign):
        self.sign = sign
        self.movement = set()

    def addMove(self, co_ord):
        self.movement.add(co_ord)
    
    def moves(self, co_ords):
        running = True
        try:
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
pMoves = []

winning = [
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
    if len(co_ords) > 2:
        input("Enter valid co-ordinates (PRESS ENTER TO CONTINUE)")
        continue

    if co_ord in pMoves:
        input("Move already played (PRESS ENTER TO CONTINUE)")
    else:
        if len(pMoves)%2 == 0:
            valid = p1.moves(co_ords)
            if valid:
                p1.addMove(co_ord)
                pMoves.append(co_ord)

                for move in winning:
                    if sorted(list(set(move)&p1.movement)) == move:
                        screen_refresh()
                        input(p1.name+" wins!!!!")
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
    if sorted(pMoves) == ['11', '12','13','21','22','23','31','32','33']:
        screen_refresh()
        input("DRAW :(")
        sys.exit()

