#My word guesser game in Pythpon
import random

#creating our word list
wordlist = ['apple', 'banana', 'cat', 'dog', 'Fire hydrant', 'snake', 'woman', 'man', 'freak']

#create our randomizer
word_to_guess = random.choice(wordlist)

#start main game code blocks
print("Welcome to the word guesser game!")
print("I am thinking of a word. Can you guess it?")

guess_counter = 0
max_guesses = 8
turns = 15
fail_counter = 0
fail_guesses = []

while turns > 0:
    player_guess = input("Enter your guess: ").lower()
    guess_counter += 1
    if player_guess == word_to_guess:
        print("You won")
        break
    else:
        print("you are wrong")
        fail_counter += 1
        fail_guesses.append(player_guess)
        guesses_left = max_guesses - guess_counter
        print(f'{guesses_left} guesses left')

        