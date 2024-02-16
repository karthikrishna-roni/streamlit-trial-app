import requests


def call(coin,date_s,date_e):
    url = "https://api.binance.com/api/v3/klines"

    params = {
        'symbol': coin,
        'interval': '1d',
        'startTime':  date_s ,
        'endTime':  date_e
    }

    response = requests.get(url, params = params)
    

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")

    return(data)



