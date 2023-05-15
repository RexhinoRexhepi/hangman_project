import random

class Hangman:
    def __init__(self, number_of_lives):
        self.lives = number_of_lives
        self.word_list = []
        self.letters_chosen = []
        self.empty_list = []
        self.index = '_'
        self.number_of_letters = len(set(self.word_list))

    def input_letter(self):
        while True:
            player_choice = input('Please choose a letter:').lower()
            if len(player_choice) > 1:
                print('Please input only one letter.')
            elif not player_choice.isalpha():
                print('Please input only letters from A to Z.')
            elif player_choice in self.letters_chosen:
                print('You have already tried this letter.')
            elif len(player_choice) == 1:
                break
        return player_choice

    def choose_random_word(self):
        with open("words.txt", "r") as file:
            word = random.choice(file.read().splitlines())
        return word

    def convert_random_word(self):
        random_word = self.choose_random_word()
        length_of_word = len(random_word)
        self.word_list = ["_"] * length_of_word
        print(self.word_list)
        print('Start Game!')
        print(f'The word has {len(self.word_list)} characters')
        return "".join(self.word_list), random_word

    def check_letter(self):
        random_word = self.convert_random_word()[1]
        while self.lives > 0:
            stored_player_input = self.input_letter()
            print(stored_player_input)
            if stored_player_input in random_word:
                print('Correct letter')
                self.letters_chosen.append(stored_player_input)
                indices = [index for index, value in enumerate(random_word) if value == stored_player_input]
                for index in indices:
                    self.word_list[index] = stored_player_input
                    self.number_of_letters -= 1
                print(f'Correct Letters = {abs(self.number_of_letters)}')
                print(self.word_list)
            else:
                print('Incorrect letter')
                self.letters_chosen.append(stored_player_input)
                self.lives -= 1
                print(f'You have {self.lives} lives remaining')
                print(self.word_list)
                print(self.letters_chosen)

            if abs(self.number_of_letters) == len(self.word_list):
                print("You Win!")
                break

            if self.lives == 0:
                print('YOU LOSE!!!')
                print(f'The word was: {random_word}')
                break

    def play_again(self):
        while True:
            choice = input("Do you want to play again? (yes/no): ").lower()
            if choice == "yes":
                self.__init__(5)
                self.play_game()
            elif choice == "no":
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    def play_game(self):
        self.choose_random_word()
        self.check_letter()
        self.play_again()

if __name__ == "__main__":
    new_game = Hangman(5)
    new_game.play_game()