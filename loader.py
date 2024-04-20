import asyncio
import logging
import sys
import os
import asyncio
import logging
import sys

from config.database import database
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, html, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, CommandObject, Command, MagicData
from aiogram import F
from aiogram.types import Message
from config import middleware
from aiogram.fsm.context import FSMContext
from state_groups.Signup import *

from config.routers.user_router import user_router

load_dotenv()
token = os.getenv('TOKEN')



bot = Bot(token=token,
           default=DefaultBotProperties(parse_mode=ParseMode.HTML))




