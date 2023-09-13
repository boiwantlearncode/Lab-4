from choices import guessingNumber, calculateSum
from password import getStrongPassword
from username import getNewUserName
from entry import userRegistration, userLogin

def getUserChoice():
  choice = int(input('''Please select one of the following
options:
  return choice
1. User registration
2. User Login
3. Play the game as a guest\n'''))
  return choice
  
def guestQuiz():
  quizChoice = chooseQuiz()
  isPass = takeQuiz(quizChoice)
  if isPass:
    print("Congratulations. You can start the game.")

def chooseQuiz():
  choice = int(input('''Dear Guest, you have to pass one quiz to play the game.
  Please select one of the following quizzes:
      1. Number guessing
      2. Calculate sum\n'''))
  return choice
def takeQuiz(choice):
  if choice == 1:
    isPass = guessingNumber()
  elif choice == 2:
    isPass = calculateSum()
  return isPass
def main():
  choice = getUserChoice()
  if choice == 1:
    userRegistration(getNewUserName(),getStrongPassword()) 
  elif choice == 2:
    userLogin()
  elif choice == 3:
    guestQuiz()

main()