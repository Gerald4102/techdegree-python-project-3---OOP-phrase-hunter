import random

from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.lives = 5
        self.phrases = [
            Phrase("Frankly my dear I dont give a damn"), 
            Phrase("Im going to make him an offer he cant refuse"), 
            Phrase("Toto Ive got a feeling we are not in Kansas anymore"), 
            Phrase("Go ahead make my day"), 
            Phrase("May the Force be with you")
            ]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.active_phrase = self.get_random_phrase()
        self.active_phrase_list = list(self.active_phrase.phrase)
        self.welcome()
        Phrase.display(self)
        while True:
            guess = self.get_guess()
            Phrase.check_letter(self,guess)
            self.game_over()

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print('\n')
        print('Welcome to PHRASE HUNTER \n')

    def get_guess(self):
        return input('Guess a letter: ').lower()

    def game_over(self):
        phrase = set(self.active_phrase.phrase) - set(' ')
        guesses = set(self.guesses)
        if phrase.issubset(guesses):
            print('You won! \n')
            self.restart()
        elif self.missed == self.lives:
            print('GAME OVER')
            self.restart()

    def restart(self):
        restart = input('Would you like to play again? Y/N \n').lower()
        if restart == 'y':
            Game().start()
        elif restart == 'n':
            print('Thank you for playing. \n')
            exit()
        else:
            self.restart()


if __name__ == "__main__":
    game = Game()
    game.start()
