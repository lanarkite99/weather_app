import streamlit as st

st.title("Weather forecast for next days")

place=st.text_input("Place")
fore_days=st.slider("Forecast days", 1,5,1)
option=st.selectbox("Select data to view", ("Temperature", "Sky"))
st.write(option)
st.subheader(f"{option} for the next {fore_days} in {place}")
