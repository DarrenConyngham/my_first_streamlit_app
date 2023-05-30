import streamlit as st
import pandas as pd

data = {
    'Series 1': [1, 3, 4, 5, 7],
    'Series 2': [10, 30, 40, 100, 250]
}

df = pd.DataFrame(data)

st.title("Our first Streamlit app")
st.subheader("Introducing Streamlit in Automate Everything with Python")
st.write("This is to demonstrate how to use Streamlit to build a simple web app.")
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider("Celsius temperature")
st.write(myslider, "In Fahrenheit is", myslider * 9 / 5 + 32)