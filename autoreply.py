from sys import argv
from time import sleep
import whatsapp_api as wa

cs = None
wa.setup()

while True:
    cs = wa.unread_chats()
    for c in cs:
        c.click()
        if len(argv) < 2:
            wa.send_msg(f'The message you have just sent is "{wa.get_last_msg()}".')
        else:
            wa.send_msg(argv[1])
        sleep(3)
