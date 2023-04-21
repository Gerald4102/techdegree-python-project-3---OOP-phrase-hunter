class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self):
        display_list = []
        for letter in self.active_phrase_list:
            if letter == ' ':
                display_list.append(' ')
            elif letter in self.guesses:
                display_list.append(letter)
            else:
                display_list.append('_')
        display = ''.join(display_list)
        print(display, '\n')

    def check_letter(self, guess):
        if len(list(guess)) != 1 or guess == ' ':
            print(f'"{guess}" is not a valid guess')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print(f'{guess} is not a letter!')
        elif guess in self.guesses:
            print(f'You have already tried {guess} \n')
        elif guess in self.active_phrase.phrase:
            self.guesses.append(guess)
            print('Good guess! \n')
            Phrase.display(self)
        else:
            print(f'{guess} is not in the phrase \n')
            self.missed += 1
            print(f'You have {self.lives - self.missed} out of {self.lives} lives remaining! \n')
            self.guesses.append(guess)

    def check_complete(self):
        pass

