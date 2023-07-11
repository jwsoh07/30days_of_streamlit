import streamlit as st


# variable name can be what the slider input represents
some_number = st.slider("test slider", value=[50, 60])

st.write(some_number)

selected_video = st.selectbox(
    "Please select a video.",
    options=["Video A", "Video B", "Video C"],
)

st.write(selected_video)

selected_videos = st.multiselect(
    "Select video(s) you wish to watch.", options=["Video A", "Video B", "Video C"]
)

st.write("You selected:", selected_videos)


st.header("st.checkbox")

st.write("What would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Okay, here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")
