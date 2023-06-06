import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.CONN = sqlite3.connect('dogs.db')
        self.CURSOR = self.CONN.cursor()
        self.create_table()

    def create_table(self):
        self.CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                breed TEXT
            )
        ''')
        self.CONN.commit()

    def save(self):
        self.CURSOR.execute('''
            INSERT INTO dogs (name, breed) VALUES (?, ?)
        ''', (self.name, self.breed))
        self.CONN.commit()
        self.id = self.cursor.lastrowid

    @classmethod
    def find(cls, dog_id):
        CONN = sqlite3.connect('dogs.db')
        CURSOR = CONN.cursor()
        CURSOR.execute('SELECT * FROM dogs WHERE id=?', (dog_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[2])
        return None

    @classmethod
    def find_all(cls):
        CONN = sqlite3.connect('dogs.db')
        CURSOR = CONN.cursor()
        CURSOR.execute('SELECT * FROM dogs')
        rows = CURSOR.fetchall()
        dogs = []
        for row in rows:
            dogs.append(cls(row[1], row[2]))
        return dogs