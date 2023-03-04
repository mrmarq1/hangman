import random

word_list = ['apples','pears','kiwis','pomegranates','strawberries']
word = random.choice(word_list)
print(word)

def ask_for_input():
  while True:
    guess = input('Please enter a single letter: ')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
  
  check_guess(guess)

def check_guess(guess):
  guess_lower = guess.lower()
  if guess_lower in word:
    print(f'Good guess! {guess_lower} is in the word.')
  else:
    print(f'Sorry, {guess_lower} is not in the word. Try again')

ask_for_input()
   