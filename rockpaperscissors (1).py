#ella
#1/6/25
#rock paper scissors

#init
import random

precord = 0 #person record
crecord = 0 #computer record
#functions
def game(): #plays the game
    comp = random.randint(1,3) #random move for computer
    global precord
    global crecord
    print("welcome to rock paper scissors")
    while True:
        move = int(input("rock (1), paper (2), or scissors (3)? Enter 4 if you want to quit: ")) #player move
        if move == 4: #break function
            print("Thank you for playing")
            break
        elif comp == 1 and move == 2: #the following are various results of the game round
            print("The computer chose rock. you win")
            precord = precord +1 #tracking record of both player and computer
        elif comp == 1 and move == 1:
            print("the computer chose rock. you lose")
            crecord = crecord +1
        elif comp == 1 and move == 3:
            print("the computer chose rock. you lose")
            crecord = crecord +1
        elif comp == 2 and move == 1:
            print("the computer chose paper. you lose")
            crecord = crecord +1
        elif comp == 2 and move == 3:
            print("the computer chose paper. you win")
            precord = precord +1
        elif comp == 3 and move == 1:
            print("the computer chose scissors. you win")
            precord = precord +1
        elif comp == 3 and move == 2:
            print("the computer chose scissors. you lose")
            crecord = crecord +1
        elif comp == move:
            print("you chose the same thing. redo. it was a tie")
        print("your score is " + str(precord) + " and the computer's score is " + str(crecord)) #displays standings
#main
game()
