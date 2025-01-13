from database.db_connection import get_connection
from database.models import Application

class ApplicationRepository:
    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM applications")
        rows = cursor.fetchall()
        conn.close()
        return [Application(**row) for row in rows]

    def get_by_id(self, app_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM applications WHERE id = ?", (app_id,))
        row = cursor.fetchone()
        conn.close()
        return Application(**row) if row else None

    def add(self, application):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO applications (app_name, app_link, icon_link, description)
            VALUES (?, ?, ?, ?)
        """, (application.app_name, application.app_link, application.icon_link, application.description))
        conn.commit()
        conn.close()

    def delete(self, app_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM applications WHERE id = ?", (app_id,))
        conn.commit()
        conn.close()
