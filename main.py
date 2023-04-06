import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import datetime

# st.set_page_config(layout='wide')

st.header("Weather Forecast for the Next Days")

place_input = st.text_input("Place:", placeholder="Enter Place Name")

forecast_days_sld = st.slider("Forecast Days", min_value=1, max_value=5)

select_output = st.selectbox("Select data to view", options=("Temperature", 'Sky'))

st.header(f"{select_output} for the next {forecast_days_sld} in {place_input}")

if place_input:
    try:
        weather_data = get_data(place_input, forecast_days_sld)

        if select_output == "Temperature":
            temperature = [format((value["main"]['temp']/10), '2f') for value in weather_data]

            wea_date = [value['dt_txt'] for value in weather_data]
            figure = px.line(x=wea_date, y=temperature,
                             labels={"x": "Date", "y": "Temperatures (C)"})
            st.plotly_chart(figure)

        if select_output == "Sky":
            sky_conditions = [value['weather'][0]["main"] for value in weather_data]
            image_path = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                          'Snow': 'images/snow.png'}
            update_image_path = [image_path[name]for name in sky_conditions]
            wea_date = [value['dt_txt'] for value in weather_data]
            date_format = '%Y-%m-%d %H:%M:%S'
            conv_list1=[]
            conv_list2=[]

            for cap in wea_date:
                new_date_format = datetime.strptime(cap, date_format)
                conv_list1.append(new_date_format)
                # print(conv_list1)

            for cap2 in conv_list1:
                image_time_cap = cap2.strftime("%a" + " %b"+" %d" + " %H" +":%M")
                conv_list2.append(image_time_cap)
                # print(conv_list2)

            st.image(update_image_path, width=115,  caption=conv_list2)


    except KeyError:
        st.info("You Enter Wrong Place Name, Try again!")
