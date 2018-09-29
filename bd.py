import pymysql.cursors
servidor = 'localhost'
usuario = 'root'
senha = 'suporte'
banco = 'pyCNPJ'

# Connect to the database
connection = pymysql.connect(host=servidor,
                             user=usuario,
                             password=senha,
                             db=banco,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
def manutEmpres(cnpj, nome, uf, capitalSocial):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_empresas(cnpj, nome, uf, capitalSocial) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (cnpj, nome, uf, capitalSocial))
        connection.commit()
        return 'OK'
    except Exception as e:
        print(e)
        return 'ERRO'