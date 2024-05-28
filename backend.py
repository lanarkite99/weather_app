import requests
import streamlit

from keys import get_keys

API_Key=get_keys()
def get_data(place, f_days, type):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response=requests.get(url)
    data=response.json()
    no_days=8*f_days
    filtered_data=data["list"]
    filtered_data=filtered_data[:no_days]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo", f_days=3,type="Temperature"))