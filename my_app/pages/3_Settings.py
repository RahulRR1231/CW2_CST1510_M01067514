import streamlit as st
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Redirect to login if not logged in
if not st.session_state.logged_in:
    st.error("Please log in to access the dashboard.")
    if st.button("Go to Login Page"):
       st.switch_page("Home.py")
       st.stop()
else:
    
    if st.button("LOG OUT"):
        st.session_state.username = ""
        st.session_state.logged_in = False
        st.switch_page("Home.py")

