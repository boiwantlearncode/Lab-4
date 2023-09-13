from random import randint

def guessingNumber():
  randomNumber = randint(1, 9)
  guessesMade = 0

  while True:
    if guessesMade == 3:
      print("Sorry, you exceed the trial limit. Failed.")
      break

    guess = int(input("Enter an integer from 1 to 9: "))
    if guess < randomNumber:
      print("guess is low")
    elif guess > randomNumber:
      print("guess is high")
    else:
      print(f"Congratulations. You guessed it by {guessesMade} trials!")
      print("You can start the game now.")
      break
    guessesMade += 1

def calculateSum():
  randomNumber = randint(55, 66)
  # randomNumber = 65
  print(f"Please calculate the sum of 5 integers start from {randomNumber}")
  answer = int(input("Please enter you answer: "))
  total = sum([x for x in range(randomNumber, randomNumber + 5)])
  if answer == total:
    print("You can start the game now.")
  else:
    print("Sorry, wrong answer. Failed.")