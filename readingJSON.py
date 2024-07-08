import pip
import requests

response = requests.get('http://api.open-notify.org/astros', headers= {
'Content-Type': 'application/json',
'Accept': 'application/json',
'Connection': 'keep-alive',
'Date': 'Wed, 03 Jul 2024 20:20:09 GMT',
'Accept-Language': 'en-US,en;q=0.9',
'Host': 'api.open-notify.org',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
})
json = response.json()
print(json)
#print people
print('The people currently in space are ')
for person in json['people']:
    print(person['name'])