USE SQLrelacional;
CREATE TABLE PAIS (
id_pais				INT NOT NULL IDENTITY(1,1),
nome				VARCHAR(60) NOT NULL,
CONSTRAINT PKIDPAIS PRIMARY KEY(id_pais)
);

CREATE TABLE FABRICANTE (
id_fabricante		INT NOT NULL IDENTITY(1,1),
nome				varchar(60) NOT NULL,
CONSTRAINT PKIDFAB PRIMARY KEY(id_fabricante),
);

CREATE TABLE FORNECEDOR (
id_fornecedor		INT NOT NULL IDENTITY(1,1),
nome				VARCHAR(60) NOT NULL,
CONSTRAINT PKIDFORN PRIMARY KEY(id_fornecedor)
);

CREATE TABLE MARCA (
id_marca			INT NOT NULL IDENTITY(1,1),
nome				VARCHAR(60) NOT NULL UNIQUE,
CONSTRAINT PKIDMARCA PRIMARY KEY(id_marca),
);

CREATE TABLE MODELO (
id_modelo			INT NOT NULL IDENTITY(1,1),
nome				VARCHAR(60) NOT NULL UNIQUE,
CONSTRAINT PKIDMODELO PRIMARY KEY(id_modelo),
);

CREATE TABLE SUBMODELO (
id_sub_modelo		INT NOT NULL IDENTITY(1,1),
nome				VARCHAR(60) UNIQUE,
CONSTRAINT PKIDTIPO PRIMARY KEY(id_sub_modelo),
);

CREATE TABLE PECAS (
id_peca			INT NOT NULL CONSTRAINT PKIDPECA PRIMARY KEY IDENTITY(1,1),
nome			VARCHAR(20) NOT NULL,
);

CREATE TABLE PESSOA(
id_pessoa		INT PRIMARY KEY IDENTITY(1,1),
n_bi			INT NOT NULL UNIQUE,
);


