import random

word_list = ['apples','pears','kiwis','pomegranates','strawberries']
word = random.choice(word_list)
print(word)

while True:
  guess = input('Please enter a single letter: ')
  if len(guess) == 1 and guess.isalpha():
      break
  else:
      print('Invalid letter. Please, enter a single alphabetical character.')
    