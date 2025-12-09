from pathlib import Path
import pandas as pd


def insert_dataset(conn, dataset_id, name, rows,columns,uploaded_by, upload_date):
    """Insert new dataset."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datasets_metadata
        ( dataset_id, name, rows, columns, uploaded_by, upload_date)
        VALUES (?, ?, ?, ?, ?,?)
    """, ( dataset_id, name, rows, columns, uploaded_by, upload_date))
    conn.commit()
    return cursor.lastrowid
    

def get_all_datasets(conn):
    """Get all metadata as DataFrame."""
    df = pd.read_sql_query(
        "SELECT * FROM datasets_metadata ORDER BY dataset_id DESC",
        conn
    )
    return df


def delete_dataset(conn, dataset_id):
    """
    Delete an incident from the database.

    TODO: Implement DELETE operation.
    """
    # TODO: Write DELETE SQL: DELETE FROM datasets_metadata WHERE dataset_id = ?
    delete_sql = """
    DELETE FROM datasets_metadata
    WHERE dataset_id = ?
    """
    # TODO: Execute and commit
    cursor = conn.cursor()
    cursor.execute(delete_sql, (dataset_id,))
    conn.commit()
    # TODO: Return cursor.rowcount
    return cursor.rowcount

def update_dataset_num_rows(conn, incident_id, new_row):
    """
    Update the rows of a dataset.

    TODO: Implement UPDATE operation.
    """
    # TODO: Write UPDATE SQL: UPDATE datasets_metadata SET rows = ? WHERE dataset_id = ?
    update_sql = """
    UPDATE datasets_metadata
    SET rows = ?
    WHERE dataset_id = ?
    """
    # TODO: Execute and commit
    cursor = conn.cursor()
    cursor.execute(update_sql, (new_row, incident_id))
    conn.commit()
    # TODO: Return cursor.rowcount
    return cursor.rowcount













def load_csv_to_table(conn, csv_path, table_name):
    csv_path = Path(csv_path)

    #TODO: Implement this function.


    # TODO: Check if CSV file exists
    if not csv_path.exists():
        print(f"⚠️  File not found: {csv_path}")
        return 0
    # TODO: Read CSV using pandas.read_csv()
    import pandas as pd
    df = pd.read_csv(csv_path)
   
    # TODO: Use df.to_sql() to insert data
    # Parameters: name=table_name, con=conn, if_exists='append', index=False
    df.to_sql(name=table_name, con=conn, if_exists='append', index=False)
    # TODO: Print success message and return row count
    row_count = len(df)
    print(f"✅ Loaded {row_count} rows into '{table_name}' from '{csv_path}'")
    return row_count
    





def load_all_csv_data(conn):
    total_rows = 0
    print("\nLoading Cyber Incident data into database...\nLoading Datasets Metadata into database...\nLoading It Tickets data into database...\n")
    total_rows = load_csv_to_table(conn, "DATA/cyber_incidents.csv", "cyber_incidents") +load_csv_to_table(conn, "DATA/it_tickets.csv", "it_tickets")+load_csv_to_table(conn, "DATA/datasets_metadata.csv", "datasets_metadata")
    


    return total_rows


