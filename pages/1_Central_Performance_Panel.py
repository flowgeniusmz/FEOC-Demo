import streamlit as st
from pagesetup import set_title

st.set_page_config(layout="wide")
set_title("FEOC", "Central Performance Panel")
st.divider()

main_container = st.container()
with main_container:
    exp1 = st.expander("Certificate Information", expanded=True)
    with exp1:
        col11, col12 = st.columns(2)
        with col11:
            st.markdown("#### Details")
            col111, col112, col113 = st.columns(3)
            with col111:
                st.markdown("**Project:** Carbon Offset for Refinery")
                st.markdown("**FEOC ID:** FEOC-001")
                st.markdown("**Start Date:** 01/01/2023")

            with col112:
                st.markdown("**Emitter:** Petroleum Refinery")
                st.markdown("**Provider:** GismoPower")
                st.markdown("**Exp. Date:** 12/31/2030")
            with col113:
                st.markdown("**Purchaser:** Commercial Airline")
                st.markdown("**AAA-Rating:** Rating Value")     

        with col12:
            st.markdown("#### Notifications and Alerts")
            txtAlerts = st.text_area(
                label="**Alerts:**",
                value="""**Alert 1:** 10/01/2023 Financial transaction initiated by John Doe  
**Alert 2:** 10/01/2023 Financial transaction initiated by John Doe  
**Alert 3:** 10/01/2023 Financial transaction initiated by John Doe  
**Alert 4:** 10/01/2023 Financial transaction initiated by John Doe """,
                disabled=True)
        

next_container = st.container()
with next_container:
    exp2 = st.expander("Performance", expanded=True)
    with exp2:
        col21, col22, col23 = st.columns(3)
        with col21:
            st.markdown("#### Financial")
            st.markdown("**Operational Profits of Provider:** 400,000 metric tons CO₂e")
            st.markdown("**Total Net-Zero Fuel Sold:** 1,000,000 metric tons")
            st.markdown("**Total Net-Zero Tickets Sold:** 10,000,000 tickets")
            st.markdown("**Current OC Value:** $2,504,543,232")
        with col22: 
            st.markdown("#### Carbon Reduction")
            st.markdown("**Annual Offset (Committed):** 400,000 metric tons CO₂e")
            st.markdown("**Annual Offset (Actual):** 300,000 metric tons CO₂e")
            st.markdown("**Annual Offset (Variance):** 100,000 (25.00%) metric tons CO₂e")
        with col23:
            st.markdown("#### Validation and Verification")
            st.warning("9/21/2023: Please check data compliance")
            st.success("9/20/2023: Data validation successfully completed; no errors")
            st.info("9/15/2023: Forward-selling activity initiated (100,000 tons fuel)")
