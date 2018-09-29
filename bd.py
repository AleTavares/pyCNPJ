import pymysql.cursors
servidor = 'localhost' # Alterar para o Nome do Servidor
usuario = 'root' # Alterar para o Usuario da sua base de dados
senha = 'XXXXXX' # Alterar para a senha do usuario que foi definaida
banco = 'pyCNPJ' # Nome da base de dados criada (Padrão do Script)

# Conectando com a BAse de Dados
connection = pymysql.connect(host=servidor,
                             user=usuario,
                             password=senha,
                             db=banco,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Função para Incluir CNPJ no cadastro
def incEmpresa(cnpj, nome, uf, capitalSocial, Municipio, EMail):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_empresas(cnpj, nome, uf, capitalSocial, Municipio, EMail)\
                    VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (cnpj, nome, uf, capitalSocial, Municipio, EMail))
        connection.commit()
        return 'OK'
    except Exception as e:
        return 'ERRO: '+ e

# Função para verificar se o CNPJ Existe
def cnpjExiste(cnpj):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT cnpj FROM tb_empresas WHERE cnpj = %s"
        cursor.execute(sql, (cnpj))
        result = cursor.fetchone()
        if result:
            print(result)
            if len(result) > 0:
                return True
            else:
                return False
        else:
            return False

# Função Para alterar Cadastro existentes
def alterEmpresa(cnpj, nome, uf, capitalSocial, Municipio, EMail):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE tb_empresas \
                        SET nome = %(nome)s \
                        , uf = %(uf)s \
                        , capitalSocial = %(capital)s \
                        , Municipio = %(Municipio)s \
                        , EMail = %(EMail)s \
                   WHERE cnpj = %(cnpj)s"
            cursor.execute(sql, ({'nome':nome, 'uf':uf, 'capital':capitalSocial, 'cnpj':cnpj, 'Municipio': Municipio , 'EMail': EMail }))
        connection.commit()
        return 'OK'
    except Exception as e:
        return 'ERRO: '+ str(e)
