from random import randint
#the introduction to what chatbot is

##
##
#Reading the information in the jokes file
jokestxt = open('jokes.txt', 'r')
jokes1 = []
jokes2 = []

for line in jokestxt:
    jokes1.append((line.split(","))[0])
    jokes2.append((line.split(","))[1])

##
##
#Reading the info in the knock jokes file
knockjokestxt = open('knockjokes.txt', 'r')
kjokes1 = []
kjokes2 = []
for line in knockjokestxt:
    kjokes1.append(line.split(",")[0])
    kjokes2.append(line.split(",")[1])
#
#

def intro():
    print("This is Chatbot. You are now speaking with a robot.")

#the chatbot introducing self and asking user name
def introduction():
    print("Hey there! My name is Chatty, what's your name?")
    userName = input("")
    print("Well its really nice to meet you %s" %(userName))
    print("Since I am a robot, there are a number of things that I am able to do.")
    print("I figure since you are talking with me you want to do some of them...")
    return userName

#where chatbot talks about the different things they can do
def genMenu():
    print("So what would you like to do?")
    print("I can tell a joke, tell a knock knock joke, play hangman, play an adventure game, and play rock, paper, scissors.")
    userChoice = input("")
    if(("joke" in userChoice.lower()) and (not ("knock" in userChoice.lower()))):
        #print("j") #j means the robot will tell a joke
        #call tell joke
        joke()
    elif(("joke" in userChoice.lower()) and ("knock" in userChoice.lower())):
        #print("k") #k means the robot will tell a knock knock joke
        knockJoke()
        #call knock joke
    elif(("rock" in userChoice.lower()) or ("scissors" in userChoice.lower()) or ("paper" in userChoice.lower())):
        #print("rps") #rps means the robot will play rock paper scissors
        #call rock paper scissors
        rps()
    elif("hangman" in userChoice.lower()):
        import Hangman
        #Hangman
    elif("adventure" in userChoice.lower()):
        import BuildYourOwnAdventure
    else:
        print("I'm sorry, I don't know what that means, let's try again!")
        genMenu()

def joke():
    jokeNum = randint(0, len(jokes1) - 1)
    print(jokes1[jokeNum])
    input("")
    print(jokes2[jokeNum])

def knockJoke():
    #jokeName = ["orange", "Who"]
    #jokePunch = ["Orange you glad I didn't say apple?", "Are you an owl?"]
    jokeNum = randint(0, len(kjokes1) - 1)
    print("Knock Knock...")
    input("")
    print(kjokes1[jokeNum])
    input("")
    print(kjokes2[jokeNum])

def rps():
    #print("Current Score:")
    #print("Computer: %d      Player: %d" %(  ))
    needInput = True
    inp = ""
    while(needInput):
        inp = input("Please enter rock, paper, or scissors: ")
        if("rock" in inp.lower()):
            inp = "r"
            needInput = False
        elif("p" in inp.lower()):
            inp = "p"
            needInput = False
        elif("s" in inp.lower()):
            inp = "s"
            needInput = False
        else:
            print("Thats an invalid input.")

    compChoice = randint(0, 2) # 1 is rock, 2 is paper, 3 is scissors
    if((compChoice == 1 and inp == "r") or (compChoice == 2 and inp == "p") or (compChoice == 3 and inp == "s")):
        print("Oops, you tied!")
        rps()
    elif((compChoice == 1 and inp == "p") or (compChoice == 2 and inp == "s") or (compChoice == 3 and inp == "r")):
        print("You've won!")
    else:
        print("You lost...")

intro()
userName = introduction()
playGame = True
while(playGame):
    genMenu(  )
    contin = input("Would you like to talk more?")
    if("n" in contin.lower()):
        playGame = False
