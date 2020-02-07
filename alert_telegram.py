import requests

def send(pair, order, stop_order):
    #Replace token, chat_id & text variables
    text = f'A new trade has been placed in {pair} at {order.lmitPrice} with a stop at {stop_order.auxPrice}'
    
    token = 'xxx'
    params = {'chat_id': xxx, 'text': text, 'parse_mode': 'HTML'}
    resp = requests.post('https://api.telegram.org/bot{}/sendMessage'.format(token), params)

send('EURUSD', order, stop_order)