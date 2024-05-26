import requests
from keys import get_keys

API_Key=get_keys()
def get_data(place, f_days=None, type=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response=requests.get(url)
    data=response.json()
    return data


if __name__=="__main__":
    print(get_data(place="Tokyo"))