import sqlite3
from pathlib import Path


class SQLiteConnector:
    def __init__(self):
        project_root = Path(__file__).parent.parent

        db_dir = project_root / "sqlite"
        db_dir.mkdir(exist_ok=True)

        self.db_path = db_dir / "library.db"
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish connection to SQLite database"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return False

    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=None):
        """Execute SQL query and return results"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def __enter__(self):
        """Context manager entry"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.disconnect()
