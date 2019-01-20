from random import randint
from sys import argv
from time import sleep
import whatsapp_api as wa

assert(len(argv) == 2)

wa.setup()
wa.sel_chat(argv[-1])

def guess_game():
    tries = 0
    n = randint(0, 300)

    print(f'n: {n}')
    wa.send_msg('welcome to the guessing game! you can guess any number or message "q" to quit.')

    while True:
        sleep(1)
        tries += 1
        s = wa.wait_for_msg()
        if s == 'q':
            wa.send_msg(f'too bad! the number was {n}')
            break

        try:
            i = int(s)
        except ValueError:
            wa.send_msg('that was NOT an integer! try again!')
        else:
            if i == n:
                wa.send_msg('that was correct! congrats!')
                wa.send_msg(f'total tries: {tries}')
                break
            elif i < n:
                wa.send_msg('you guessed a bit too low... try again!')
            elif i > n:
                wa.send_msg('you guessed a bit too high... try again!')

while True:
    s = wa.wait_for_msg()
    if s.lower() == 'guess':
        guess_game()
