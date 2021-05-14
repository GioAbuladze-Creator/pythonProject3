import requests
import json
# city = input("City: \n")

key ='fbde532726a7dd79d0dec6d4d9a9a717'

resp=requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}')
print(resp.status_code)
print(resp.headers)


res = json.loads(resp.text)

print(json.dumps(res,indent=4))
ing_url=res['url']
r_ing=requests.get(ing_url)
print(r_ing)