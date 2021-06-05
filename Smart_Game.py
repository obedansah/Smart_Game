
#Welcoming the Users
name = input("Enter your name")

print("Hello " +name,"Let's Play SmartGame")

print("So what's your first guess")

#Guess word
word = "Entertainment"

#creates an variable with an empty value
guesses = " "

#determine the number of runs
runs = 15

while runs>0:   # Create a while loop and check if the number of turns are greater than zero

    failed = 0    # make a counter that starts with zero

    for Char in word:     # for every character in secret_word

        if Char in guesses:  # Print if the character is in the players / users guess
            print(Char)

        # if not found, print a dash
        else:
            print("*")
            failed += 1
#if failed == 0 print you won
        if failed == 0:
            print("You won")

            break

    print()

    # ask the user to  guess a character
    guess = input("Guess a Character:")
    guesses += guess


  # if guess is not found in the secret word
    if guess not in word:

#number of runs is reduced by 1
        runs -= 1

#
        print("Wrong guess")

# The number of runs left
        print("You have", +runs, "more guesses")


#if the number of runs is 0 print hurray you won
    if runs == 0:
        print("Hurray!!!! you lose")


