import sqlite3


class Connection_Closure:
    def __init__(self):
        self.connect = sqlite3.connect('Users_Bot70.db')
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()


class Database(Connection_Closure):
    def __init__(self):
        super().__init__()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS User(
                        id INTEGER PRIMARY KEY,
                        user_name TEXT,
                        genre INTEGER,
                        characters TEXT,
                        locations TEXT,
                        additionally TEXT,
                        spent_tokens INTEGER,
                        content TEXT,
                        tokens INTEGER,
                        session_id INTEGER)""")
        self.connect.commit()

    def check_user_exists(self, id, user_name):
        self.cursor.execute(
            "SELECT id, user_name FROM User "
            "WHERE id = ? "
            "OR user_name = ? ",
            (id, user_name))
        data = self.cursor.fetchone()
        return data is not None

    def add_user(self, id, user_name):
        self.cursor.execute("INSERT INTO User VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                            (id, user_name, '', '', '', '', 0, '', 300, 2))
        self.connect.commit()


class spent_tokens_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def spent_tokens(self, id):
        self.cursor.execute(f"SELECT spent_tokens FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class session_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt5(self, id):
        self.cursor.execute(f"SELECT session_id FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class spent_tokens_add(Connection_Closure):
    def __init__(self):
        super().__init__()

    def spent(self, id):
        self.cursor.execute("SELECT id, spent_tokens FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_spent(self, promt, user_id):
        self.cursor.execute("UPDATE User SET spent_tokens = ? WHERE id = ?", (promt, user_id))
        self.connect.commit()


class session(Connection_Closure):
    def __init__(self):
        super().__init__()

    def session1(self, id):
        self.cursor.execute("SELECT id, session_id FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_session(self, promt, user_id):
        self.cursor.execute("UPDATE User SET session_id = ? WHERE id = ?", (promt, user_id))
        self.connect.commit()


class tok_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt5(self, id):
        self.cursor.execute(f"SELECT tokens FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class CONTROL(Connection_Closure):
    def __init__(self):
        super().__init__()

    def tokens(self, id):
        self.cursor.execute("SELECT id, tokens FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_tokens(self, promt, user_id):
        self.cursor.execute("UPDATE User SET tokens = ? WHERE id = ?", (promt, user_id))
        self.connect.commit()


class content_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt5(self, id):
        self.cursor.execute(f"SELECT content FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class Add_content(Connection_Closure):
    def __init__(self):
        super().__init__()

    def content(self, id):
        self.cursor.execute("SELECT id, content FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_content(self, promt, user_id):
        self.cursor.execute("UPDATE User SET content = ? WHERE id = ?", (promt, user_id))
        self.connect.commit()


class additionally_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt4(self, id):
        self.cursor.execute(f"SELECT additionally FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class Genre_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt1(self, id):
        self.cursor.execute(f"SELECT genre FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class Characters_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt2(self, id):
        self.cursor.execute(f"SELECT characters FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class Additionally(Connection_Closure):
    def __init__(self):
        super().__init__()

    def additionally(self, id):
        self.cursor.execute("SELECT id, additionally FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_additionally(self, characters, user_id):
        self.cursor.execute("UPDATE User SET additionally = ? WHERE id = ?", (characters, user_id))
        self.connect.commit()


class Locations_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt3(self, id):
        self.cursor.execute(f"SELECT locations FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class Genre(Connection_Closure):
    def __init__(self):
        super().__init__()

    def Genre(self, id):
        self.cursor.execute("SELECT id, genre FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_Genre(self, genre, user_id):
        self.cursor.execute("UPDATE User SET genre = ? WHERE id = ?", (genre, user_id))
        self.connect.commit()


class Characters(Connection_Closure):
    def __init__(self):
        super().__init__()

    def characters(self, id):
        self.cursor.execute("SELECT id, characters FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_characters(self, characters, user_id):
        self.cursor.execute("UPDATE User SET characters = ? WHERE id = ?", (characters, user_id))
        self.connect.commit()


class Locations(Connection_Closure):
    def __init__(self):
        super().__init__()

    def locations(self, id):
        self.cursor.execute("SELECT id, locations FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_locations(self, genre, user_id):
        self.cursor.execute("UPDATE User SET locations = ? WHERE id = ?", (genre, user_id))
        self.connect.commit()
