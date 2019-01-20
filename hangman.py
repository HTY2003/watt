import random
from sys import argv
from time import sleep
import whatsapp_api as wa

assert(len(argv) == 2)

DICT_PATH = '/usr/share/dict/cracklib-small'

wa.setup()
wa.sel_chat(argv[1])

def random_word():
    with open(DICT_PATH, 'r') as f:
        lines = f.readlines()
        while True:
            word = random.choice(lines).strip('\n')
            if word.isalnum():
                break
        return word

def occurences(c, s):
    idxs = []
    for idx, i in enumerate(s):
        if i == c:
            idxs.append(idx)
    return idxs

def hangman():
    tries = 0
    word = random_word()
    print(f'word: {word}')

    guess = ['_'] * len(word)
    wa.send_msg('welcome to hangman! message "quit" to quit.')

    while True:
        sleep(1)
        tries += 1
        wa.send_msg('current guess: {}'.format(' '.join(guess)))

        s = wa.wait_for_msg()
        s = s.lower()

        if s == 'quit':
            wa.send_msg(f'too bad! the word was {word}')
            break

        if len(s) != 1:
            wa.send_msg(f'send just ONE character!')
            continue

        if len(s) == len(word):
            if s == word:
                wa.send_msg(f'you guessed it correctly! the word was {word}')
                wa.send_msg(f'total tries: {tries}')
                break
            else:
                wa.send_msg(f'your guess was incorrect! try again!')
                continue

        idxs = occurences(s, word)
        for i in idxs:
            guess[i] = s

        if len(idxs) == 0:
            wa.send_msg(f'{s} is not found in the word, try again!')
        else:
            wa.send_msg(f'{s} occurs in the word {len(idxs)} times')
            if ''.join(guess) == word:
                wa.send_msg(f'you guessed it correctly! the word was {word}')
                wa.send_msg(f'total tries: {tries}')
                break

while True:
    s = wa.wait_for_msg()
    if s.lower() == 'hangman':
        hangman()
