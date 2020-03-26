CREATE DATABASE pyCNPJ;

USE pyCNPJ;

CREATE TABLE tb_empresas(
	idEmpresa SMALLINT AUTO_INCREMENT,
    cnpj CHAR(14) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    uf char(2) NOT NULL,
    Municipio varchar(100),
    EMail varchar(100),
    capitalSocial DECIMAL(16,2),
	PRIMARY KEY(idEmpresa)
);