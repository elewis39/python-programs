#Ella Lewis
#name generator
#init

#functions
def whichartistgame():

    print("Welcome to the Which artist are you Quiz") #welcome
    print("Answer the Questions to Find Out What artist you are")
    ans = input("single (s) or band (b) ?") #various input questions to match user with their artist
    if ans =="s": 
        ans = input("Female)(f) or male (m)?")
        if ans == "f":
            ans = input("pop (p) or country (c)?")
            if ans == "p":
                print("You are the artist Ariana Grande")
            else:
                print("You are the artist Dolly Parton")
        elif ans == "m":
            ans = input("pop (p) or country (c) ?")
            if ans == "p":
                print("You are the artist Bruno Mars")
            else:
                print("You are the artist Zac Bryan")
    elif ans =="b":
        ans = input("mixed-gender group (mg) or one-gender group (og)?")
        if ans == "mg":
            ans = input("pop (p) or alternative/indie (a/i)?")
            if ans == "p":
                print("You are the Black-Eyed Peas")
            else:
                print("You are The Lumineers")
        elif ans == "og":
            ans = input("pop (p) or alternative/indie (a/i)?")
            if ans == "p":
                print("You are The Beach Boys")
            else:
                print("You are the Arctic Monkeys")

#Main
whichartistgame()
