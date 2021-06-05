name= "Number Guessing Game"
print(name)
guess= "Guess a number between 1 and 9"
print(guess)
number = int(input("Enter your guess:-"))
if(number==1):
    print("Your guess was too low: Guess a number higher than 1")
if(number==2):
    print("Your guess was too low: Guess a number higher than 2")
if(number==3):
    print("Your guess was too low: Guess a number higher than 3") 
if(number==4):
    print("Your guess was too low: Guess a number higher than 4")       
if(number==5):
    print("Your guess was too low: Guess a number higher than 5")
if(number==6):
    print("Your guess was too low: Guess a number higher than 6") 
if(number==7):
    print("Your guess was too low: Guess a number higher than 7") 
elif(number>7):
    print("Congratulation YOU WON!")    
