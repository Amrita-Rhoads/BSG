# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:31:45 2018

@author: Amrita
"""


from __future__ import unicode_literals

import battlestargalactica as bsg

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import TelegramError, Unauthorized
import logging

import sys
import os
import time


def reply(bot, update, text):
    """
    Send a message to the chat.
    """
    bot.send_message(chat_id=update.message.chat_id, text=text)


def new_game(bot, update, chat_data=None, args=None):
    """
    Start a new blank game in the chat.
    """
    print("new game called!")
    if "game" not in chat_data:
        chat_data["game"] = bsg.Game(bot)
    elif not chat_data["game"]:
        chat_data["game"] = bsg.Game(bot)
    else:
        reply(bot, update, "Game already exists. /endgame?")
    reply(bot, update, chat_data["game"])


def join_game(bot, update, chat_data=None, args=None):
    """
    Join an existing game.
    """
    reply(bot, update, "about to add to game!")
    chat_data["game"].add_player(update.message.from_user.id,
                                update.message.from_user.first_name)
    reply(bot, update, "Added to game!")


def end_game(bot, update, chat_data=None, args=None):
    """
    End any existing games.
    """
    chat_data["game"] = None
    reply(bot, update, "Any existing game has been ended. /newgame?")


# Create an updater to fetch updates.
TOKEN = '743000106:AAHkYjE0ZtVd3tVT_xPajy1zdWZylaLl73I'
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -'
                    '%(message)s', level=logging.INFO,
                    filename='ignore/logging.txt', filemode='a')

joingame_synonyms = ["joingame", "join", "addme", "hibitch"]
newgame_handler = CommandHandler('newgame', new_game, pass_chat_data=True,
                                 pass_args=True)
joingame_handler = CommandHandler(joingame_synonyms, join_game,
                                  pass_chat_data=True, pass_args=True)
endgame_handler = CommandHandler('endgame', end_game, pass_chat_data=True)
dispatcher.add_handler(newgame_handler)
dispatcher.add_handler(joingame_handler)
dispatcher.add_handler(endgame_handler)

dispatcher.add_handler(CommandHandler('hi', (lambda bot, update : bot.send_message(chat_id=update.message.chat.id, text="/hi")) ))


updater.start_polling()
