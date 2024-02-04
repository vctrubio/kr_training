import sys

red_cc = "\033[91m"
blue_cc = "\033[94m"
green_cc = "\033[92m"
reset_cc = "\033[0m"
orange_cc = "\033[38;5;208m"

'''
Hangman with a twist, the user can input the word directly. 
Count will go up for every letter that is missed, 'hello' with = 'helo'
if h,e,l,o is not present in word, we loose 4 counts
'''

def join_lst(lst):
    return ' '.join(lst)

def print_menu():
    print(f'{orange_cc}{6 - count}{reset_cc} tries left   :')
    print(f'Used letters   : {join_lst(lst)}')

def print_word():
    sys.stdout.write('HANGMAN        | ')
    for i in word:
        if i in lst:
            sys.stdout.write(i)
        else:
            sys.stdout.write('_')
        sys.stdout.write(' ')
    print()


if len(sys.argv) > 1:
    word = sys.argv[1]
else:
    word = 'helloworld'

lst = set()
count = 0


while count < 6:
    print_menu()
    print_word()
    ui = input('Guess a letter : ')
    
    if len(ui) == 0:
        continue

    single_letters = set(ui)
    print(f"You've guessed the letters: {join_lst(single_letters)}")
    print_word()
    for i in single_letters:
        if i not in lst:
            lst.add(i)
        else:
            print(f'{red_cc}SillyBilly.{reset_cc} You just wasted 1 count on {i}')
            count +=1
        if i not in word:
            count +=1
    if set(word) == lst:
        print(f'{green_cc}{word}{reset_cc} | Congrats, it only took you {count} go\'s')
        exit(1) 
    print()


print(f'Game is OVER. Good try, better luck next time.')
print(f'Did you know, you could set your own HANGMAN by running: {blue_cc} python3 hangman.py JoeyThepythononicHanger {reset_cc}')


