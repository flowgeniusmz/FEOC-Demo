import streamlit as st
from pagesetup import set_title
import pandas as pd
import numpy as np
from charts.heatmap import render_heatmap_cartesian

st.set_page_config(layout="wide")
set_title("FEOC", "Analytics Panel")
st.divider()

# Key Metrics
container0 = st.container()
with container0:
    exp0 = st.expander("Key Metrics", expanded=True)
    with exp0:
        col01, col02, col03 = st.columns(3)
        with col01:
            st.metric("Carbon Reduction Commitment", "1,500,000 Tons", "+250,000")
        with col02:
            st.metric("Net Zero Fuel Sales", "$1,500,000", "+$300,000")
        with col03:
            st.metric("Project Financing", "$5,000,000", "-$500,000")

# Financial Analytics
container1 = st.container()
with container1:
    exp1 = st.expander("Financial Analytics", expanded=True)
    with exp1:
        col11, col12, col13 = st.columns(3)
        
        with col11:
            st.markdown("#### Carbon Offset Revenue")
            chart_data11 = pd.DataFrame({
                'Months': list(range(1, 13)),
                'Revenue': np.random.randint(100000, 150000, 12)
            })
            st.line_chart(chart_data11.set_index('Months'))
        
        with col12:
            st.markdown("#### Carbon Reduction vs Commitment")
            chart_data12 = pd.DataFrame({
                'Months': list(range(1, 13)),
                'Actual Reduction': np.random.randint(100000, 130000, 12),
                'Committed Reduction': [125000] * 12
            })
            st.line_chart(chart_data12.set_index('Months'))
        
        with col13:
            st.markdown("#### Monthly Financing vs Returns")
            chart_data13 = pd.DataFrame({
                'Months': list(range(1, 13)),
                'Financing': np.random.randint(300000, 500000, 12),
                'Returns': np.random.randint(250000, 450000, 12)
            })
            st.bar_chart(chart_data13.set_index('Months'))

# Live Sensor Data
container2 = st.container()
with container2:
    exp3 = st.expander("Live sensor data details")
    with exp3:
        st.write("In our environmental monitoring project, data was collected by ...")
        places = pd.read_csv('.localdata/refinery_sensor_data_test_extended_values.csv')
        st.map(places)

# Operational Analytics
container4 = st.container()
with container4:
    exp2 = st.expander("Operational Analytics", expanded=True)
    with exp2:
        col21, col22, col23 = st.columns(3)
        
        with col21:
            st.markdown("#### Carbon Emission Over Time")
            chart_data21 = pd.DataFrame({
                'Months': list(range(1, 13)),
                'Emission': np.random.randint(5000, 15000, 12)
            })
            st.area_chart(chart_data21.set_index('Months'))
        
        with col22:
            st.markdown("#### Provider Project Efficiency")
            chart_data22 = pd.DataFrame({
                'Providers': ['A', 'B', 'C', 'D'],
                'Efficiency': np.random.rand(4)
            })
            st.bar_chart(chart_data22.set_index('Providers'))
        
        with col23:
            st.markdown("#### Monthly Equipment Failures")
            chart_data23 = pd.DataFrame({
                'Months': list(range(1, 13)),
                'Failures': np.random.randint(1, 5, 12)
            })
            st.bar_chart(chart_data23.set_index('Months'))
            
# Future Projections
container5 = st.container()
with container5:
    exp4 = st.expander("Future Projections", expanded=True)
    with exp4:
        st.markdown("#### Predicted Carbon Reduction")
        pred_data = pd.DataFrame({
            'Months': list(range(1, 13)),
            'Predicted Reduction': np.random.randint(110000, 130000, 12)
        })
        st.line_chart(pred_data.set_index('Months'))
        
        st.markdown("#### Predicted Net Zero Fuel Sales Growth")
        growth_data = pd.DataFrame({
            'Years': list(range(1, 6)),
            'Predicted Growth (%)': np.random.randint(5, 10, 5)
        })
        st.line_chart(growth_data.set_index('Years'))

# User Feedback
container6 = st.container()
with container6:
    exp5 = st.expander("User Feedback", expanded=True)
    with exp5:
        feedback_data = pd.DataFrame({
            'Rating': ['Excellent', 'Good', 'Average', 'Poor'],
            'Count': np.random.randint(50, 200, 4)
        })
        st.bar_chart(feedback_data.set_index('Rating'))

if __name__ == '__main__':
    st.write("Streamlit Analytics Dashboard")
