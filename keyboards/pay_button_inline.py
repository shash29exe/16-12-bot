from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def pay_button(amount:float, url:str):
    """
        Кнопка для оплаты
    """

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=f'Оплатить ({amount:.0f}₽)',
                url=url
            )]
        ]
    )