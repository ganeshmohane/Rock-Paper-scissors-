#Rock-Paper_Scissors Game in Python

#importing libraries
import random
import os
import re

#Taking Input from User
print("\n")
print("Rock, Paper & Scissors")
print("\n")
print("[R].Rock\n[P].Paper\n[S].Scissor\n[E].Exit")
userChoice=input("Enter your choice :")

#Checking input valid or invalid
if (not re.match("[SsRrPpEe]", userChoice)) or (len(userChoice) != 1):
    print ("Please choose a letter:")
    print ("[R]ock, [S]cissors, [P]aper or [E]xit")
    
#Showing User Choice if Valid 
if userChoice == 'R':
    print("Your Choice " + userChoice)
elif userChoice == 'P' :
    print("Your choice", userChoice)  
elif userChoice == 'S':
    print("Your choice", userChoice)  
elif userChoice == 'E':
    print("Exiting the Game...")
    quit()
#Generating random inputs from computer  
choices = ['R','P','S']
opponenetChoice = random.choice(choices)
print ("I chose: " + opponenetChoice)

#Games Rules
if opponenetChoice == userChoice:         
        print ("Tie! ")
elif opponenetChoice == 'R' and userChoice == 'S':            
        print ("Rock beats Scissors, I win! ") 
    
elif opponenetChoice == 'S' and userChoice == 'P':     
        print ("Scissors beats paper! I win! ")
        
elif opponenetChoice == 'P' and userChoice == 'R':          
        print ("Paper beat rock, I win! ")
        
else:                                                           
        print ("You win!")


