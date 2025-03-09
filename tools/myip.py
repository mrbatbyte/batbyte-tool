import requests

def myip():

    req = requests.get(f"https://api.myip.com/")

    ip = req.json()['ip']
    cc = req.json()['cc']
    country = req.json()['country']

    print("\033[1;32mYour IP Address: \033[1;33m" + ip)
    print("\033[1;32mYour CC : \033[1;33m" + cc)
    print("\033[1;32mYour Country : \033[1;33m" + country)