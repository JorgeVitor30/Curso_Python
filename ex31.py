import pymysql.cursors
from contextlib import contextmanager


# CRUD - CREATE, READ, UPDATE, DELETE


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


#I NSERE UM REGISTRO NA BASE DE DADOS
#with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#        #cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#        conexao.commit()


#with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#        
#        dados = [
#            ('MURILO', 'BISPO', 16 , 45),
#           ('JOAO', 'REGO', 18 , 85),
#            ('JORGE', 'VITOR', 19 , 93),
#        ]
#       
#        cursor.executemany(sql,dados) 
#                       
#       conexao.commit()



# APAGA EM UNIDADE DO BD
with conecta() as conexao:
    with conexao.cursor() as cursor:
       sql = 'DELETE FROM clientes WHERE id = %s'
       cursor.execute(sql, 6)
            
       conexao.commit()



# APAGA EM MAIOR QUANTIADE DO BD
with conecta() as conexao:
    with conexao.cursor() as cursor:
       sql = 'DELETE FROM clientes WHERE id IN (%s,%s,%s)'
       cursor.execute(sql, (7,8,9))
              
       conexao.commit()



# APAGA EM MAIOR QUANTIADE DO BD DE UM INTERVALO ATÉ OUTRO INTERVALO
with conecta() as conexao:
    with conexao.cursor() as cursor:
       sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
       cursor.execute(sql, (10,12))

       conexao.commit()


# TROCA O NOME DO CLIENTE DE ACORDO COM O ID DETERMINADO
with conecta() as conexao:
    with conexao.cursor() as cursor:
       sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
       cursor.execute(sql, ('Ana',2))

       conexao.commit()



with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

