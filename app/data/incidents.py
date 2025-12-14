import pandas as pd


def insert_incident(conn, timestamp, severity, category, status, description):
    """Insert new incident."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cyber_incidents
        ( timestamp, severity, category, status, description)
        VALUES ( ?, ?, ?, ?, ?)
    """, ( timestamp, severity, category, status, description))
    conn.commit()
    return cursor.lastrowid
    

def get_all_incidents(conn):
    """Get all incidents as DataFrame."""
    df = pd.read_sql_query(
        "SELECT * FROM cyber_incidents ORDER BY incident_id DESC",
        conn
    )
    return df



def update_incident_status(conn, incident_id, new_status):
    """
    Update the status of an incident.
    """
    # UPDATE SQL
    update_sql = """
    UPDATE cyber_incidents
    SET status = ?
    WHERE incident_id = ?
    """
    # Execute and commit
    cursor = conn.cursor()
    cursor.execute(update_sql, (new_status, incident_id))
    conn.commit()

    # Return cursor.rowcount
    return cursor.rowcount



def delete_incident(conn, incident_id):
    """
    Delete an incident from the database.
    """
    # DELETE SQL
    delete_sql = """
    DELETE FROM cyber_incidents
    WHERE incident_id = ?
    """

    # Execute and commit
    cursor = conn.cursor()
    cursor.execute(delete_sql, (incident_id,))
    conn.commit()

    # Return cursor.rowcount
    return cursor.rowcount



def get_incidents_by_type_count(conn):
    """
    Count incidents by type.
    """
    query = """
    SELECT category, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY category
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn)
    return df

def get_high_severity_by_status(conn):
    """
    Count high severity incidents by status.
    """
    query = """
    SELECT status, COUNT(*) as count
    FROM cyber_incidents
    WHERE severity = 'High'
    GROUP BY status
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn)
    return df

def get_incident_types_with_many_cases(conn, min_count=5):
    """
    Find incident types with more than min_count cases.
    """
    query = """
    SELECT category, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY category
    HAVING COUNT(*) > ?
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn, params=(min_count,))
    return df

