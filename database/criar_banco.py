import sqlite3

conn = sqlite3.connect("database/banco.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS demandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    instituicao TEXT,
    demanda TEXT
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso")