import streamlit as st
import pandas as pd
import numpy as np

def display_Analytics_panel():
    st.title("FEOC Analytics Panel")
    # Key Metrics
    st.header("Key Metrics")
    # col01, col02, col03 = st.columns(3)
    # with col01:
    #     st.metric("Carbon Reduction Commitment", "1,500,000 Tons", "+250,000")
    # with col02:
    #     st.metric("Net Zero Fuel Sales", "$1,500,000", "+$300,000")
    # with col03:
    #     st.metric("Project Financing", "$5,000,000", "-$500,000")

    # # Financial Analytics
    # st.header("Financial Analytics")
    # col11, col12, col13 = st.columns(3)
    # with col11:
    #     st.subheader("Carbon Offset Revenue")
    #     chart_data11 = pd.DataFrame({
    #         'Months': list(range(1, 13)),
    #         'Revenue': np.random.randint(100000, 150000, 12)
    #     })
    #     st.line_chart(chart_data11.set_index('Months'))

    # with col12:
    #     st.subheader("Carbon Reduction vs Commitment")
    #     chart_data12 = pd.DataFrame({
    #         'Months': list range(1, 13)),
    #         'Actual Reduction': np.random.randint(100000, 130000, 12),
    #         'Committed Reduction': [125000] * 12
    #     })
    #     st.line_chart(chart_data12.set_index('Months'))

    # with col13:
    #     st.subheader("Monthly Financing vs Returns")
    #     chart_data13 = pd.DataFrame({
    #         'Months': list(range(1, 13)),
    #         'Financing': np.random.randint(300000, 500000, 12),
    #         'Returns': np.random.randint(250000, 450000, 12)
    #     })
    #     st.bar_chart(chart_data13.set_index('Months'))

    # # Live Sensor Data
    # st.header("Live Sensor Data Details")
    # st.write("In our environmental monitoring project, data was collected by ...")
    # places = pd.read_csv('.localdata/refinery_sensor_data_test_extended_values.csv')
    # st.map(places)

    # # Operational Analytics
    # st.header("Operational Analytics")
    # col21, col22, col23 = st.columns(3)
    # with col21:
    #     st.subheader("Carbon Emission Over Time")
    #     chart_data21 = pd.DataFrame({
    #         'Months': list(range(1, 13)),
    #         'Emission': np.random.randint(5000, 15000, 12)
    #     })
    #     st.area_chart(chart_data21.set_index('Months'))

    # with col22:
    #     st.subheader("Provider Project Efficiency")
    #     chart_data22 = pd.DataFrame({
    #         'Providers': ['A', 'B
