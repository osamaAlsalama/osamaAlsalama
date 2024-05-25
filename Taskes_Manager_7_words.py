import time
import sys
import random
WORDS = {
    "Absence": "The lack or unavailability of something or someone.",
    "Approval": "Having a positive opinion of something or someone.",
    "Answer": "The response or receipt to a phone call, question, or letter.",
    "Attention": "Noticing or recognizing something of interest.",
    "Amount": "A mass or a collection of something",
    "Borrow": "To take something with the intention of returning it after a period of time.",
    "Baffle": "An event or thing that is a mystery and confuses.",
    "Ban": "An act prohibited by social pressure or law.",
    "Banish": "Expel from the situation, often done officially.",
    "Banter": "Conversation that is teasing and playful.",
    "Characteristic": "referring to features that are typical to the person, place, or thing.",
    "Cars": "Four-wheeled vehicles used for traveling.",
    "Care": "extra responsibility and attention.",
    "Chip": "a small and thin piece of a larger item.",
    "Cease": "to eventually stop existing.",
    "Dialogue": "A conversation between two or more people.",
    "Decisive": "a person who can make decisions promptly.",
          }

def main():
    while True:
        print_options()
        try:
            user_choice =int(input('Enter your choice: '))
            if user_choice < 1 or user_choice > 3:
                raise
        except:
            print('invalid option')
            continue
        if user_choice == 1 :
            reviw_random_word(WORDS)
        elif user_choice == 2:
            test_yourself(WORDS)

        elif user_choice == 3:
            break
def print_options():
     the_massege = ''' 
1. Review random word
2. Test yourself
3. Exit
'''
     print(the_massege)
def reviw_random_word(word_dict):
        word = random.choice(list(word_dict.keys()))
        print(word)
        print(word_dict[word])
def test_yourself(word_list):
        word = random.choice(list(word_list.keys()))
        sys.stdout.write(word_list[word])
        sys.stdout.flush()
        time.sleep(5)
        sys.stdout.write('\r'+ ' '*len(word_list[word])+ '\r ')
        sys.stdout.flush()
        attempts = 3
        while attempts:
            test_word = input('Enter the word: ')
            if test_word.title() != word:
                if attempts != 1:
                    if attempts != 2:
                        print(f'wrong answer, you have {attempts - 1} attempts remaining')
                    else:
                        print(f'wrong answer, you have {attempts - 1} attempt remaining')
                else:
                    print('wrong, no more attempts remaining')
                    print(f'the word is {word}')
                attempts -= 1
            else:
                print('good answer')
                break

if __name__ == main():
    main()

