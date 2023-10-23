import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd

#Available for users, notifications, auditlog
def supabase_run_query(varTable):
    #Set Variables
    varColumnsSelect = "*"
    varTTL = "10m"

    #Initialize connection
    fConnection = st.experimental_connection("supabase", SupabaseConnection)

    #Perform Query
    fRows = fConnection.query(varColumnsSelect, table=varTable, ttl=varTTL).execute()
    
    #Get only the data
    fData = fRows.data

    #Create dataframe
    fDataframe = pd.DataFrame(fData)

    return fDataframe




    

#https://docs.streamlit.io/knowledge-base/tutorials/databases/supabase#copy-your-app-secrets-to-the-cloud
#https://docs.streamlit.io/knowledge-base/tutorials/databases/supabase#create-a-supabase-database
