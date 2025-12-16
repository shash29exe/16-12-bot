from aiogram import Bot
from utils.payments import pending_payments


async def confirm_payment(bot: Bot, payment_id: str):
    payment = pending_payments.get(payment_id)
    if not payment:
        return

    user_id = payment['user_id']
    username = payment['username']
    amount = payment['amount']
    message_id = payment.get('message_id')

    if message_id:
        try:
            await bot.edit_message_reply_markup(chat_id=user_id, message_id=message_id, reply_markup=None)
        except:
            print('Не удалось удалить кнопку.')

    await bot.send_message(user_id, 'Платёж успешно обработан.')
    payment['status'] = 'success'
