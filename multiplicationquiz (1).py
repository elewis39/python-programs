#Ella Lewis
#1/8/25
#Multiplication Quiz

#init
import random
import time
score = 0
#functions
def quiz(name): #quiz function
    global score
    print("Welcome to the multiplication quiz " + name)
    start_time= time.time()
    while True:
        questions = int(input("How many questions would you like?: ")) #the number of quiz questions
        for i in range(questions): #the function will repeat "question" amount of times
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            real_ans = num1 * num2 #the answer to the problem
            print("please solve the problem: " + str(num1) + "*" + str(num2))
            answer = int(input("please enter your answer: ")) #answer input
            if answer == num1*num2: #correct answer
                print("Correct! The answer was " + str(real_ans) + "!")
                score = score + 1
                print("You now have " + str(score) + (" points. Keep it up!"))
            else: #wrong answer
                print("That is incorrect. The answer was " + str(real_ans))
                print("Your score is " + str(score))
        quit = input("Would you like to quit?")
        if quit == "yes":
            end_time= time.time()
            elapsed_time = end_time - start_time
            print("your final score was " + str(score))
            print("your elapsed time was " + str(elapsed_time) + " seconds")
            print("Thank you for playing")
            break
#main
quiz("claudia")
