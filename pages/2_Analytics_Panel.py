import streamlit as st
from pagesetup import set_title
import pandas as pd
import numpy as np
from charts.heatmap import render_heatmap_cartesian

st.set_page_config(layout="wide")
set_title("FEOC", "Analytics Panel")
st.divider()

container0 = st.container()
with container0:
    exp0=st.expander("Key Metrics", expanded=True)
    with exp0:
        col01, col02, col03 = st.columns(3)
        with col01:
            st.metric("Total Offset", "1,000,000", "200,000")
        with col02:
            st.metric("Total Offset", "1,000,000", "200,000")
        with col03:
            st.metric("Total Offset", "1,000,000", "200,000")

container1 = st.container()

with container1:
    exp1 = st.expander("Financial Analytics", expanded=True)
    with exp1:
        col11, col12, col13 = st.columns(3)
        with col11:
            st.markdown("#### Chart 1")
            chart_data11 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data11)
            #st.dataframe(chart_data11)
        with col12:
            st.markdown("#### Chart 2")
            chart_data12 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
            st.vega_lite_chart(
            chart_data12,
            {
                "mark": {"type": "circle", "tooltip": True},
                "encoding": {
                    "x": {"field": "a", "type": "quantitative"},
                    "y": {"field": "b", "type": "quantitative"},
                    "size": {"field": "c", "type": "quantitative"},
                    "color": {"field": "c", "type": "quantitative"},
                },
            },
            )
            #st.dataframe(chart_data12)
        with col13:
            st.markdown("#### Chart 3") 
            render_heatmap_cartesian()
            #st.dataframe(chart_data13)

container2 = st.container()

with container2:
    exp3 = st.expander("Live sensor data details", expanded=True)
    with exp3:
        st.write("In our environmental monitoring project, data was collected by a network of state-of-the-art sensors strategically placed in and around oil refineries across three different countries.") 
        st.write("These advanced sensors were strategically installed at critical locations within the refineries to measure key pollutants, including carbon monoxide (CO), nitrogen dioxide (NO2), sulfur dioxide (SO2), and unburned hydrocarbons (UHC). The sensors were designed to capture real-time data, and they transmitted this information to our central monitoring system. The sensors were periodically calibrated to ensure the accuracy of the measurements.The data collection process was managed by a team of dedicated experts who conducted routine maintenance checks to ensure the sensors were functioning optimally. Each sensor was equipped with GPS for precise location tracking, and data was timestamped to provide a record of when each measurement was taken. This comprehensive approach allowed us to gather valuable insights into the emissions and air quality surrounding these refineries. Our goal was to provide investors and purchasing teams with reliable information regarding the environmental impact of these refineries. The collected data was analyzed to calculate annual carbon reduction metrics, enabling us to report on the refinery's commitment to offsetting carbon emissions.") 
        st.write(" This data was further used to assess the refinery's actual emission reductions, highlight any variances, and demonstrate the environmental responsibility of these facilities")        

container3 = st.container()

with container3:
    exp4 =st.expander("Live sensor geospacial graphing")
    with exp4:
        st.write('New graphed data loaded upon login')
        places = pd.read_csv('.localdata/refinery_sensor_data_test.csv')
        st.map(places)


container4 = st.container()

with container4:
    exp2 = st.expander("Operational Analytics", expanded=True)
    with exp2:
        col21, col22, col23 = st.columns(3)
        with col21:
            st.markdown("#### Chart 1")
            chart_data21 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data21)
            #st.dataframe(chart_data21)
        with col22:
            st.markdown("#### Chart 2")
            chart_data22 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
            st.vega_lite_chart(
            chart_data22,
            {
                "mark": {"type": "circle", "tooltip": True},
                "encoding": {
                    "x": {"field": "a", "type": "quantitative"},
                    "y": {"field": "b", "type": "quantitative"},
                    "size": {"field": "c", "type": "quantitative"},
                    "color": {"field": "c", "type": "quantitative"},
                },
            },
            )
            #st.dataframe(chart_data22)
        with col23:
            st.markdown("#### Chart 3")
            chart_data23 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.area_chart(chart_data23)
            #st.dataframe(chart_data23)

container5 = st.container()

with container5:
    exp3 = st.expander("Other Analytics", expanded=True)
    with exp3:
        col31, col32, col33 = st.columns(3)
        with col31:
            st.markdown("#### Chart 1")
            chart_data31 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data31)
            st.dataframe(chart_data31)
        with col32:
            st.markdown("#### Chart 2")
            chart_data32 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
            st.vega_lite_chart(
            chart_data32,
            {
                "mark": {"type": "circle", "tooltip": True},
                "encoding": {
                    "x": {"field": "a", "type": "quantitative"},
                    "y": {"field": "b", "type": "quantitative"},
                    "size": {"field": "c", "type": "quantitative"},
                    "color": {"field": "c", "type": "quantitative"},
                },
            },
            )
            st.dataframe(chart_data32)
        with col33:
            st.markdown("#### Chart 3")
            chart_data33 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.area_chart(chart_data33)
            st.dataframe(chart_data33)
        
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

prompt = st.chat_input("Enter a question")
