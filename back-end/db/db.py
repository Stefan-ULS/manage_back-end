import sqlite3

class SQLiteDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to the databaseL {e}")
            return False
        
    def create_table(self, table_name, **kwargs):
        try:
            cursor = self.conn.cursor()

            # Construct the SQL statement with column names and data types
            columns_and_types = ', '.join([f'{column_name} {column_spec}' for column_name, column_spec in kwargs.items()])

            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_and_types})")
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            return False
        
    def insert_data(self, table_name, **kwargs):
        try:
            cursor = self.conn.cursor()
            column_name = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' * len(kwargs))
            values = tuple(kwargs.values())

            query = f"INSERT INTO {table_name} ({column_name}) VALUES ({placeholders})"

            cursor.execute(query, values)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f'Error inserting data: {e}')
            return False
        
    def execute_query(self, query, *parameters):
        try:
            cursor = self.conn.cursor()
            # Check if any parameters are provided
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Error executing query: {e}')
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            return True
        return False



# Step 1: Create a connection to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('db.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Perform database operations
# For example, creating a table and inserting data:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        email TEXT,
        phone TEXT,
        password_hash TEXT
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Step 4: Commit the changes (for data modification operations)
conn.commit()

# Step 5: Close the cursor and the database connection
cursor.close()
conn.close()
