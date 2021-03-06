"""
===========
Description
===========

The popular video games Fallout 3 and Fallout: New Vegas has a computer hacking mini game
This game requires the player to correctly guess a password from a list of same length words. 
Your challenge is to implement this game yourself.
The game works like the classic game of Mastermind.
The player has only 4 guesses and on each incorrect guess,
the computer will indicate how many letter positions are correct.
For example, if the password is MIND and the player guesses MEND,
the game will indicate that 3 out of 4 positions are correct (M_ND). 
If the password is COMPUTE and the player guesses PLAYFUL, the game will report 0/7. 
While some of the letters match, they're in the wrong position.
Ask the player for a difficulty (very easy, easy, average, hard, very hard), 
then present the player with 5 to 15 words of the same length. The length can be 4 to 15 letters. 
More words and letters make for a harder puzzle. 
The player then has 4 guesses, and on each incorrect guess indicate the number of correct positions.

Here's an example game:

Difficulty (1-5)? 3
SCORPION
FLOGGING
CROPPERS
MIGRAINE
FOOTNOTE
REFINERY
VAULTING
VICARAGE
PROTRACT
DESCENTS
Guess (4 left)? migraine
0/8 correct
Guess (3 left)? protract
2/8 correct
Guess (2 left)? croppers
8/8 correct
You win!

========
Solution
========
"""
import random

difficulties = {1:4,
		2:5,
		3:7,
		4:10,
		5:15}

def wordlist(difficulty):
	wordlist = open('enable1')
	words = [word.strip() for word in wordlist if len(word) == difficulties[difficulty]+1]
	wordlist.close()
	return words

def get_words(word_amount,difficulty):
	words = []
	for i in range(word_amount):
		word = random.choice(wordlist(difficulty))
		words.append(word)
	return words

def print_words(words):
	print('----------')
	for word in words:
		print (word)
	print('----------')

def check_word(word,answer):
	correct_letter_count = 0
	for i in range(len(word)):
		if word[i] == answer[i]:
			correct_letter_count+=1
	return correct_letter_count

def main_loop(num_of_guesses,amount_of_words,difficulty):

	guesses = num_of_guesses

	words = get_words(amount_of_words,difficulty)
	answer = random.choice(words)

	while guesses:
		print_words(words)
		word = input('Take a guess: ')
		print()
		if check_word(word,answer) == len(answer):
			print('YOU WON')
			break
		print(check_word(word,answer),'were in the correct position')
		guesses-=1
	print('The answer was',answer)
	input('Press enter to exit')


main_loop(10,10,4)
