#! /home/pi/.pyenv/shims/python
# coding: utf-8

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()

