import streamlit as st
from app.data.incidents import *
from app.data.tickets import *
from app.data.datasets import*
from app.data.db import connect_database

# Checks if the user is logged in

# Creates a login state if it does not exist
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# If the user is not logged in, access is denied
if not st.session_state.logged_in:
    st.error("Please log in to access the dashboard.")

    # Button to go back to the login page
    if st.button("Go to Login Page"):
        st.switch_page("Home.py")
        st.stop()  # Stops the rest of the page from running


# Dashboard (only shows if logged in)
else:
    # Connects to the database
    conn = connect_database("DATA/intelligence_platform.db")

    # Creates tabs for each type of data
    tab_incidents, tab_tickets, tab_datasets = st.tabs(
        ["Incidents", "Tickets", "Datasets"]
    )

    
    # Incidents tab
    with tab_incidents:
        # Gets all incident data from the database
        incidents = get_all_incidents(conn)

        # Shows incident severity as charts
        st.title("Bar Chart For Incident Severity")
        st.bar_chart(incidents['severity'].value_counts())

        st.title("Line Chart For Incident Severity")
        st.line_chart(incidents['severity'].value_counts())

        # Shows incident status as charts
        st.title("Bar Chart For Incident Status")
        st.bar_chart(incidents['status'].value_counts())

        st.title("Line Chart For Incident Status")
        st.line_chart(incidents.groupby('status').size())

        # Shows incident category as charts
        st.title("Bar Chart For Incident Category")
        st.bar_chart(incidents['category'].value_counts())

        st.title("Line Chart For Incident Category")
        st.line_chart(incidents.groupby('category').size())

    
    # Tickets tab
    with tab_tickets:
        # Gets all ticket data from the database
        tickets = get_all_tickets(conn)

        # Shows ticket priority as charts
        st.title("Bar Chart For Ticket Priority")
        st.bar_chart(tickets['priority'].value_counts())

        st.title("Line Chart For Ticket Priority")
        st.line_chart(tickets['priority'].value_counts())

        # Shows ticket status as charts
        st.title("Bar Chart For Ticket Status")
        st.bar_chart(tickets['status'].value_counts())

        st.title("Line Chart For Ticket Status")
        st.line_chart(tickets['status'].value_counts())

        # Shows tickets are assigned to whom as charts
        st.title("Bar Chart For Ticket Assigned To")
        st.bar_chart(tickets['assigned_to'].value_counts())

        st.title("Line Chart For Ticket Assigned To")
        st.line_chart(tickets['assigned_to'].value_counts())

    
    # Datasets tab
    with tab_datasets:
        # Gets all dataset data from the database
        datasets = get_all_datasets(conn)

        # Shows how many datasets each person uploaded
        st.title("Bar Chart For Data Scientist")
        st.bar_chart(datasets['uploaded_by'].value_counts())

        st.title("Line Chart For Data Scientist")
        st.line_chart(datasets['uploaded_by'].value_counts())
