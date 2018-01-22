from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import os

@respond_to('(.*)')
def giveme(message, something):
    get_msg = '{}'.format(something)

    # debug
    # message.reply('{}'.format(something))

    # ここでhomeを呼ぶ
    os.system('ls -l')
    os.system('/home/pi/home-voice/git/say.sh ' + get_msg)
