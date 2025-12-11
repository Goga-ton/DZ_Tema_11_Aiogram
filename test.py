
import requests


def get_weather(city):
    api_key = 'd8c70d191e440c410b7a57897a5ee1c5'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url) # получаем все что есть в сcылке
    data = response.json()
    print(f"Город: {data['name']}")
    print(f"Температура: {data['main']['temp']}°C")
    print(f"Ощущается как: {data['main']['feels_like']}°C")
    print(f"Описание: {data['weather'][0]['description']}")
    print(f"Влажность: {data['main']['humidity']}%")

    return data
   # return response.json() #возвращаем в формате json

result = get_weather('Tomsk')
# print(result['name'])

