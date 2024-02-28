
import requests
import json

city=input("PLEASE ENTER THE CITY YOU WANT TO FORECAST :")

url=f"https://api.weatherapi.com/v1/current.json?key=4f27f59912b94e79a2a183845242602&q={city}"

r=requests.get(url)
wdic= json.loads(r.text)
print (f"The Temperature in {city} is " , wdic ["current"]["temp_c"] , "degrees ",  )