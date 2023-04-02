import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')

st.header("Weather Forecast for the Next Days")


place_input = st.text_input("Place:", placeholder="Enter Place Name")

forecast_days_sld = st.slider("Forecast Days",min_value=1, max_value=5)

select_output = st.selectbox("Select data to view", options=("Temperature", 'Sky'))

st.header(f"{select_output} for the next {forecast_days_sld} in {place_input}")

if select_output == "Temperature":
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
