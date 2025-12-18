from fastapi import FastAPI, Request
from utils.payment_confirm import confirm_payment
from utils.payments import pending_payments

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

    return {'status': 'ok', 'payment_id': internal_payment_id}
