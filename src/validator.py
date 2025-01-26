import hashlib
from typing import Union, List, Any

from .db_connector import SQLiteConnector
from .query_hashes import ALLOWED_QUERY_HASHES


def hash_query(query):
    return hashlib.sha256(query.lower().strip().encode()).hexdigest()


def is_modification_query(query: str) -> bool:
    """Check if query modifies the database."""
    query = query.lower().strip()
    return any(query.startswith(word) for word in ["insert", "update", "delete"])


def validate_and_execute_query(query: str, function_name: str) -> Union[str, List[Any]]:
    """Generic query validator and executor"""
    hashed_query = hash_query(query)
    if hashed_query not in ALLOWED_QUERY_HASHES[function_name]:
        return "Invalid query"

    with SQLiteConnector() as connector:
        result = connector.execute_query(query)
        if is_modification_query(query):
            return "Success!"
        return result if result else []
