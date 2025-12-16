from aiogram.utils.keyboard import ReplyKeyboardBuilder

def hello_kb():
    """
        Кнопка приветствия
    """

    builder = ReplyKeyboardBuilder()
    builder.button(text='Приветствую')

    return builder.as_markup(resize_keyboard=True)
