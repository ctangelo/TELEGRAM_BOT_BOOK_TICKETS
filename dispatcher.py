from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = "5934557949:AAFrqKVfW0X3SoUecxReUIzwOXAN6W8JyUs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
