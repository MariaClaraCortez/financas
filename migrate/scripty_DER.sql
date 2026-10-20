create database financas;
use financas;

CREATE TABLE if not exists tb_usuarios (
 login VARCHAR(120) NOT NULL PRIMARY KEY,
 senha VARCHAR(200)
);


CREATE TABLE if not exists tb_categorias (
 id_categoria SMALLINT auto_increment primary KEY,
 login VARCHAR(120) NOT NULL,
 tipo VARCHAR(20),

 FOREIGN KEY (login) REFERENCES tb_usuarios (login)
);


CREATE TABLE if not exists tb_dispesas (
 id_dispesa SMALLINT auto_increment primary KEY,
 id_categoria SMALLINT NOT NULL,
 valor DECIMAL(30,2),
 descricao VARCHAR(200),
 data DATE,
 hora TIME(6),

 FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria)
);


