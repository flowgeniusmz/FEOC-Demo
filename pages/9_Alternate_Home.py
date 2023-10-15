import streamlit as st
from login import get_loginform
from pagesetup import set_title

if 'authenticated' not in st.session_state:
    get_loginform()
else:
    set_title("Faulkner Emission Offset Certificate Program", "Home")
    st.divider()
    main_container = st.container()
    with main_container:
        exp1 = st.expander("Overview", expanded=True)
        with exp1:
            st.header("Welcome to the Faulkner Emission Solutions Platform!")
            
            st.write("We are thrilled to have you join our mission. Whether you're an Emitter, a Provider, a Purchaser, or simply a champion for the environment, this platform aims to unify our collective efforts towards a greener planet.")
            
            st.markdown("**Emitters**, you are the linchpin of emission reduction, driving us towards a sustainable future. Your investments empower Providers to innovate and bring forth Green Solutions that battle against emissions.")
            
            st.markdown("**Providers**, with your groundbreaking solutions, you are lighting the path to a brighter, cleaner future. By collaborating with Emitters, we are making strides in environmental conservation.")
            
            st.markdown("**Purchasers**, by choosing to back reduced emission products, you set a commendable standard. Every purchase you make takes us one step closer to a cleaner, better world.")
            
            st.markdown("Introducing the **Faulkner Certificates** - our benchmark for emission offset. These certificates not only validate and track environmental contributions but, with the aid of state-of-the-art AI technology, ensure their authenticity, accuracy, and completeness.")
            
            st.subheader("Harness the power of cutting-edge AI technology.")
            st.write("Our AI continuously refines and validates data, ensuring accuracy and credibility at every step.")
            
            st.subheader("To our vibrant user community")
            st.write("Your interactions and inputs amplify the effectiveness of our platform. Each one of you is a cog in this grand machinery combating climate change. Together, let's pave the way for a sustainable, verdant future for the next generation.")
            
            st.write("Jump in, explore, and be the change you wish to see in the world!")
