import streamlit as st
from google import genai
from app.data.incidents import get_all_incidents
from app.data.db import connect_database
from app.data.tickets import get_all_tickets
from app.data.datasets import get_all_datasets


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Redirect to login if not logged in
if not st.session_state.logged_in:
    st.error("Please log in to access the dashboard.")
    if st.button("Go to Login Page"):
       st.switch_page("Home.py")
       st.stop()
else:

    # -------------------------
    # PAGE CONFIG
    # -------------------------
    st.set_page_config(
        page_title="AI Assistants Hub",
        page_icon="🤖",
        layout="wide"
    )

    # -------------------------
    # TABS
    # -------------------------
    tab_Cybersecurity_AI_Assistant, tab_IT_Operation_AI_Assistant, tab_Data_Science_AI_Assistant = st.tabs(
        ["Cybersecurity AI Assistant", "IT Operation AI Assistant", "Data Science AI Assistant"]
    )

    # -------------------------
    # GEMINI CLIENT (ONE INSTANCE)
    # -------------------------
    client = genai.Client(api_key=st.secrets["API_KEY"])

    # -------------------------
    # CYBERSECURITY TAB
    # -------------------------
    with tab_Cybersecurity_AI_Assistant:

        st.title("🛡 Cybersecurity AI Assistant")
        st.caption("Powered by Gemini 2.5 Flash")

        system_prompt_cyber = """You are a cybersecurity expert assistant.
        - Analyze incidents and threats
        - Provide technical guidance
        - Explain attack vectors and mitigations
        - Use standard terminology (MITRE ATT&CK, CVE)
        - Prioritize actionable recommendations
        Tone: Professional, technical
        Format: Clear, structured responses"""

        if "messages_cyber" not in st.session_state:
            st.session_state.messages_cyber = [{"role": "system", "content": system_prompt_cyber}]

        # Sidebar controls
        with st.sidebar.expander("Cybersecurity Chat Controls", expanded=True):
            st.subheader("Cybersecurity Chat Controls")
            message_count = len([m for m in st.session_state.messages_cyber if m["role"] != "system"])
            st.metric("Messages", message_count)
            if st.button("🗑 Clear Chat", key="clear_chat_cyber"):
                st.session_state.messages_cyber = [{"role": "system", "content": system_prompt_cyber}]
            temperature = st.slider("Temperature", 0.0, 2.0, 1.0, 0.1, key="temp_cyber")

        # Chat container
        chat_container = st.container()
        for message in st.session_state.messages_cyber:
            if message["role"] != "system":
                with chat_container.chat_message(message["role"]):
                    st.markdown(message["content"])

        # User input at the bottom
        prompt = st.chat_input("Say something...", key="chat_input_cyber")
        if prompt:
            with chat_container.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages_cyber.append({"role": "user", "content": prompt})

            # ----------------------------------------------------------
            # ✅ MINIMAL ADDITION: Load incident data for the API
            # ----------------------------------------------------------
            try:
                conn = connect_database()  # your DB connection function
                incidents_df = get_all_incidents(conn)
                incidents_text = incidents_df.to_string(index=False)
            except:
                incidents_text = "No incident data available."
            # ----------------------------------------------------------

            contents = [system_prompt_cyber] + [
                f"{msg['role'].capitalize()}: {msg['content']}"
                for msg in st.session_state.messages_cyber
                if msg["role"] != "system"
            ] + [
                # ------------------------------------------------------
                # ✅ MINIMAL ADDITION: Attach incident data to model input
                # ------------------------------------------------------
                f"Incident Database:\n{incidents_text}"
            ]

            with st.spinner("Thinking..."):
                response = client.models.generate_content_stream(
                    model="gemini-2.5-flash",
                    contents=contents
                )

                full_reply = ""
                with chat_container.chat_message("assistant"):
                    container = st.empty()
                    for chunk in response:
                        if chunk.text:
                            full_reply += chunk.text
                            container.markdown(full_reply + "▌")
                    container.markdown(full_reply)

            st.session_state.messages_cyber.append({"role": "assistant", "content": full_reply})


    # -------------------------
    # IT OPERATIONS TAB
    # -------------------------
    with tab_IT_Operation_AI_Assistant:

        st.title("🖥 IT Operations AI Assistant")
        st.caption("Powered by Gemini 2.5 Flash")

        system_prompt_it = """You are an IT Operations expert assistant.
        - Help troubleshoot IT issues
        - Optimize system performance
        - Manage tickets
        - Use standard terminology
        - Prioritize actionable recommendations
        Tone: Professional, technical
        Format: Clear, structured responses"""

        if "messages_it" not in st.session_state:
            st.session_state.messages_it = [{"role": "system", "content": system_prompt_it}]

        # Sidebar
        with st.sidebar.expander("IT Operations Chat Controls", expanded=True):
            st.subheader("IT Operations Chat Controls")
            message_count = len([m for m in st.session_state.messages_it if m["role"] != "system"])
            st.metric("Messages", message_count)
            if st.button("🗑 Clear Chat", key="clear_chat_it"):
                st.session_state.messages_it = [{"role": "system", "content": system_prompt_it}]
            temperature = st.slider("Temperature", 0.0, 2.0, 1.0, 0.1, key="temp_it")

        # Chat container
        chat_container = st.container()
        for message in st.session_state.messages_it:
            if message["role"] != "system":
                with chat_container.chat_message(message["role"]):
                    st.markdown(message["content"])

        # User input
        prompt = st.chat_input("Say something...", key="chat_input_it")
        if prompt:
            with chat_container.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages_it.append({"role": "user", "content": prompt})

            try:
                conn = connect_database()  # your DB connection function
                incidents_df = get_all_tickets(conn)
                tickets_text = incidents_df.to_string(index=False)
            except:
                tickets_text = "No ticket data available."
            

            contents = [system_prompt_it] + [
                f"{msg['role'].capitalize()}: {msg['content']}"
                for msg in st.session_state.messages_it
                if msg["role"] != "system"
            ] + [
                f"IT Ticket Database:\n{tickets_text}"
            ]



            with st.spinner("Thinking..."):
                response = client.models.generate_content_stream(
                    model="gemini-2.5-flash",
                    contents=contents
                )

                full_reply = ""
                with chat_container.chat_message("assistant"):
                    container = st.empty()
                    for chunk in response:
                        if chunk.text:
                            full_reply += chunk.text
                            container.markdown(full_reply + "▌")
                    container.markdown(full_reply)

            st.session_state.messages_it.append({"role": "assistant", "content": full_reply})

    # -------------------------
    # DATA SCIENCE TAB
    # -------------------------
    with tab_Data_Science_AI_Assistant:

        st.title("📊 Data Science AI Assistant")
        st.caption("Powered by Gemini 2.5 Flash")

        system_prompt_ds = """You are a Data Science expert assistant.
        - Help with analysis, visualization, and statistical insights.
        - Provide technical guidance
        - Use standard terminology
        - Prioritize actionable recommendations
        Tone: Professional, technical
        Format: Clear, structured responses"""

        if "messages_ds" not in st.session_state:
            st.session_state.messages_ds = [{"role": "system", "content": system_prompt_ds}]

        # Sidebar
        with st.sidebar.expander("Data Science Chat Controls", expanded=True):
            st.subheader("Data Science Chat Controls")
            message_count = len([m for m in st.session_state.messages_ds if m["role"] != "system"])
            st.metric("Messages", message_count)
            if st.button("🗑 Clear Chat", key="clear_chat_ds"):
                st.session_state.messages_ds = [{"role": "system", "content": system_prompt_ds}]
            temperature = st.slider("Temperature", 0.0, 2.0, 1.0, 0.1, key="temp_ds")

        # Chat container
        chat_container = st.container()
        for message in st.session_state.messages_ds:
            if message["role"] != "system":
                with chat_container.chat_message(message["role"]):
                    st.markdown(message["content"])

        # User input
        prompt = st.chat_input("Say something...", key="chat_input_ds")
        if prompt:
            with chat_container.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages_ds.append({"role": "user", "content": prompt})

            try:
                conn = connect_database()  # your DB connection function
                datasets_df = get_all_datasets(conn)
                datasets_text = datasets_df.to_string(index=False)
            except:
                datasets_text = "No dataset data available."
            

            contents = [system_prompt_ds] + [
                f"{msg['role'].capitalize()}: {msg['content']}"
                for msg in st.session_state.messages_ds
                if msg["role"] != "system"
            ]+[
                f"Datasets Metadata Database:\n{datasets_text}"
            ]

            with st.spinner("Thinking..."):
                response = client.models.generate_content_stream(
                    model="gemini-2.5-flash",
                    contents=contents
                )

                full_reply = ""
                with chat_container.chat_message("assistant"):
                    container = st.empty()
                    for chunk in response:
                        if chunk.text:
                            full_reply += chunk.text
                            container.markdown(full_reply + "▌")
                    container.markdown(full_reply)

            st.session_state.messages_ds.append({"role": "assistant", "content": full_reply})



