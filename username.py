from storage import db_usernames

def getNewUserName():
  return ask_for_username()

def ask_for_username():
  while True:
    username = input("Input your user name: ")
    if username in db_usernames:
      print("The user exists. Please choose another user name.")
    else:
      return username

