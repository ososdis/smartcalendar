import sqlite3


class AbstractDAO:

    def __init__(self, db_name="database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_by_id(self, table, obj_id):
        query = f"SELECT * FROM {table} WHERE id = ?"

        self.cursor.execute(query, (obj_id,))

        return self.cursor.fetchone()

    def get_all(self, table):
        query = f"SELECT * FROM {table}"

        self.cursor.execute(query)

        return self.cursor.fetchall()

    def save(self):
        self.connection.commit()

    def delete(self, table, obj_id):
        query = f"DELETE FROM {table} WHERE id = ?"

        self.cursor.execute(query, (obj_id,))

        self.connection.commit()

    def close(self):
        self.connection.close()


class UserDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

    def create_table(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                email TEXT UNIQUE,
                google_linked BOOLEAN
            )
            """
        )

        self.connection.commit()

    def insert_user(self, role, email, google_linked):

        self.cursor.execute(
            """
            INSERT INTO users(role, email, google_linked)
            VALUES (?, ?, ?)
            """,
            (role, email, google_linked)
        )

        self.connection.commit()

    def get_by_email(self, email):

        self.cursor.execute(
            """
            SELECT * FROM users
            WHERE email = ?
            """,
            (email,)
        )

        return self.cursor.fetchone()

    def update_tokens(self, user_id, token):

        self.cursor.execute(
            """
            ALTER TABLE users
            ADD COLUMN token TEXT
            """
        )

        self.cursor.execute(
            """
            UPDATE users
            SET token = ?
            WHERE id = ?
            """,
            (token, user_id)
        )

        self.connection.commit()

    def get_user_by_id(self, user_id):

        return self.get_by_id("users", user_id)

    def get_all_users(self):

        return self.get_all("users")

    def delete_user(self, user_id):

        self.delete("users", user_id)


class EventDAO(AbstractDAO):

    def __init__(self):
        super().__init__()

    def create_table(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER,
                title TEXT,
                date_event TEXT,
                start_time TEXT,
                end_time TEXT,
                salle TEXT,
                teacher_sign TEXT
            )
            """
        )

        self.connection.commit()

    def insert_event(
        self,
        course_id,
        title,
        date_event,
        start_time,
        end_time,
        salle
    ):

        self.cursor.execute(
            """
            INSERT INTO events(
                course_id,
                title,
                date_event,
                start_time,
                end_time,
                salle
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                course_id,
                title,
                date_event,
                start_time,
                end_time,
                salle
            )
        )

        self.connection.commit()

    def get_my_courses(self, course_id):

        self.cursor.execute(
            """
            SELECT * FROM events
            WHERE course_id = ?
            """,
            (course_id,)
        )

        return self.cursor.fetchall()

    def get_by_date(self, date_event):

        self.cursor.execute(
            """
            SELECT * FROM events
            WHERE date_event = ?
            """,
            (date_event,)
        )

        return self.cursor.fetchall()

    def update_sign(self, event_id, sign):

        self.cursor.execute(
            """
            UPDATE events
            SET teacher_sign = ?
            WHERE id = ?
            """,
            (sign, event_id)
        )

        self.connection.commit()

    def get_event_by_id(self, event_id):

        return self.get_by_id("events", event_id)

    def get_all_events(self):

        return self.get_all("events")

    def delete_event(self, event_id):

        self.delete("events", event_id)


if __name__ == "__main__":

    userDAO = UserDAO()

    userDAO.create_table()

    userDAO.insert_user(
        role="admin",
        email="admin@gmail.com",
        google_linked=True
    )

    print(userDAO.get_all_users())

    print(userDAO.get_by_email("admin@gmail.com"))

    eventDAO = EventDAO()

    eventDAO.create_table()

    eventDAO.insert_event(
        course_id=1,
        title="Cours Automatique",
        date_event="2026-05-23",
        start_time="08:00",
        end_time="10:00",
        salle="B12"
    )

    print(eventDAO.get_all_events())

    print(eventDAO.get_by_date("2026-05-23"))
