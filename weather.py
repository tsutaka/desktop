import requests as req
import json
import sys
import configparser
import datetime

from pythonlib import date

class Weather:

    def __init__(self, city_name_, file_name):
        # 初期化
        config = configparser.ConfigParser()
        config.read('config.ini')
        # APIキーの指定
        self.API_KEY = config['WeatherAPI']['API_KEY']
        self.city_name = city_name_

    def get_weather(self):
        # 現在の天気URLひな形
        api = "http://api.openweathermap.org/data/2.5/" + \
            "weather?q={city}&units=metric&APPID={key}"
        url = api.format(city = self.city_name, key = self.API_KEY)
        # print(url)
        response = req.get(url)
        data = json.loads(response.text)
        # print("+ 都市=", data["name"])
        # print("| 天気=", data["weather"][0]["main"])
        # print("| 最低気温=", data["main"]["temp_min"])
        # print("| 最高気温=", data["main"]["temp_max"])
        # print("| 湿度=", data["main"]["humidity"])

        output = []
        output += [data["name"]]
        output += [data["weather"][0]["main"]]
        output += [data["main"]["temp_min"]]
        output += [data["main"]["temp_max"]]
        output += [data["main"]["humidity"]]

        return output

    def get_forecast(self):
        # 未来の天気URLひな形
        api = "http://api.openweathermap.org/data/2.5/" + \
            "forecast?q={city}&units=metric&APPID={key}"
        url = api.format(city = self.city_name, key = self.API_KEY)
        # print(url)
        response = req.get(url)
        data = json.loads(response.text)
        # print(
        #     json.dumps(data, ensure_ascii=False, indent=4,
        #         sort_keys=False, separators=(',', ': '))
        #     )

        # print("+場所=", data["city"]["name"])
        outputs = []
        lists = data["list"]
        for cnt, list_ in enumerate(lists):
            # print("+ 日時=", list_["dt_txt"])
            # print("| 天気=", list_["weather"][0]["main"])
            # print("| 最低気温=", list_["main"]["temp_min"])
            # print("| 最高気温=", list_["main"]["temp_max"])
            # print("| 湿度=", list_["main"]["humidity"])
            output = []
            output += [list_["dt_txt"]]
            output += [list_["weather"][0]["main"]]
            output += [list_["main"]["temp_min"]]
            output += [list_["main"]["temp_max"]]
            output += [list_["main"]["humidity"]]
            outputs += [output]
        return outputs

    def get_forecast_weather_day(self, date_):

        # 天気予報を取得
        data = weather.get_forecast()

        outputs = []
        for weather_ in data:
            weather_year = str(weather_[0])[0:4]
            weather_month = str(weather_[0])[5:7]
            weather_day = str(weather_[0])[8:10]
            weather_hour = str(weather_[0])[11:13]
            # print(weather_year, weather_month,
            #     weather_day, weather_hour)

            # 入力日時と同じ日付の場合
            if(date_.year == int(weather_year) and
                date_.month == int(weather_month) and
                date_.day == int(weather_day)):
                outputs += [weather_]

        return outputs

if __name__ == '__main__':
    print(">start")

    # インスタンス生成
    weather = Weather("Tokyo,JP", "config.ini")

    # 現在の天気を取得
    # print(weather.get_weather())

    # 天気予報の取得
    # print(weather.get_forecast())

    # 天気予報1日分を取得
    print(weather.get_forecast_weather_day(date.get_today()))

    print(">end")
