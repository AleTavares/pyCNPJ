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
def incEmpresa(cnpj, nome, uf, capitalSocial):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_empresas(cnpj, nome, uf, capitalSocial) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (cnpj, nome, uf, capitalSocial))
        connection.commit()
        return 'OK'
    except Exception as e:
        return 'ERRO: '+ e

def cnpjExiste(cnpj):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT cnpj FROM tb_empresas WHERE cnpj = %s"
        cursor.execute(sql, (cnpj))
        result = cursor.fetchone()
        print(result)
        if len(result) > 0:
            return True
        else:
            return False
def alterEmpresa(cnpj, nome, uf, capitalSocial):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE tb_empresas \
                        SET nome = %(nome)s, \
                        uf = %(uf)s, \
                        capitalSocial = %(capital)s \
                   WHERE cnpj = %(cnpj)s"
            cursor.execute(sql, ({'nome':nome, 'uf':uf, 'capital':capitalSocial, 'cnpj':cnpj}))
        connection.commit()
        return 'OK'
    except Exception as e:
        return 'ERRO: '+ e
