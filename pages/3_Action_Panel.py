import streamlit as st
import pandas as pd
from pagesetup import set_title
import requests


st.set_page_config(layout="wide")
set_title("FEOC", "Action Panel")
st.divider()

container1 = st.container()
with container1:
    tab11, tab12, tab13 ,tab14, tab15 = st.tabs(["Ask the Data", "Initiate Financial Transaction", "Add a Party", "Send Communications", "View Audit Log"])
with st.sidebar:
    tabA, tabB, tabC = st.tabs(["Common Questions", "Quick Summary", "Notes"])
    
#Ask The Data
    with tab11:
        st.markdown("#### Ask the Data")
        container111 = st.container()
        with container111:
            exp1111 = st.expander("Instructions", expanded=True)
            with exp1111:
                st.markdown("1. **Data Inquiry:** The AI chatbot, located under these notes, is here to assist you with data-related questions. Simply type your data inquiries in the chat window.")
                st.markdown("2. **AI Assistance:** The chatbot is equipped to provide information, insights, and perform data-related tasks based on your queries. It can assist with data retrieval, analysis, and more.")
                st.markdown("3. **User-Friendly:** The chatbot is designed to be user-friendly and responsive. You can initiate conversations, seek information, and engage with it just like you would with a human assistant.")
                st.markdown("4. **Streamlined Data Access:** The AI chatbot streamlines your access to data, making it convenient and efficient to gather insights and perform data-driven tasks.")
                st.markdown("5. **Ask Anything:** Feel free to ask questions about certificates, transactions, financial commitments, parties involved, project descriptions, or any other data-related topic. The chatbot is here to assist you!")
                
            exp1112 = st.expander("Details", expanded=True)
            with exp1112:
                st.markdown("- The AI chatbot is located in the Action Page, under these notes, providing continuous support for your data-related inquiries.")
                st.markdown("- Interaction with the chatbot is as simple as typing your questions or requests in the chat window and receiving immediate responses.")
                st.markdown("- The chatbot can help you extract data insights, perform data analysis, and assist with various data-related tasks, enhancing your experience with the web app.")
        #ask the data cont. (this will be present in the sidebar at all times)
with tabC:
    st.text_area("Write notes here:")
    st.success(f"your notes have been recordedy")

#Initiate Financial Transactions               
    with tab12:
        st.markdown("#### Initiate Financial Transaction")
        container121 = st.container()
        with container121:
            exp1211 = st.expander("Instructions", expanded=True)
            with exp1211:
                st.markdown("#### Instructions:")
                st.markdown("1. **Certificate ID:** This is a user-friendly, front-facing ID that uniquely identifies the certificate. Upon creation, an API key will be automatically linked to this ID, establishing the data connection for the certificate.")
                st.markdown("2. **Dates and Duration:** Select a start date, and either (a) specify an end date or (b) provide a duration. If you specify one, the other will be automatically calculated for you.")
                st.markdown("3. **Financial or Contractual Commitments:** Enter any financial or contractual commitments associated with the certificate. This could include financial obligations, contract terms, or other related commitments. Please note that this list is not exhaustive, and you can include any relevant information.")
                st.markdown("4. **Project Description:** Provide a project description. This description is a key input for AI prompts and automation. The AI will use this input to create the project description.")
                st.markdown("5. **Information for Parties Involved:")
                st.markdown("   - **Company Information (5a):** The company information will prepopulate after the company is searched for and selected. This may include details about the company involved in the certificate.")
                st.markdown("   - **People Information (5b):** This includes establishing the owner, who is responsible for the execution of the contract, and additional company users. You have the ability to add usernames and passwords for users as needed.")
                st.markdown("   - **Other Information (5c):** Capture any other specific information required for the certificate. This could include additional details relevant to the parties involved.")
                st.markdown("6. **Submit Button:** Click the \"Submit\" button to compile all the provided information. This will create an electronic contract, send it out for electronic signature by all parties (owners), and upon execution, the certificate will store the contract and automatically generate the certificate.")
                st.markdown("7. **Custom Terms and Conditions:** You have the ability to use AI to insert any additional terms and conditions. This feature allows you to include specific, customized terms and conditions as needed for the certificate.")
            exp1212 = st.expander("Details", expanded=True)
            with exp1212:
                st.markdown("#### Detail Notes:")
                st.markdown("- The Certificate ID serves as a unique and user-friendly identifier for certificates. It ensures easy reference and access to certificate-related data.")
                st.markdown("- The ability to choose between specifying an end date or duration provides flexibility when defining the certificate's timeline.")
                st.markdown("- For financial or contractual commitments, consider including details such as payment schedules, terms, and conditions that parties involved need to adhere to.")
                st.markdown("- The project description is a crucial input that aids in generating automated project descriptions, streamlining processes, and enhancing efficiency.")
                st.markdown("- The inclusion of company information simplifies data entry by prepopulating relevant details.")
                st.markdown("- People information, including the owner and additional users, contributes to the management and execution of the certificate. It allows for user access control.")
                st.markdown("- Custom Terms and Conditions provide the flexibility to adapt the contract to specific project requirements and legal terms. Using AI to generate these terms ensures accuracy and consistency.")
                st.markdown("- The \"Submit\" button streamlines the process by automating the generation of electronic contracts and facilitating electronic signatures, reducing manual paperwork.")
                st.markdown("- The linkage of an API key to the Certificate ID establishes the necessary data connections for efficient data management and retrieval.")
                

        
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
            df= pd.read_csv(".localdata/FEOC_transactionlist_dataset_test (1).csv")
            st.table(df)
        
        
            
        container122 = st.container()
        with container122:
            exp1221 = st.expander("Instructions", expanded=True)
            exp1222 = st.expander("Details", expanded=True)
    with tab13:
        st.markdown("#### Add a Party")
        container131 = st.container()
        st.write("You can add new parties (users within your company) here and track their processes.")
        party_name_first_name = st.text_input("New user's First Name", "")
        party_name_last_name = st.text_input("New user's Last Name", "")
        party_role = st.text_input("New user's role in the organization", "")
        party_email = st.text_input("New user's Email", "")
        party_phone = st.text_input("New user's phone number", "")
        if st.button("Add Party"):
            if party_name_first_name and party_name_last_name and party_role and party_email and party_phone:
                st.success(f"New User added successfully: representative:{party_name_first_name} {party_name_last_name}, {party_role}. contact information: {party_email}, {party_phone}")
        else:
            st.error("Please fill in all the fields, thank you!")
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
                sURL = st.secrets.HTTP_URL_COMMS
                sBody = {
                    "sender": user_type,
                    "name": name,
                    "email": email,
                    "message": message,
                    "recipient": recipient
                }
                sRequest = requests.post(url=sURL, json=sBody)
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
