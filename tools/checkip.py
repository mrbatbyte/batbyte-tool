import requests
from bs4 import BeautifulSoup

def check_another_ip():
    ip = input(" \033[1;32m|--- \033[1;31m Enter IP Address: \033[1;32m")

    req = requests.get(f"https://www.whois.com/whois/{ip}")

    src = req.content
    sop = BeautifulSoup(src, 'lxml')
    git_info = sop.find_all('pre', {'df-raw'})

    print(git_info)