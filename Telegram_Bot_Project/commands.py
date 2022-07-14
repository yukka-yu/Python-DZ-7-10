from telegram import Update
from telegram.ext import ContextTypes
import requests
from pyowm import OWM
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # sum 123 456
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def weather_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    owm = OWM('1d9a084266788353bef1ad217fd6e62f')
    msg = update.message.text
    city = msg.split(' ')[1]
    mngr = owm.weather_manager()
    observation = mngr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')
    status = w.detailed_status
    wind = w.wind()
    await update.message.reply_text(f'{status}, {temperature}, {wind}')
