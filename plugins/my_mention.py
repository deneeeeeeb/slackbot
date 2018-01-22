from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import os


@listen_to('.*')
def mention_func(message):

    # debug
    # print(dir(message))
    # print(message.body)
    # print(message.body['text'])
    # message.reply(message.body['text']) 


    # call say.sh
    cmd = '/home/pi/home-voice/git/say.sh "' + message.body['text'] + '"'
    print(cmd)
    os.system(cmd)


