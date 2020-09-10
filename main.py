import requests

wordlist = open("common.txt", "r")

for item in wordlist:
    item = item.strip()
    response = requests.get(f'http://192.168.126.129/{item}')
    if response.status_code == 200:
        print(item)