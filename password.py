def getStrongPassword():
  return ask_for_password()

def contains_upper(password):
  for char in password:
      if char.isupper():
          return True
  return False

def contains_lower(password):
  for char in password:
      if char.islower():
          return True
  return False

def contains_digit(password):
  for char in password:
      if char.isdigit():
          return True
  return False

def is_password_strong(password):
    if len(password) > 8 and contains_upper(password) and contains_lower(password) and contains_digit(password):
       return True
    else:
       return False
    
def ask_for_password():
  while True:
    password = input(
"""
Input your password:
1.the password has at least one upper case letter 
2.the password has at least one lower case letter 
3.the password has at least one digit
4.its length is more than 8
"""
    )
    if is_password_strong(password):
      print("Your password is strong enough. User registered.")
      return password
    else:
      print("Your password is weak. Please enter a new password ")