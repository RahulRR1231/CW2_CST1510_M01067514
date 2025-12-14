def create_users_table(conn):
    #Creates users table.

    # Get a cursor from the connection
    cursor = conn.cursor()

    # SQL statement to create users table if it does not exist
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    # Executes the SQL statement
    cursor.execute(create_table_sql)

    # Commits the changes
    conn.commit()

    # Prints success message
    print("✅ Users table created successfully!")



def create_cyber_incidents_table(conn):

    #Create cyber_incidents table.

    #  Get a cursor from the connection
    cursor = conn.cursor()

    # Creates table if it does not exist
    # SQL statement to create cyber_incidents table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS cyber_incidents (
        incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        severity TEXT,
        category TEXT,
        status TEXT,
        description TEXT
    )
    """

   
    # Executes the SQL statement
    cursor.execute(create_table_sql)

    # Commits the changes
    conn.commit()

    # Prints success message
    print("✅ cyber_incidents table created successfully!")
    



def create_datasets_metadata_table(conn):
    
    #Creates the datasets_metadata table.

    # Get a cursor from the connection
    cursor= conn.cursor()

    # Creates table if it does not exist
    # SQL statement to create datasets metadata table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS datasets_metadata (
        dataset_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rows TEXT,
        columns TEXT,
        uploaded_by TEXT,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_sql)
    conn.commit()
    print("✅ datasets_metadata table created successfully!")
    pass



def create_it_tickets_table(conn):


    #Creates the it_tickets table.

   
    cursor = conn.cursor()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS it_tickets (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        priority TEXT,
        description TEXT,
        status TEXT,
        assigned_to TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        resolution_time_hours INTEGER
    )
    """
    #Executes the SQL statement
    cursor.execute(create_table_sql)

    #commits the changes
    conn.commit()

    # prints success message
    print("✅ it_tickets table created successfully!")
    pass




def create_all_tables(conn):

    #Creates all tables.

    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)




   