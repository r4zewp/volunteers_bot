import asyncio
import logging
import sys
import os
import asyncio
import logging
import sys
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, CommandObject, Command, MagicData
from aiogram import F
from aiogram.types import Message

load_dotenv()
token = os.getenv('TOKEN')

dp = Dispatcher()
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def main() -> None:
    
    await dp.start_polling(bot)

