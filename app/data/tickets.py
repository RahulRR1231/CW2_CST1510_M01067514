import pandas as pd




def insert_ticket(conn, ticket_id, priority, description, status , assigned_to, created_at, resolution_time_hours):
    """Insert new ticket."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO it_tickets
        (ticket_id, priority, description, status, assigned_to, created_at,resolution_time_hours)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (ticket_id, priority, description, status, assigned_to, created_at, resolution_time_hours))
    conn.commit()
    ticket_id = cursor.lastrowid
    return ticket_id

def get_all_tickets(conn):
    """Get all tickets as DataFrame."""
    df = pd.read_sql_query(
        "SELECT * FROM it_tickets ORDER BY ticket_id DESC",
        conn
    )
    return df



def update_ticket_status(conn, ticket_id, new_status):
    """
    Update the status of an ticket.

    TODO: Implement UPDATE operation.
    """
    # UPDATE SQL: UPDATE it_tickets SET status = ? WHERE id = ?
    update_sql = """
    UPDATE it_tickets
    SET status = ?
    WHERE ticket_id = ?
    """
    # TODO: Execute and commit
    cursor = conn.cursor()
    cursor.execute(update_sql, (new_status, ticket_id))
    conn.commit()
    # TODO: Return cursor.rowcount
    return cursor.rowcount



def delete_ticket(conn, ticket_id):
    """
    Delete a ticket from the database.

    TODO: Implement DELETE operation.
    """
    # DELETE SQL: DELETE FROM it_tickets WHERE id = ?
    delete_sql = """
    DELETE FROM it_tickets
    WHERE ticket_id = ?
    """
    # TODO: Execute and commit
    cursor = conn.cursor()
    cursor.execute(delete_sql, (ticket_id,))
    conn.commit()
    # TODO: Return cursor.rowcount
    return cursor.rowcount


'''
def get_tickets_by_type_count(conn):
    """
    Count tickets by type.
    Uses: SELECT, FROM, GROUP BY, ORDER BY
    """
    query = """
    SELECT ticket_type, COUNT(*) as count
    FROM it_tickets
    GROUP BY ticket_type
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn)
    return df'''

def get_high_priority_tickets_by_status(conn):
    """
    Count high severity tickets by status.
    Uses: SELECT, FROM, WHERE, GROUP BY, ORDER BY
    """
    query = """
    SELECT status, COUNT(*) as count
    FROM it_tickets
    WHERE priority = 'High'
    GROUP BY status
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn)
    return df





def get_tickets_types_with_many_cases(conn, min_count=5):
    """
    Find incident types with more than min_count cases.
    Uses: SELECT, FROM, GROUP BY, HAVING, ORDER BY
    """
    query = """
    SELECT ticket_type, COUNT(*) as count
    FROM it_tickets
    GROUP BY ticket_type
    HAVING COUNT(*) > ?
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn, params=(min_count,))
    return df



'''
# Test: Run analytical queries
conn = connect_database()

print("\n Incidents by Type:")
df_by_type = get_incidents_by_type_count(conn)
print(df_by_type)

print("\n High Severity Incidents by Status:")
df_high_severity = get_high_severity_by_status(conn)
print(df_high_severity)

print("\n Incident Types with Many Cases (>5):")
df_many_cases = get_incident_types_with_many_cases(conn, min_count=5)
print(df_many_cases)

conn.close()'''