import streamlit as st
import plotly.express as px
from backend import get_data
import datetime

st.title("Weather forecast for next days")

place=st.text_input("Place")
fore_days=st.slider("Forecast days", 1,5,1)
option=st.selectbox("Select data to view", ("Temperature", "Sky"))
st.write(option)
st.subheader(f"{option} for the next {fore_days} in {place}")

if place:
    try:
        filtered_data=get_data(place, fore_days, option)

        dates = [diction["dt_txt"] for diction in filtered_data]

        if option=="Temperature":
            temperatures = [diction["main"]["temp"]-273.15 for diction in filtered_data]
            figure=px.line(x=dates,y=temperatures, labels={"x":"Date", "y":"Temperature"})
            st.plotly_chart(figure)

        if option=="Sky":
            strings={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png",
                     "Snow":"images/snow.png"}
            sky_conditions = [diction["weather"][0]["main"] for diction in filtered_data]
            img_paths=[strings[conditions] for conditions in sky_conditions]
            st.image(img_paths,width=115,caption=dates)
    except KeyError:
        st.write("The place doesn't exist")