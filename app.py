import streamlit as st
import requests

'''
# MinimalistApp
'''

'''
## Data
'''
pickup_datetime = st.text_input('Data and time', '2013-07-06 17:18:00')
pickup_longitude = st.text_input('Pickup longitude', '-73.950655')
pickup_latitude = st.text_input('Pickup latitude', '40.783282')
dropoff_longitude = st.text_input('Dropoff longitude', '-73.984365')
dropoff_latitude = st.text_input('Dropoff latitude', '40.769802')
passenger_count = st.text_input('Passenger count', '1')

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Prediction with Le Wagon API')

my_dict = {'pickup_datetime': pickup_datetime, 
           'pickup_longitude': pickup_longitude, 
           'pickup_latitude': pickup_latitude,
           'dropoff_longitude': dropoff_longitude,
           'dropoff_latitude': dropoff_latitude,
           'passenger_count': passenger_count} 

if st.button("Predict"):
    try:
        response = requests.get(url, params=my_dict)
        if response.status_code == 200:
            prediction = response.json()["fare"]
            st.success(f"Prediction: **{prediction:.2f} $**")
        else:
            st.error(f"Error API ({response.status_code}) : {response.text}")
    except Exception as e:
        st.error(f"Fail call API : {e}")