# Import Streamlit and Week 8 functions
import streamlit as st
from app.data.db import connect_database
from app.data.incidents import *
from app.data.tickets import *
from app.data.datasets import*
from time import sleep

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Redirect to login if not logged in
if not st.session_state.logged_in:
    st.error("Please log in to access the dashboard.")
    if st.button("Go to Login Page"):
       st.switch_page("Home.py")
       st.stop()
else:

    # Connect to database (Week 8 function)
    conn = connect_database("DATA/intelligence_platform.db")






    tab_incidents, tab_tickets, tab_datasets = st.tabs(["Incidents", "Tickets", "Datasets"])
    with tab_incidents:

        
        # Page title
        st.title("Cyber Incidents Dashboard")

        # READ: Display incidents in a beautiful table (Week 8 function + Streamlit UI)
        incidents = get_all_incidents(conn)
        st.dataframe(incidents, use_container_width=True)

        st.bar_chart(incidents['severity'].value_counts())



        # CREATE: Add new incident with a form
        with st.form("new_incident"):

            timestamp = st.date_input("Timestamp")
            #incident_id = st.text_input("Incident ID")
            severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
            description = st.text_input("Description")
            category = st.text_input("Catergory")

            submitted = st.form_submit_button("Add Incident")

        # When form is submitted
        if submitted :
            insert_incident(conn, timestamp, severity, category, status ,description)
            st.success("✓ Incident added successfully!")
            sleep(5)
            st.rerun()



        #To Delete an incident 
        with st.form("delete_incident"):
            delete = st.text_input("Enter Incident ID to Delete")
            submitted_for_deletion = st.form_submit_button("delete Incident")

        #when form is submitted 
        if submitted_for_deletion and delete:
            delete_incident(conn, delete)
            st.success("✓ Incident deleted successfully!")
            sleep(5)
            st.rerun()


        #To update an incident status
        with st.form("update_incident"):
            incident_id = st.text_input("Enter Incident ID to Update")
            new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved"])

            submitted_for_update = st.form_submit_button("Update Incident Status")

        #when form is submitted
        if submitted_for_update and incident_id:
            update_incident_status(conn, incident_id, new_status)
            st.success("✓ Incident status updated successfully!")
            sleep(5)
            st.rerun()

        #incident count by type
        st.subheader("Incident Count by Type")
        incident_type_count = get_incidents_by_type_count(conn)
        st.dataframe(incident_type_count, use_container_width=True)



        #High severity by status 
        st.subheader("High Severity Incidents by Status")
        high_severity_incidents = get_high_severity_by_status(conn)
        st.dataframe(high_severity_incidents, use_container_width=True)



        #incident types with mininum cases 
        st.subheader("Incident Types with Minimum Cases ")
        minimum_count = st.text_input("Enter Minimum Case Count","5")
        st.dataframe(get_incident_types_with_many_cases(conn, int(minimum_count)), use_container_width=True)



    with tab_tickets:

        # Page title
        st.title("It Tickets Dashboard")

        # READ: Display tickets in a beautiful table (Week 8 function + Streamlit UI)
        tickets = get_all_tickets(conn)
        st.dataframe(tickets, use_container_width=True)

        st.bar_chart(tickets['priority'].value_counts())


        # CREATE: Add new ticket with a form
        with st.form("new_ticket"):

            ticket_id = st.text_input("Ticket ID")
            priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
            description = st.text_input("Description")
            assigned_to = st.text_input("Assigned To")
            created_at = st.date_input("Created At")
            resolution_time_hours = st.number_input("Resolution Time (hours)", min_value=0)
        

            submitted = st.form_submit_button("Add Ticket")

        # When form is submitted
        if submitted and ticket_id:
            insert_ticket(conn, ticket_id, priority, description, status, assigned_to, created_at, resolution_time_hours)
            st.success("✓ Ticket added successfully!")
            sleep(5)
            st.rerun()



        #To Delete a ticket 
        with st.form("delete_ticket"):
            delete = st.text_input("Enter Ticket ID to Delete")
            submitted_for_deletion = st.form_submit_button("delete ticket")

        #when form is submitted 
        if submitted_for_deletion and delete:
            delete_ticket(conn, delete)
            st.success("✓ Ticket deleted successfully!")
            sleep(5)
            st.rerun()


        #To update a ticket's status
        with st.form("update_ticket"):
            ticket_id = st.text_input("Enter ticket ID to Update")
            new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved"])

            submitted_for_update = st.form_submit_button("Update Ticket Status")

        #when form is submitted
        if submitted_for_update and ticket_id:
            update_ticket_status(conn, ticket_id, new_status)
            st.success("✓ Ticket's status updated successfully!")
            sleep(5)
            st.rerun()



        #High priority ticket by status 
        st.subheader("High priority tickets by Status")
        high_priority_tickets = get_high_priority_tickets_by_status(conn)
        st.dataframe(high_priority_tickets, use_container_width=True)



    with tab_datasets:


        # Page title
        st.title("Datasets Metadata Dashboard")

        # READ: Display datasets in a beautiful table (Week 8 function + Streamlit UI)
        datasets = get_all_datasets(conn)
        st.dataframe(datasets, use_container_width=True)

        st.bar_chart(datasets['uploaded_by'].value_counts())




        # CREATE: Add new dataset with a form
        with st.form("new_dataset"):

            name = st.text_input("Name")
            dataset_id = st.text_input("Dataset ID")
            rows = st.number_input("Rows", min_value=0)
            columns = st.number_input("Columns", min_value=0)
            uploaded_by = st.text_input("Uploaded By")
            upload_date = st.date_input("Upload Date")

            submitted = st.form_submit_button("Add Dataset")

        # When form is submitted
        if submitted :
            insert_dataset(conn, dataset_id, name, rows, columns, uploaded_by, upload_date)
            st.success("✓ Dataset added successfully!")
            sleep(5)
            st.rerun()



        #To Delete a detaset
        with st.form("delete_dataset"):
            delete = st.text_input("Enter dataset ID to Delete")
            submitted_for_deletion = st.form_submit_button("delete dataset")

        #when form is submitted 
        if submitted_for_deletion and delete:
            delete_dataset(conn, delete)
            st.success("✓ Dataset deleted successfully!")
            sleep(5)
            st.rerun()



        #To update a dataset's number of rows
        with st.form("update_dataset"):
            dataset_id = st.text_input("Enter dataset ID to Update")
            new_num_rows = st.number_input("Enter new Rows value", min_value=0)

            submitted_for_update = st.form_submit_button("Update Dataset Number Of Rows")

        #when form is submitted
        if submitted_for_update and dataset_id:
            update_dataset_num_rows(conn, dataset_id, new_num_rows)
            st.success("✓ Dataset Number Of Rows Updated Successfully!")
            sleep(5)
            st.rerun()