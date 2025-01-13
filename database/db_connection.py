import sqlite3

def get_connection():
    conn = sqlite3.connect("applications.db")
    conn.row_factory = sqlite3.Row  # Permite acessar os resultados por nomes de coluna
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_name TEXT NOT NULL,
            app_link TEXT NOT NULL,
            icon_link TEXT NOT NULL,
            description TEXT
        );
    """)
    conn.commit()
    conn.close()
