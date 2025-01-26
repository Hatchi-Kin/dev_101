import os
import sqlite3
from datetime import datetime, timedelta

def get_database_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))
    sqlite_dir = os.path.join(project_root, "sqlite")
    os.makedirs(sqlite_dir, exist_ok=True)
    db_path = os.path.join(sqlite_dir, "library.db")
    return db_path

def create_database():
    db_path = get_database_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create authors table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """
    )

    # Create books table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        )
    """
    )

    # Create users table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """
    )

    # Create borrowings table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS borrowings (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT NOT NULL,
            return_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (book_id) REFERENCES books (id),
            UNIQUE (user_id, return_date) -- Ensure a user can only borrow one book at a time
        )
    """
    )

    # Create indexes for performance
    c.execute("""CREATE INDEX IF NOT EXISTS idx_author_id ON books(author_id)""")
    c.execute("""CREATE INDEX IF NOT EXISTS idx_user_id ON borrowings(user_id)""")
    c.execute("""CREATE INDEX IF NOT EXISTS idx_book_id ON borrowings(book_id)""")

    # Initial data
    authors = [
        (1, "Victor Hugo"),
        (2, "Jules Verne"),
        (3, "Albert Camus"),
        (4, "Gustave Flaubert"),
        (5, "Emile Zola"),
        (6, "Guy de Maupassant"),
        (7, "Alphonse Daudet"),
        (8, "Stendhal"),
        (9, "Balzac"),
        (10, "Voltaire"),
        (11, "Simone de Beauvoir"),
        (12, "Karl Marx"),
    ]

    books = [
        (1, "Les Misérables", 1),
        (2, "Les Contemplations", 1),
        (3, "L'Étranger", 3),
        (4, "Le Tour du monde en 80 jours", 2),
        (5, "Madame Bovary", 4),
        (6, "Vingt mille lieues sous les mers", 2),
        (7, "La Peste", 3),
        (8, "Nana", 5),
        (9, "Bel-Ami", 6),
        (10, "Tartarin de Tarascon", 7),
        (11, "Le Rouge et le Noir", 8),
        (12, "Père Goriot", 9),
        (13, "Candide", 10),
        (14, "Les Chouans", 1),
        (15, "Michel Strogoff", 2),
        (16, "L'Avenir de la science", 3),
        (17, "Salammbô", 4),
        (18, "Une vie", 5),
        (19, "Contes du jour et de la nuit", 6),
        (20, "Fromont jeune et Risler aîné", 7),
        (21, "L'invitée", 11),
        (22, "Les Mandarins", 11),
        (23, "Le Deuxième Sexe", 11),
        (24, "Les Bouches inutiles", 11),
        (1867, "Le Capital", 12),
    ]

    users = [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (4, "David"),
        (5, "Eve"),
        (6, "Frank"),
        (7, "Grace"),
        (8, "Heidi"),
        (9, "Ivan"),
    ]

    # Borrowings data
    now = datetime.now()
    borrowings = [
        (1, 1, 1, (now - timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S"), (now - timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S")),  # Alice borrowed and returned "Les Misérables"
        (2, 2, 2, (now - timedelta(days=17)).strftime("%Y-%m-%d %H:%M:%S"), None),  # Bob borrowed "Le Tour du monde en 80 jours" and hasn't returned it
        (3, 3, 3, (now - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"), (now - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")),  # Charlie borrowed and returned "L'Étranger"
        (4, 4, 4, (now - timedelta(days=6)).strftime("%Y-%m-%d %H:%M:%S"), None),  # David borrowed "Les Contemplations" and hasn't returned it
        (5, 5, 5, (now - timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S"), None),  # Eve borrowed "Madame Bovary" and hasn't returned it
    ]

    # Use an explicit transaction
    with conn:
        c.executemany("INSERT OR IGNORE INTO authors VALUES (?,?)", authors)
        c.executemany("INSERT OR IGNORE INTO books VALUES (?,?,?)", books)
        c.executemany("INSERT OR IGNORE INTO users VALUES (?,?)", users)
        c.executemany("INSERT OR IGNORE INTO borrowings VALUES (?,?,?,?,?)", borrowings)

    conn.close()


####################
# appellez la fonction create_database pour créer la base de données et exécutez le script.