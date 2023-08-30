# Hangman
guess = input('Guess a letter in A _P_E_')
guess = guess.upper()
gletters = ''  # to declare variable with all correct letters guessed
if guess in 'PLS':
    print('Yes,', guess, 'is in the word! Two more letters to guess.')
else:
    print(guess, 'is not in the word. You have two tries left')
    guess = input('Guess a letter in A _P_E_')
guess = guess.upper()
if guess in 'PLS':
    if guess not in gletters:
        print('Yes,', guess, 'is in the word! One more letter to guess.')
        gletters = gletters + guess
    else:
        print('You already guessed this letter. One guess left')
else:
    print(guess, 'is not in the word. You have one try left')

guess = input('Guess a letter in A _P_E_')
guess = guess.upper()
if guess in 'PLS':
    if guess not in gletters:
        print('Yes,', guess, 'is in the word!')
        gletters = gletters + guess
    else:
        print('You already guessed this letter.')
else:
    print(guess, 'is not in the word. You have no guesses left')

print('The word was APPLES!')
