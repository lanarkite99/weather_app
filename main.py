import streamlit as st
import plotly.express as px
st.title("Weather forecast for next days")

place=st.text_input("Place")
fore_days=st.slider("Forecast days", 1,5,1)
option=st.selectbox("Select data to view", ("Temperature", "Sky"))
st.write(option)
st.subheader(f"{option} for the next {fore_days} in {place}")

dates=["2024-01-10","2024-01-11","2024-01-12"]
temps=[11,13,5]
figure=px.line(x=dates,y=temps, labels={"x":"Date", "y":"Temperature"})
st.plotly_chart(figure)