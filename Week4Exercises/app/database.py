import sqlite3
from contextlib import contextmanager
from typing import List, Union

from security import hash_password, get_session

DEFAULT_USER = "cryptonator"
DEFAULT_PASSWORD = DEFAULT_USER
DEFAULT_SECRET = hash_password(DEFAULT_PASSWORD)

ADMIN_USER = "admin"
ADMIN_SECRET = "6b337775fce2301772f36e05a10ed9822033a7496520cf24ebe13ed324262c99"

c_users = f'''CREATE TABLE if not exists USERS(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    role INTEGER NOT NULL, -- 0 is normal user, 1 is admin
    secret TEXT NOT NULL
);'''
c_insert_user = '''INSERT INTO USERS (username, role, secret) VALUES (?, ?, ?)'''  # Secure insert


class User:
    def __init__(self, username: str = "", role: int = 0):
        self.username: str = username
        self.role: int = role


class DB:
    database = "database.db"

    def __init__(self, app):
        self.app = app
        self.logger = app.logger
        self.logger.info("Initializing database...")
        self.db = sqlite3.connect(self.database, check_same_thread=False)
        self.cursor = self.db.cursor()
        # Create users table if not exist
        with self.transaction():
            self.cursor.execute(c_users)
        res1 = self._is_user(DEFAULT_USER, DEFAULT_SECRET)
        res2 = self._is_user(ADMIN_USER, ADMIN_SECRET)
        if not res1:
            self.logger.info(f"Inserting default guest user... {DEFAULT_USER}")
            with self.transaction():
                self.cursor.execute(c_insert_user, (DEFAULT_USER, 0, DEFAULT_SECRET))
        if not res2:
            self.logger.info(f"Inserting default admin user... {ADMIN_USER}")
            with self.transaction():
                self.cursor.execute(c_insert_user, (ADMIN_USER, 1, ADMIN_SECRET))

    def __del__(self):
        self.cursor.close()

    def query_db(self, query, args=(), one=False) -> Union[sqlite3.Row, List[sqlite3.Row]]:
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return (rows[0] if rows else None) if one else rows

    def _is_user(self, username: str, password: str) -> sqlite3.Row:
        return self.query_db("select count(*) from USERS where username = ? and secret = ?", (username, password),
                             one=True)[0]

    def login_query(self, form):
        """Login if credentials match"""
        if not form:
            return None
        username = form.get("username")
        hashed_password = hash_password(form.get("password"))
        result = self._is_user(username, hashed_password)
        if result:
            return {"username": username, "secret": hashed_password}
        else:
            return None

    def _get_role(self, username: str, secret: str) -> sqlite3.Row:
        return self.query_db("select role from USERS where username = ? and secret = ?", (username, secret), one=True)

    def get_user(self, username: bytes, secret: bytes):
        """ Returns User object if exist """
        username = username.decode()
        secret = secret.decode()
        res = self._get_role(username, secret)
        if res:
            self.logger.info(f"User {username} found.")
            user = User(username, res[0])
            return user
        return None

    def is_admin(self, request) -> bool:
        session = get_session(request)
        print(session)
        if not session:
            return None
        if "username" not in session or "secret" not in session:
            return None
        user = self.get_user(session.get("username"), session.get("secret"))
        return user.role == 1

    @contextmanager
    def transaction(self):
        # We must issue a "BEGIN" explicitly when running in auto-commit mode.
        self.db.execute('BEGIN')
        try:
            # Yield control back to the caller.
            yield
        except sqlite3.Error:
            self.db.rollback()  # Roll back all changes if an exception occurs.
            raise
        else:
            self.db.commit()
