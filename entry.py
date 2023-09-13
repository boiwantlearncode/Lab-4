from storage import db_usernames

def userRegistration(username, password):
  db_usernames[username] = password
  # print(db_usernames)
  print("New User registered. You can start the game.")

def userLogin():
  while True:
    username = input("Input user name: ")
    password = input("Input password: ")
    if username in db_usernames and db_usernames[username] == password:
      print(f"Welcome back, {username}. You can start the game.")
      return
    else:
      print("Invalid username and password.")