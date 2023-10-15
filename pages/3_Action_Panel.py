import streamlit as st
import pandas as pd
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
 #Initiate Financial Transactions               
    with tab12:
        st.markdown("#### Initiate Financial Transaction")
        menu = st.selectbox("Menu", ["Add Transaction", "View Transactions"])
        if menu == "Add Transaction":
            st.subheader("Add Transaction")
            certificate_id = st.text_input("Certificate ID (Front-facing ID)", "")
            start_date = st.date_input("Start Date", None)
            end_date = st.date_input("End Date", None)
            duration = st.number_input("Duration (in days)", value=0)
            commitments = st.text_area("Financial/Contractual Commitments", "")
            project_description = st.text_area("Project Description", "")
            if st.button("Submit Transaction"):
                if certificate_id and start_date and end_date and duration and commitments and project_description:
                    st.success("Transaction added successfully!")
            else:
                st.error("Please fill in all the fields")

        elif menu == "View Transactions":
            df= pd.read_csv("/workspaces/FEOC-Demo/localdata/FEOC_transactionlist_dataset_test (1).csv")
            st.table(df)
        
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
        st.write("You can add new parties (users within your company) here and track their processes.")
        party_name = st.text_input("New user's Name", "")
        party_email = st.text_input("New user's Email", "")
        party_role = st.text_input("user's Role within your organization", "")
        user_type = st.selectbox("User type", ["A Emitter", "B Provider", "C Development Team"])
        if st.button("Add Party"):
            if party_name and party_email and party_role and user_type:
                st.success(f"Party added successfully: {party_name}, {party_email}, {party_role}, {user_type}")
        else:
            st.error("Please fill in all the fields")
    with tab14:
        st.markdown("#### Send Communications")
        container141 = st.container()
    # Selector for "Who are you?"
        user_type = st.selectbox("Process position", ["Emitter", "Provider", "Other", "Development Team"])
        
        name = st.text_input("Name", "")
        email = st.text_input("Email", "")
        message = st.text_area("Message", "")
        
        # Selector for "Who you are reaching out to?"
        recipient = st.selectbox("Who you are reaching out to?", ["Emitter", "Provider", "Other", "Development Team"])
        
        if st.button("Submit"):
            if name and email and message:
                st.success("Message sent successfully!")
                st.write(f"You are {user_type}, reaching out to {recipient}.")
            else:
                st.error("Please fill in all the fields.")
    with tab15:
        st.markdown("#### View Audit History")
        container151 = st.container()
        options=st.multiselect("find", options= ("Client name", "Purchase made", "date"))
        df= pd.read_csv(".localdata/FEOC_Audit_log_data_test.csv")
        st.table(df)
