import sqlite3
import pandas as pd

def perform_data_quality_checks(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    print("Database connection successful.")

    # Check tables
    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
    print("Tables in database:", tables)

    # Verify table existence
    table_check = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table' AND name='tmdb_5000_movies'", conn)
    if table_check.empty:
        print("Table 'tmdb_5000_movies' does not exist.")
        return

    # Perform data quality check
    missing_values_check = pd.read_sql_query("SELECT * FROM tmdb_5000_movies WHERE title IS NULL OR revenue IS NULL", conn)
    if not missing_values_check.empty:
        c.execute('''
            INSERT INTO data_quality_checks (check_name, description, status)
            VALUES (?, ?, ?)
        ''', ('Missing Values Check', 'Check for missing values in title and revenue columns in tmdb_5000_movies table', 'Failed'))
    else:
        c.execute('''
            INSERT INTO data_quality_checks (check_name, description, status)
            VALUES (?, ?, ?)
        ''', ('Missing Values Check', 'Check for missing values in title and revenue columns in tmdb_5000_movies table', 'Passed'))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_file = r'C:\Users\shree\data_quality.db'
    perform_data_quality_checks(db_file)


