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

cnpjBuscar = ['16501555000157', '14994237000140', '18727053000174', '13966572000171', '12839955000116', 
              '16569357000125', '16575851000100', '12592831000189']

for cnpj in cnpjBuscar:
    print(cnpj)
    resposta = dadosCNPJ(cnpj)
    if 'nome' in resposta:
        if bd.cnpjExiste(cnpj) == True:
            alterou = bd.alterEmpresa(cnpj, resposta['nome'], resposta['uf'], resposta['capital_social'])
            if alterou == 'OK':
                print('CNPJ Atualizado com sucesso!')
            else:
                print('Não Foi Possivel alterar o CNPJ' + str(cnpj))
                print(resposta)
        else:
            incluiu = bd.incEmpresa(cnpj, resposta['nome'], resposta['uf'], resposta['capital_social'])
            if incluiu == 'OK':
                print('CNPJ Incluido com Sucesso!')
            else:
                print('Não Foi Possivel Incluir o CNPJ' + str(cnpj))
                print(resposta)
    elif 'erro' in resposta:
        print(resposta['erro'])
    else:
        print('Erro inesperado, contacte o e-mail: portalatibaia@gmail.com')

            
    