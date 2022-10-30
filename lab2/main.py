import requests

s_city = "Moscow, RU"
appid = "99a4abe3f8ecc57e027265306f7ede09"

def today(s_city,appid):
    print("Сегодняшние данные")
    res=requests.get("http://api.openweathermap.org/data/2.5/weather",
        params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data=res.json()
    print("Город:", s_city)
    print("Скорость ветра:", data['wind']['speed'])
    print("Видимость:", data['visibility'])

def week(s_city,appid):
    print("Данные на неделю")
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    for i in data['list']:
        print("Дата <", i['dt_txt'],
              "> \r\n Скорость ветра: ", i['wind']['speed'],
              "\r\n Видимость:", i['visibility'])
    print("____________________________")
today(s_city,appid)
week(s_city,appid)
