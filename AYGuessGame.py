# Here I am creating a guess game for purposes of practice. 

theme = 'animals'
secret_word = 'rabbit'

player_name = input('Hello, what is your name? ')
print("Hello, " + player_name + ", let's play a guess game!")
print()
print('The theme for this guess game is ' + theme + '!')

# A variable to store the guess word.
guess = ''

# A variable that stores the guess count
guess_count = 0

# A variable that stores the guess limit
guess_limit = 3

# A variable that lets me know he still has guesses
out_of_guesses = False

# print first hint
i = 0
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter your guess: ')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
        print("I didn't think it was that difficult... the word is " + secret_word + '!')
else: 
        print("Good job! That wasn't so hard right!")