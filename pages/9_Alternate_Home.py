import streamlit as st
from pagesetup import set_title

st.set_page_config(layout="wide")
set_title("FEOC", "Central Performance Panel")

# Display progress bar with the emissions reduced
progress = st.progress(0.5)
st.caption("Total Emissions Reduced")
st.divider()

# Certificate Information
with st.expander("Certificate Information", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Details")
        col1a, col1b, col1c = st.columns(3)
        
        with col1a:
            st.markdown("**Project:** Carbon Offset for Refinery")
            st.markdown("**FEOC ID:** FEOC-001")
            st.markdown("**Start Date:** 01/01/2023")
            
        with col1b:
            st.markdown("**Emitter:** Petroleum Refinery")
            st.markdown("**Provider:** GismoPower")
            st.markdown("**Exp. Date:** 12/31/2030")
            
        with col1c:
            st.markdown("**Purchaser:** Commercial Airline")
            st.markdown("**AAA-Rating:** Rating Value")
    
    with col2:
        st.markdown("#### Notifications and Alerts")
        st.text_area(
            label="**Alerts:**",
            value="""**Alert 1:** 10/01/2023 Financial transaction initiated by John Doe  
**Alert 2:** 10/01/2023 Financial transaction initiated by John Doe  
**Alert 3:** 10/01/2023 Financial transaction initiated by John Doe  
**Alert 4:** 10/01/2023 Financial transaction initiated by John Doe """,
            disabled=True)

# Performance
with st.expander("Performance", expanded=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Financial")
        st.bar_chart({"Operational Profits (in metric tons CO₂e)": [400000], "Net-Zero Fuel Sold (in metric tons)": [1000000]})
        st.markdown("**Total Net-Zero Tickets Sold:** 10,000,000 tickets")
        st.markdown("**Current OC Value:** $2,504,543,232")
    
    with col2:
        st.markdown("#### Carbon Reduction")
        data = {"Annual Offset (Committed)": 400000, "Annual Offset (Actual)": 300000}
        st.bar_chart(data)
        st.markdown("**Variance:** 100,000 (25.00%) metric tons CO₂e")
    
    with col3:
        st.markdown("#### Validation and Verification")
        st.warning("9/21/2023: Please check data compliance")
        st.success("9/20/2023: Data validation successfully completed; no errors")
        st.info("9/15/2023: Forward-selling activity initiated (100,000 tons fuel)")
