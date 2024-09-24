import pyodbc

# Function to connect to the SQL Server
def connect_db():
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=your_server_name;'
        'Database=LibraryDB;'
        'Trusted_Connection=yes;'
    )
    return conn
