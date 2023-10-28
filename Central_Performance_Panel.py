import streamlit as st
from functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Central Performance Panel")
    set_page_overview("Main Header", "View key information and metrics related to your FEOC.")
    st.progress(0.5, "Total Emissions Reduced")
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
                    value="""**Alert 1:** 10/01/2023 Financial transaction initiated by Emitter 
  **Alert 2:** 10/15/2023 Financial transaction initiated by Provider  
  **Alert 3:** 10/24/2023 New Purchaser Added - PanAm Airlines  
  **Alert 4:** 10/31/2023 Compliance Meeting Scheduled""",
                    disabled=True)

    # Define your dynamic variables
    operational_profits = 400000
    total_net_zero_fuel_sold = 1000000
    total_net_zero_tickets_sold = 10000000
    current_oc_value = 2504543232

    annual_offset_committed = 400000
    annual_offset_actual = 300000
    annual_offset_variance = annual_offset_committed - annual_offset_actual

    validation_date = "9/21/2023"
    validation_message = "Please check data compliance"
    success_date = "9/20/2023"
    success_message = "Data validation successfully completed; no errors"
    info_date = "9/15/2023"
    info_message = "Forward-selling activity initiated (100,000 tons fuel)"
  
    next_container = st.container()
    with next_container:
        exp2 = st.expander("Performance", expanded=True)
        with exp2:
            col21, col22, col23 = st.columns(3)
            
            with col21:
                st.markdown("#### Financial")
                st.markdown(f"**Operational Profits of Provider:** {operational_profits} metric tons CO₂e")
                st.markdown(f"**Total Net-Zero Fuel Sold:** {total_net_zero_fuel_sold} metric tons")
                st.markdown(f"**Total Net-Zero Tickets Sold:** {total_net_zero_tickets_sold} tickets")
                st.markdown(f"**Current OC Value:** ${current_oc_value}")
        
            with col22:
                st.markdown("#### Carbon Reduction")
                st.markdown(f"**Annual Offset (Committed):** {annual_offset_committed} metric tons CO₂e")
                st.markdown(f"**Annual Offset (Actual):** {annual_offset_actual} metric tons CO₂e")
                st.markdown(f"**Annual Offset (Variance):** {annual_offset_variance} ({annual_offset_variance / annual_offset_committed * 100:.2f}%) metric tons CO₂e")
        
            with col23:
                st.markdown("#### Validation and Verification")
                st.warning(f"{validation_date}: {validation_message}")
                st.success(f"{success}")
