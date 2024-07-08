import requests

response = requests.get('http://api.weatherapi.com/v1/ip.json?key=1863c61a79764cea9d2135128240807&q=auto:ip')

json= response.json()
country = json['country_name']
state = json['region']
city = json['city']

print(country + " " + state + " " + city)

request2 = 'http://api.weatherapi.com/v1/current.json?key=1863c61a79764cea9d2135128240807&q=' + str(city)
response2 = requests.get(request2)
json2 = response2.json()
print(json2)