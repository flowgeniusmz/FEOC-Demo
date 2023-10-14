import streamlit as st
from login import get_loginform
from pagesetup import set_title


if 'authenticated' not in st.session_state:
    get_loginform()
else:
    set_title("FEOC", "Home")
    st.divider()
    main_container = st.container()
    with main_container:
        exp1 = st.expander("Overview", expanded=True)
        with exp1:
            st.write("Welcome")
