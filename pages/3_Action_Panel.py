import streamlit as st
impport pandas as pd
from pagesetup import set_title


st.set_page_config(layout="wide")
set_title("FEOC", "Action Panel")
st.divider()

container1 = st.container()
with container1:
    tab11, tab12, tab13 ,tab14, tab15 = st.tabs(["Ask the Data", "Initiate Financial Transaction", "Add a Party", "Send Communications", "View Audit Log"])

    with tab11:
        st.markdown("#### Ask the Data")
        container111 = st.container()
        with container111:
            exp1111 = st.expander("Instructions", expanded=True)
            with exp1111:
                st.write("Hello")
            exp1112 = st.expander("Details", expanded=True)
            with exp1112:
                st.write("Hello")
        container112 = st.container()
        with container112:
            exp1121 = st.expander("Instructions", expanded=True)
            with exp1121:
                st.write("Hello")
            exp1122 = st.expander("Details", expanded=True)
            with exp1122:
                st.write("Hello")
    with tab12:
        st.markdown("#### Initiate Financial Transaction")
        container121 = st.container()
        with container121:
            exp1211 = st.expander("Instructions", expanded=True)
            with exp1211:
                st.write("Hello")
            exp1212 = st.expander("Details", expanded=True)
            with exp1212:
                st.write("Hello")
        container122 = st.container()
        with container122:
            exp1221 = st.expander("Instructions", expanded=True)
            exp1222 = st.expander("Details", expanded=True)
    with tab13:
        st.markdown("#### Add a Party")
        container131 = st.container()
        container132 = st.container()
    with tab14:
        st.markdown("#### Send Communications")
        container141 = st.container()
        container142 = st.container()
    with tab15:
        st.markdown("#### View Audit History")
        container151 = st.container()
        container152 = st.container()
        df= pd.read_csv(".localdata/FEOC_Audit_log_data_test.csv")
        st.table(df)
