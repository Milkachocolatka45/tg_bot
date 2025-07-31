from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


help_kb = ReplyKeyboardBuilder()

help_kb.add(
    KeyboardButton(text = "інфо"),
    KeyboardButton(text = "анектод")
)
help_kb.adjust(2)
