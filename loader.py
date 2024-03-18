from aiogram import Bot, Dispatcher
from data.config import settings


bot = Bot(settings.BOT_TOKEN.get_secret_value())
dp = Dispatcher()