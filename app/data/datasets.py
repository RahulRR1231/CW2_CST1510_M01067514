def load_csv_to_table(conn, csv_path, table_name):
    

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
    