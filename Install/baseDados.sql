CREATE DATABASE pyCNPJ;
USE pyCNPJ;
drop table tb_empresas;
CREATE TABLE tb_empresas(
	idEmpresa SMALLINT AUTO_INCREMENT,
    cnpj CHAR(14) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    uf char(2) NOT NULL,
    capitalSocial DECIMAL(16,2),
	PRIMARY KEY(idEmpresa)
);

alter table tb_empresas add column Municipio varchar(100);

alter table tb_empresas add column EMail varchar(100);

