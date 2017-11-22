import requests

def live_social_status():

    url = 'https://www.cryptocompare.com/api/data/socialstats/?id=1182'
    page = requests.get(url)
    data = page.json()['Data']
    return data

data = live_social_status()
print(data)

# peut-être pas la meilleur solution