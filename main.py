Valiity import re
while True:
  input_password = input("Enter a password : ")
  valid_password = False
  if (len(input_password)<8):
    print("Not valid ! Total characters should atleast be 8")
    continue
  elif not re.search("[A-Z]",input_password):
    print("Not valid ! Password should contain one letter between [A-Z]")
    continue
  elif not re.search("[a-z]",input_password):
    print("Not valid ! Password should contain one letter between [a-z]")
    continue
  elif not re.search("[1-9]",input_password):
    print("Not valid ! Password should contain one letter between [1-9]")
    continue
  elif not re.search("[~!@#$%^&*]",input_password):
    print("Not valid ! Password should contain at least one letter in [~!@#$%^&*]")
    continue
  elif re.search("[\s]",input_password):
    print("Not valid ! Password should not contain any space")
    continue
  else:
    valid_password = True
    break
if(valid_password==True):
  print("Password is valid")