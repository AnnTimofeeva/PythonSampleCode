import random    
# Number guessing game
# --------------------

# Implement the following game in python:

# 1. Randomly select a number between 1 and 20 | 50 | 100

#     import random                   <-- needs to go at the top of your python file

#     print random.randint(1,101)     <-- prints random number between 1 and 100

# 2. Ask the user to make a guess
#     Look at the input() function - e.g:
#         guess = input("Make a guess: ")

# 3. If correct report total number of guesses

# 4. Otherwise, report higher or lower than target number.

# Testing?
#     What kind of tests, if any, do you feel would be necessary/appropriate 
#     for your code?
randomnumber =  (random.randint(1,101))

chance = 0
status="play"

while (status!="quit"):
        guess = input("Make a guess or type Q to quit: ")
        if (guess=="Q"):
                print(f"Game over! The number was {randomnumber}  number of guesses is {chance}")
                status="quit"
                break
        if(randomnumber==int(guess)):
                
                print(f"You win! The number was {randomnumber}  number of guesses is {chance}")
                status="quit"
                break
        else:
                chance+=1
                if (int(randomnumber)<int(guess)):
                        print("Random number is lower than "+guess)
                else:
                        print("Random number is higher than "+guess)