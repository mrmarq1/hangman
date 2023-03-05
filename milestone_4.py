import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)     
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
            guess = guess.lower()
            if guess in self.word:
                print(f'Good guess! {guess} is in the word.')
                for letter in self.word:
                    if letter == guess:
                       letter_idx = self.word.index(letter)
                       self.word_guessed[letter_idx] = letter                    
                self.num_letters -= 1

    def ask_for_input(self):
         while True:
          self.guess = input('Please enter a single letter: ')
          if len(self.guess) != 1 or not self.guess.isalpha():
            print('Invalid letter. Please, enter a single alphabetical character.')
          elif self.guess in self.list_of_guesses:
            print('You already tried that letter!')
          else:
            self.list_of_guesses.append(self.guess)
            self.check_guess(self.guess)
            break

hangman = Hangman(['apples', 'pears', 'pomegranates', 'kiwis'])
hangman.ask_for_input()