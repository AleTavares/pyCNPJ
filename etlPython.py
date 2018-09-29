import json
import requests
import time
import bd
def dadosCNPJ(cnpjConsulta):
    dadosEmpresa = requests.get('https://www.receitaws.com.br/v1/cnpj/'+cnpjConsulta)
    if dadosEmpresa.status_code == 200:
        resultado = {}
        dadosExibir = json.loads(dadosEmpresa.content)
        if 'status' in dadosExibir:
            if dadosExibir['status'] == 'OK':
                resultado['nome'] = dadosExibir['nome']
                resultado['uf'] = dadosExibir['uf']
                resultado['capital_social'] = dadosExibir['capital_social']
                resultado['municipio'] = dadosExibir['municipio']
                resultado['email'] = dadosExibir['email']
                return resultado
            elif dadosExibir['status'] == 'ERROR':
                resultado['erro'] = dadosExibir['message']
                return resultado
            else:
                resultado['erro'] = 'Erro Inesperado com o CNPJ' + str(cnpjConsulta)
                return resultado
        else:
            dadosCNPJ(cnpjConsulta)
    else:
        print('### Falha na consulta, Aguarde 1 minuto que tentaremos novamente! ###')
        time.sleep( 60 )
        return dadosCNPJ(cnpjConsulta)

cnpjBuscar = open('listaCNPJ.txt', "r", encoding='iso-8859-1')

for cnpj in cnpjBuscar:
    cnpj = cnpj.replace('\n', '')
    resposta = dadosCNPJ(cnpj)
    if 'nome' in resposta:
        if bd.cnpjExiste(cnpj) == True:
            alterou = bd.alterEmpresa(cnpj, resposta['nome'], resposta['uf'], resposta['capital_social'], resposta['municipio'], resposta['email'])
            if alterou == 'OK':
                print('CNPJ Atualizado com sucesso!')
            else:
                print('Não Foi Possivel alterar o CNPJ' + str(cnpj))
                print(resposta)
        else:
            incluiu = bd.incEmpresa(cnpj, resposta['nome'], resposta['uf'], resposta['capital_social'], resposta['municipio'], resposta['email'])
            if incluiu == 'OK':
                print('CNPJ Incluido com Sucesso!')
            else:
                print('Não Foi Possivel Incluir o CNPJ' + str(cnpj))
                print(resposta)
    elif 'erro' in resposta:
        print(resposta['erro'])
    else:
        print('Erro inesperado, contacte o e-mail: portalatibaia@gmail.com')