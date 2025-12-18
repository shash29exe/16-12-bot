from fastapi import FastAPI, Request
from utils.payment_confirm import confirm_payment
from utils.payments import pending_payments
from main import bot

app = FastAPI()


@app.post('/yookassa/webhook')
async def yookassa_webhook(request: Request):
    data = await request.json()

    event = data.get('event')
    payment = data.get('object', {})
    if event != 'payment.succeeded':
        return {'status': 'ignored'}

    metadata = payment.get('metadata', {})
    internal_payment_id = metadata.get('internal_payment_id')
    if not internal_payment_id:
        return {'status': 'no_internal_id'}

    if internal_payment_id not in pending_payments:
        return {'status': 'not_found'}

    await confirm_payment(bot, internal_payment_id)
    return {'status': 'ok'}
