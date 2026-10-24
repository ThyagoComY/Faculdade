CREATE DATABASE IF NOT EXISTS db_java
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE db_java;

-- JSON preserva os componentes de Endereco em uma unica coluna
-- sem concatenar dados e sem criar uma segunda tabela.
CREATE TABLE IF NOT EXISTS usuario (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    cpf CHAR(11) NOT NULL,
    email VARCHAR(254) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco JSON NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_usuario_cpf (cpf),
    UNIQUE KEY uk_usuario_email (email)
);
