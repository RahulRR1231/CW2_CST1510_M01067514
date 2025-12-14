import pandas as pd




def insert_ticket(conn, priority, description, status , assigned_to, created_at, resolution_time_hours):
    """Insert new ticket."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO it_tickets
        ( priority, description, status, assigned_to, created_at,resolution_time_hours)
        VALUES ( ?, ?, ?, ?, ?, ?)
    """, ( priority, description, status, assigned_to, created_at, resolution_time_hours))
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

    """
    # UPDATE SQL
    update_sql = """
    UPDATE it_tickets
    SET status = ?
    WHERE ticket_id = ?
    """
    # Execute and commit
    cursor = conn.cursor()
    cursor.execute(update_sql, (new_status, ticket_id))
    conn.commit()

    # Return cursor.rowcount
    return cursor.rowcount



def delete_ticket(conn, ticket_id):
    """
    Delete a ticket from the database.

    """
    # DELETE SQL
    delete_sql = """
    DELETE FROM it_tickets
    WHERE ticket_id = ?
    """
    # Execute and commit
    cursor = conn.cursor()
    cursor.execute(delete_sql, (ticket_id,))
    conn.commit()

    # Return cursor.rowcount
    return cursor.rowcount



def get_high_priority_tickets_by_status(conn):
    """
    Count high severity tickets by status.
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






