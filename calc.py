from subprocess import Popen, PIPE
from time import sleep
import whatsapp_api as wa

wa.setup()

while True:
    cs = wa.unread_chats()
    for c in cs:
        c.click()
        s = wa.get_last_msg()

        for i in ('calculate ', 'Calculate ', 'calc ', 'Calc '):
            if s.startswith(i):
                if len(i) > 6:
                    q = s[10:]
                else:
                    q = s[5:]

                p_echo = Popen(['echo', q], stdout=PIPE, stderr=PIPE)
                p_bc = Popen(['bc', '-l'], stdin=p_echo.stdout, stdout=PIPE, stderr=PIPE)
                out, err = p_bc.communicate()

                if err:
                    wa.send_msg('that was an invalid query :(')
                if out:
                    wa.send_msg(out.decode('utf-8').strip('\n'))

                break

    sleep(1)
