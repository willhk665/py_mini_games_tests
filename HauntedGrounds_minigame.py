print('''
          <|
           A             
          /.\       
     <|  [""M#      
      A   | #              
     /.\ [""M#             
    [""M# | #  U"U#U                 
     | #  | #  \ .:/    
     | #  | #___| #     
     | "--'     .-"     
   |"-"-"-"-"-#-#-##    
   |     # ## ######     
    \       .::::'/     
     \      ::::'/      
   :8a|    # # ##      
   ::88a      ###       
  ::::888a  8a ##::.    
  ::::::888a88a[]::::
 :::::::::SUNDOGa8a::::. ...              
 :::::8::::888:Y8888:::::::::...      
::':::88::::888::Y88a______________________________________________________
:: ::::88a::::88a:Y88a                                  __---__-- __
' .: ::Y88a:::::8a:Y88a                            __----_-- -------_-__
  :' ::::8P::::::::::88aa.                   _ _- --  --_ --- __  --- __--
.::  :::::::::::::::::::Y88as88a...s88aa.

''')
print("Welcome to Haunted Castle Grounds.")
print("Your mission is to get into the castle.... Alive!\n") 


print("You are at the foot of the hill, to get up to the castle choose to go left or right?")
hill = input("Type left or right?\n").lower()
if hill == "left":
  print("huh... You dodged it! To get to the hanging bridge, you need to get across the lake. Do you want to swim or wait for the boat?")
  lake = input("Type swim or wait?\n").lower()
  if lake == "wait":
    print("You've got to the castle, there are three doors. Which one will you choose?")
    door = input("Type blue, red or yellow?\n").lower()  
    if (door == "red") or (door == "blue"):
      if door == "red":
        print("That door is locked! What is the lock combination? ")
        combination = int(input("2 or more digits...\n"))
        if combination >= 45:
          print("You are safe! You win!")
        else:
          print("**WRONG** Game Over! The ghost got you!")
      if door == "blue":
       print("Ghost attack! Game over!")
    elif door == "yellow":
      print("You win!")
  elif lake == "swim":
    print("Attacked by an Alligator, game over!")  
else:
  print("Game over!")