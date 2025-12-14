# Project for module CST1510
Student Name: [Rahul Ramburrun]
Student ID: [M01067514]
Course: CST1510 -CW2 - Multi-Domain Intelligence Platform


# Week 7: Secure Authentication System
## Project Description
A command-line authentication system implementing secure password hashing
This system allows users to register accounts and log in with proper pass

## Features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data persistence

## Technical Implementation
- Hashing Algorithm: bcrypt with automatic salting
- Data Storage: Plain text file (`users.txt`) with comma-separated values
- Password Security: One-way hashing, no plaintext storage
- Validation: Username (3-20 alphanumeric characters), Password (6-50 characters)

# Week 8: Data Pipeline and CRUD
## Project Description
Created database tables for all three domains and implemented full CRUD (Create, Read, Update, Delete) functions

## Features
- Building the database file
- Checking that the CSV files and  information are successfully imported into the database
- Ensuring the database is properly configured and its integrity is maintained
- Confirming that all CRUD actions (Create, Read, Update, Delete) work as expected

## Technical Implementation
- Created database tables for the three domains(Cybersecurity,IT Operations and Data Science) and the user login system
- SQL Queries implementing CRUD functions in the 3 domains

# Note : To set up the database,run setupdatabase.py

# Week 9: Web Interface, MVC & Visualisation
## Project Description
Using streamlit to convert the Python scripts into interactive web program

## Features
- Structured web application consisting of three main pages, including a home page
- Secure login and registration system
- Dashboard and analytics page for all 3 domains
- Functionality for users to create, update, and delete data
- Graphical representation of the data in each domain
- Settings page that allows users to view their account information and to log out of their account

## Technical Implementation
- Utilization of session_state to maintain and persist data across multiple pages
- Restricted page access to non authenticated individuals

# Note : Access the web application by running the following command: py -m streamlit run my_app/Home.py 

# Week 10:  AI Integration
## Project Description
Development of AI assistants with the Gemini 2.5 Flash model, featuring domain-specific access and behavior.

## Features
- A specialized webpage designed for the AI assistant
- Three distinct tabs, each representing one of the domains
- Features that let users submit questions specific to each domain
- The AI assistant provides answers tailored to the expertise defined for that domain

## Technical Implementation

- Loaded data for the three domains from the database
- Converting data into a string format and storing it in history

