print("Hello and welcome to the zoo!")
print("I hope you're excited to hear about all of the wonderful things that are happening here")
startGame = input("Would you like to enter the zoo?")

if((startGame.lower() == "yes") or (startGame.lower() == "y")):
  print("Wonderful, welcome to your beautiful facility")
  while(startGame.lower() == "yes" or (startGame.lower == "y")):
      print("Welcome to the main entrance")
      firstTurn = input("Would you like to go left or right?")
      if(firstTurn.lower() == "left"):
          #time to go left
          print("Alright, we can definitely go left")
          print("Oh hey look, there are elephants over there and giraffes over there")
          secondTurn = input("Which would you like to see?")
          while(secondTurn.lower() != "elephants" and secondTurn.lower() !="giraffes"):
              secondTurn = input("Oh, I'm sorry, what did you say?")
          if(secondTurn.lower() == "elephants"):
              print("To the elephants we go!")
          elif(secondTurn.lower() == "giraffes"):
              print("March straight to the giraffes!")
          print("Cool! Let's go back to the entrance")
      elif(firstTurn.lower() == "right"):
          #time to go right
          print("Go right")
      else:
          while(firstTurn.lower() != "left" and firstTurn.lower() != "right"):
              print("Oops, that didn't quite make sense to me, could you repeat it?")
              firstTurn = input("Would you like to go left or right?")
else:
  print("Well that's alright, hope to see you again sometime soon!")
