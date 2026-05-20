import random

def guess_game():
    
    print('Start your game!')
    
    # guess the secret number
    random_num = random.randint(1, 100)
    
    score = 0
    
    print('Welcome to the number guessing game!')
    print('I am thinking of the number between 1 and 100')
    
    while True:
        try:
        # guess the number
         guess = (int)(input("Guess the number : "))
         score += 1
        
         if guess < random_num :
            print('Too Low! Please enter the higher number.')
         elif guess > random_num :
            print('Too High! Please enter the low number.')
         else:
            print('Congrats! Your score %d'%(score))
            break
        except ValueError:
            print('Invalid! Please try again.')

guess_game()