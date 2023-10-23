import streamlit as st
from PIL import Image
from login import get_loginform
from pagesetup import set_title
import hydralit_components as hc
from Central_Performance_Panel import display_Central_Performance_Panel
import pandas as pd
import numpy as np

st.set_page_config(layout='wide', page_title="Faulkner Emission Offset Certificate Program")

if 'authenticated' not in st.session_state:
    get_loginform()
else:
    menu_data = [
        {'label':'Performance Panel'},
        {'label':"Action Panel",'':"Dropdown1", 'submenu':[{'label':"Create a Certificate"},{'id':'subid12', 'label':"monitor existing certificates"},{'id':'subid13', 'label':"contact partner(s)"}]},
        {'label':"Analytics Panel"},
    ]   
    over_theme = {'txc_active': '#FFFFFF'}
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        login_name='Logout',
        hide_streamlit_markers=True,
        sticky_nav=False,
        sticky_mode='sticky',  # 'jumpy' or 'not-jumpy', but sticky or pinned
)

    if menu_id== 'Performance Panel':
        display_Central_Performance_Panel()

    elif menu_id== 'Create a Certificate':
        display_Central_Performance_Panel()

    elif menu_id== 'monitor existing certificates':
        display_existing_certificates()

    elif menu_id== "contact partner(s)":
        display_contact_partners()

    elif menu_id== 'Analytics Panel':
        display_Analytics_panel()
        
    elif menu_id== 'Home':
        st.header("Welcome")
        # Main content
        st.write("Welcome to the Emission Solutions Web App!")
        st.write("We're excited to have you on board, whether you're an Emitter, Provider, Purchaser, or just someone interested in making a difference in our environment. Our platform is designed to bring all these entities together to make a positive impact on the world.")
        "---"
        st.markdown("***As an Emitter***, you play a crucial role in reducing emissions and working towards a sustainable future. The investments you make in Providers contribute to the creation of innovative Green Solutions that help combat emissions.")
        st.markdown("***Providers***, your innovative solutions are at the forefront of this battle. By partnering with Emitters, you're creating a brighter, greener future.")
        st.markdown("***Purchasers***, your choice to support reduced emission products is commendable. Your purchases directly impact the reduction of emissions, leading us to a cleaner planet.")
        st.markdown("Our Emission Offset Certificates, known as the **Faulkner Certificates**, track and validate the impact of these efforts. Emission Data, AI Activities, Completeness Checks, and Verifications ensure the accuracy and credibility of these certificates.")
        st.subheader("Harnessing the world's most advanced AI technology available.")
        st.write("Behind the scenes, our AI tirelessly processes data and iterates for accuracy, capturing every detail through AI Activities, Completeness Checks, and Accuracy Iterations.")
        st.subheader("Leverage future potential now")
        st.write("Last but not least, our User community is a vital part of this ecosystem. User Activities reflect your interactions and contributions to this platform.")
        st.write("Together, we are all part of a global effort to combat climate change and make the world a better place. Join us in this collective endeavor, and let's create a sustainable and greener future for generations to come.")
        st.write("Get started, explore, and be a part of the solution today!")
