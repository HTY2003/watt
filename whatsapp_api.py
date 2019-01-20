from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep

d = None
last_msg = ''
last_unread = []

def setup():
    global d
    d = webdriver.Firefox()
    d.get('https://web.whatsapp.com')
    while True:
        try:
            d.find_element_by_class_name('C28xL')
        except NoSuchElementException:
            pass
        else:
            sleep(1)
            return d

def sel_chat(name):
    global d, last_msg
    d.find_element_by_class_name('C28xL').click()
    d.find_element_by_tag_name('input').send_keys(name + Keys.ENTER)
    d.find_element_by_class_name('C28xL').click()
    last_msg = ''

def get_last_msg_raw():
    global d
    return d.find_elements_by_class_name('message-in')[-1].text

def get_last_msg():
    global d
    ss = get_last_msg_raw().split('\n')
    if len(ss) > 2 and ss[0][0] == '+':
        return ''.join(ss[2:-1])
    elif len(ss) > 2 and ss[0][0] != '+':
        return ''.join(ss[1:-1])
    else:
        return ''.join(get_last_msg_raw()[:-6])

def send_msg(msg):
    global d
    d.find_element_by_class_name('_2S1VP').send_keys(msg + Keys.ENTER)

def new_msg_in_chat():
    global d, last_msg
    if last_msg == '':
        last_msg = get_last_msg_raw()

    if last_msg != get_last_msg_raw():
        last_msg = get_last_msg_raw()
        return True
    return False

def unread_chats():
    global d
    return d.find_elements_by_class_name('OUeyt')

def wait_for_msg():
    global d, last_msg
    while True:
        if new_msg_in_chat():
            last_msg = get_last_msg_raw()
            return get_last_msg()
        sleep(1)
