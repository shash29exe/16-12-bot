import os
import uuid
import aiohttp
from typing import Dict

YOOKASSA_API = 'https://api.yookassa.ru/v3'
SHOP_ID = os.getenv('YOOKASSA_SHOP_ID')
SECRET_KEY = os.getenv('YOOKASSA_SECRET_KEY')
RETURN_URL = os.getenv('YOOKASSA_RETURN_URL')

pending_payments: Dict[str, dict] = {}


async def create_payment(amount: float, description: str, user_id: int, username: str):
    """
        Метод создания платежа
    """

    payment_id = str(uuid.uuid4())
    payload = {
        'amount': {'value': f'{amount:.2f}', 'currency': 'RUB'},
        'confirmation': {'type': 'redirect', 'return_url': RETURN_URL},
        'capture': True,
        'description': description,
        'metadata': {'internal_payment_id': payment_id}
    }

    auth = aiohttp.BasicAuth(login=SHOP_ID, password=SECRET_KEY)

    async with aiohttp.ClientSession(auth=auth) as session:
        headers = {'Idempotence-Key': payment_id, 'Accept': 'application/json'}

        async with session.post(f'{YOOKASSA_API}/payments', json=payload, headers=headers) as resp:
            data = await resp.json()
            print(f'Payment response: {data}, {resp.status}')

            if resp.status not in (200, 201):
                raise RuntimeError(f'Payment failed with status code {resp.status}')

            confirmation_url = data['confirmation']['confirmation_url']

            pending_payments[payment_id] = {
                'user_id': user_id,
                'username': username or '',
                'amount': amount,
                'status': 'pending'
            }

            return confirmation_url, payment_id
