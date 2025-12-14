import streamlit as st

# Checks if the user is logged in

# Creates login state if it does not exist
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# If the user is not logged in, block access
if not st.session_state.logged_in:
    st.error("Please log in to access the dashboard.")

    # Button to go back to the login page
    if st.button("Go to Login Page"):
        st.switch_page("Home.py")
        st.stop()  # Stops the page from running


# Settings page (only visible if logged in)
else:
    # Page title
    st.title("⚙️ Settings")

    # Shows the username of the logged-in user
    st.subheader(
        f"Account Username : {st.session_state.get('username', 'Guest')}"
    )

    # Log out button
    if st.button("LOG OUT"):
        # Clears the username
        st.session_state.username = ""

        # Changes login status to logged out
        st.session_state.logged_in = False

        # Redirects to login page
        st.switch_page("Home.py")



