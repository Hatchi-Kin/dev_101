from sqlite3 import Error

from .db_connector import SQLiteConnector
from .validator import validate_and_execute_query


def get_tables_in_db():
    with SQLiteConnector() as connector:
        result = connector.execute_query(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
        return [table[0] for table in result]


def print_schema_of_table(table_name):
    with SQLiteConnector() as connector:
        result = connector.execute_query(f"PRAGMA table_info({table_name});")
        print(f"\nSchema for table '{table_name}':")
        print("-" * 30)
        for column in result:
            name, type = column[1], column[2]
            print(f"{name:15} {type}")


def execute_query(query):
    try:
        with SQLiteConnector() as connector:
            result = connector.execute_query(query)
            return result
    except Error as e:
        return f"Erreur SQL : {e}"
    except Exception as e:
        return f"Erreur lors de l'exécution de la requête : {e}"

