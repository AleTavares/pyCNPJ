#nome, UF e capital social
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
    resposta = dadosCNPJ(cnpj)
    print(resposta)
    if 'nome' in resposta:
        teste = bd.manutEmpres(cnpj, resposta['nome'], resposta['uf'], resposta['capital_social'])
        print(teste)
        print('Nome:', resposta['nome'])
        print('UF:',  resposta['uf'])
        print('Capital Social:',  resposta['capital_social'])
    else:
        print('Erro:', resposta['erro'] )
    
    