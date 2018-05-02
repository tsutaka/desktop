import requests as req
import json
import sys
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# print(config.sections())

# APIキーの指定
API_KEY = config['WeatherAPI']['API_KEY']
# URLひな形
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 検索都市名
city_name = "Tokyo,JP"
url = api.format(city = city_name, key = API_KEY)

# 温度変換(ケルビン→摂氏)
k2c = lambda k: k - 273.15

# print(url)
response = req.get(url)
data = json.loads(response.text)
print(data)
print("+ 都市=", data["name"])
print("| 天気=", data["weather"][0]["description"])
print("| 最低気温=", k2c(data["main"]["temp_min"]))
print("| 最高気温=", k2c(data["main"]["temp_max"]))
print("| 湿度=", data["main"]["humidity"])
print("| 気圧=", data["main"]["pressure"])
print("| 風向き=", data["wind"]["deg"])
print("| 風速度=", data["wind"]["speed"])
print("")
