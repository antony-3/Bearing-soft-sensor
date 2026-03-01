import streamlit as st
import requests

API_URL = ""

st.title('Bearing Soft Sensor')

vib_x = st.number_input('Vibration X', value=0.1)
vib_y = st.number_input('Vibration Y', value=0.1)
vib_z = st.number_input('Vibration Z', value=0.1)

if st.button('Predict'):
    payload = {
        'vib_x': vib_x,
        'vib_y': vib_y,
        'vib_z': vib_z}
    
    r = requests.post(API_URL, json=payload)
    st.success(r.json())

    