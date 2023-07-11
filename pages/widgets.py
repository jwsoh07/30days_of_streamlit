import streamlit as st


def on_change_handler():
    st.session_state.select_video = "is_selected"


# variable name can be what the slider input represents
some_number = st.slider("test slider", value=[50, 60])

st.write(some_number)

selected_video = st.selectbox(
    "Please select a video.",
    options=["Video A", "Video B", "Video C"],
)

st.write(selected_video)
