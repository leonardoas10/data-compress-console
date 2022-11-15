import os

class Helper:
    @staticmethod
    def yes_or_not_answer(word: str, answer):
        init_yes_or_not_answer = True
        print('\nIs correct the option {}? = {}'.format(word, answer))
        option = input('\nYes (y) or Not (n): ').lower()
        while init_yes_or_not_answer:
            if option == 'y':
                init_yes_or_not_answer = False
                return answer
            elif option == 'n':
                answer = input('\nEnter your {} again: '.format(word)).lower()
                print('\nIs correct the option {}? = {}'.format(word, answer))
                option = input('\nYes (y) or Not (n): ').lower()
            else:
                print("\nEnter a valid option: y or n")