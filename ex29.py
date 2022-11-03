import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'nome TEXT,' 
    'peso REAL'
    ')')

# INTEGER = INT
# REAL = FLOAT
# TEXT = STRING


cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Jorge', 50))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', 
{'nome':'Jorge','peso': 50})

cursor.execute(' UPDATE clientes SET nome=:nome WHERE id=:id',
          {'nome': 'Joana', 'id':2}
)


conexao.commit() # EXECUTAR O COMANDO DE CIMA


conexao.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
