n = 5

# takes input of number from the user
userInput = int(input('Enter a number from 1 - 9: '))

# loops the choice until the guess is correct
while userInput != n:
    # if the user inputs a number greater than n
    if userInput > n:
        print('Guess number lower than ', userInput)
        # after statement, it takes back to the choice
        userInput = int(input('Enter a number from 1 - 9: '))
    # if the user inputs a number lower than n
    elif userInput < n:
        print('Guess number greater than ', userInput)
        # after statement, it takes back to the choice
        userInput = int(input('Enter a number from 1 - 9: '))

# checks if the guess is correct and prints congrats statement
if userInput == n:
    print('Yay, you guessed it correct!!🎉')