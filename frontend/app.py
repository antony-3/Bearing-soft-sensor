# import streamlit as st
# import requests

# API_URL = "https://bearing-soft-sensor.onrender.com"

# st.title('Bearing Soft Sensor')

# vib_x = st.number_input('Vibration X', value=0.1)
# vib_y = st.number_input('Vibration Y', value=0.1)
# vib_z = st.number_input('Vibration Z', value=0.1)

# if st.button('Predict'):
#     payload = {
#         'vib_x': vib_x,
#         'vib_y': vib_y,
#         'vib_z': vib_z}
    
#     r = requests.post(f'{API_URL}/predict', json=payload)
#     st.success(r.json())

import streamlit as st
import requests

API_URL = "https://bearing-soft-sensor.onrender.com"

payload = {"vib_x": 1.0, "vib_y": 2.0, "vib_z": 3.0}

r = requests.post(f"{API_URL}/predict", json=payload)

st.write("Status code:", r.status_code)
st.write("Raw response text:")
st.code(r.text)