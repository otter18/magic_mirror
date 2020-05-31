
def info():
    import requests
    s_city = "Moscow,RU"
    city_id = 524901
    appid = "3957babd7a920cb791cdc4f3fdaf1a2f"
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
#%%
    
def current_weather():
    import requests
    city_id = 524901
    appid = "3957babd7a920cb791cdc4f3fdaf1a2f"
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    current_weather = res.json()
    return  current_weather


#%%
def forecast():
    import requests
    city_id = 524901
    appid = "3957babd7a920cb791cdc4f3fdaf1a2f"
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    forecast = res.json()
    return forecast





