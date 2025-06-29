#greetings and rules print statements
#tell player to choose difficulty, and guess
#check greater then, less than, equal to and change the attempted guesses mark as the player guesses
#multiple rounds
#clock
import random 
import time

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

#socre trackers
easy_score = None 
mid_score = None
hard_score = None


def easy(target):
    attempts = 0
    max_attempts = 10
    start = time.time() #timer 
    global easy_score  
    while attempts < max_attempts:

        guess = int(input("Enter your guess: "))
        attempts += 1 

        #checking the relations between the guess nad target number
        if guess < target : 
            print("Incorrect! The number is greater than ",guess)
        elif guess == target :
            print("Congratulations! You guessed the correct number in",attempts,"attempts.")
            #updating the score trakcer
            if easy_score is None or easy_score > attempts:
                easy_score = attempts
            print(f"The new high score is for easy level is {easy_score}")
            break
        else :
            print("Incorrect! The number is less than ",guess)
        
      
       

        #hint for the player
        if max_attempts - attempts == 3:
            low = max(1,target-5)
            high = min(target +5, 100)
            print(f"The target is between numbers {low} and {high}") 
    #timer ends and the total time taken
    end = time.time() 
    duration = end - start 
    print(f"The round completed in {duration:.2f} seconds" )
    
    if attempts == max_attempts and guess != target:
        print("You couldn't guess the number in specified amount of attempts given. ")
 


def mid(target):
    attempts = 0
    max_attempts = 5
    start = time.time() #timer starts
    global mid_score 
    while attempts < max_attempts:

        guess = int(input("Enter your guess: "))
        attempts += 1 

        #checking the relations between the guess nad target number
        if guess < target : 
            print("Incorrect! The number is greater than ",guess)
        elif guess == target :
            print("Congratulations! You guessed the correct number in",attempts,"attempts.")

            #timer ends adn total time taken
            end = time.time()
            duration = end - start
            print(f"You guessed the correct number in {duration:.2f} seconds" )

            #updating the score tracker
            if mid_score is None or attempts < mid_score:
                mid_score = attempts
            print(f"The new high score is for medium level is {mid_score}")
            break
        else :
            print("Incorrect! The number is less than ",guess)

        #hinting the player 
        if max_attempts - attempts == 2:
            low = max(1,target-5)
            high = min(target +5, 100)
            print(f"The target is between numbers {low} and {high}")     

    #timer ends and the total time taken
    end = time.time() 
    duration = end - start 
    print(f"The round completed in {duration:.2f} seconds" )  

    if attempts == max_attempts and guess != target:
        print("You couldn't guess the number in specified amount of attempts given. ")


def hard(target):
    attempts = 0
    max_attempts = 3
    start = time.time() # timer starts
    global hard_socre 
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1 

        #checking the relations between the guess nad target number
        if guess < target : 
            print("Incorrect! The number is greater than ",guess)
        elif guess == target :
            print("Congratulations! You guessed the correct number in",attempts,"attempts.")

            #timer ends and total time taken
            end = time.time()
            duration = end - start
            print(f"You guessed the correct number in {duration:.2f} seconds" )

            #updating the score tracker
            if hard_score is None or hard_score > attempts:
                hard_score = attempts
            print(f"The new high score for the hard level is {hard_score}. ")
            break
        else :
            print("Incorrect! The number is less than ",guess)

        #hinting the player 
        if max_attempts - attempts == 1:
            low = max(1,target-5)
            high = min(target +5, 100)
            print(f"The target is between numbers {low} and {high}") 

    #timer ends and the total time taken
    end = time.time() 
    duration = end - start 
    print(f"The round completed in {duration:.2f} seconds" )  

    if attempts == max_attempts and guess != target:
        print("You couldn't guess the number in specified amount of attempts given. ")

#for multiple levels until the player says no
again = "y"
while again == "y" :
    print("Please select the difficulty levels:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    choice = int(input("Enter your choice: "))
    print("Great! You have selected difficulty level ", choice)
    print("Let's start the game!")

    #choosing random integer form 1to 100
    target = random.randint(1,100)

    #calling level function according to the choice
    if choice == 1:
        easy(target)
    elif choice == 2:
        mid(target)
    elif choice == 3:
        hard(target)
    else:
        print("Enter valid choice number : 1, 2, 3.")
    
    #player choose to play again or not
    again = input("Would you like to play again? (y/n)")

# The end
print("Thankyou for playing. ")

    
