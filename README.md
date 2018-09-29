# pyCNPJ
A aplicação construída deve extrair dados da api da receitaws (informações constantes em https://receitaws.com.br/api). 

# Instalação
 - Instalar o MySQL no computador local
 - Abrir o arquivo bd.py e configurar os dados do servidor
 - conectar ao banco de dados e executar o script Install/baseDados.sql

 - Instalar o Python no computador local

 - Registrar no Path do seu sistema Operacional o caminho para o python

 - Abrir o Shell e executar os comandos:
  - pip install json
  - pip install requests
  - pip install time
  - pip install pymysql

 - no shell executa o comando "python etlPython.py" para captura dos dados
 
 - instalar o Power BI
 - Iniciar o Power BI e abrir o arquivo dashboardcapitalporUF.pbix
 - Entrar em:
  - Arquivo -> Opções e Definições -> Definições de Origem de Dados
  - Editar a conexão e alerar os dados pra conexão com a Base de Dados Local
 
 # Arquivos
 - bd.py -> Dados e Funções para o Banco de Dados
 - etlPython.py -> ELT para estrair dados da api da receitaws
 - listaCNPJ.txt -> ista de CNPJ para baixar os dados
 - dashboardcapitalporUF.pbix -> painel do Power BI para exibir dados de Capital Social por UF
 - Install/baseDados.sql -> Script para criação da Base de Dados
 
 # Fonte
 https://receitaws.com.br
 
 # Suporte
 portalatibaia@gmail.com