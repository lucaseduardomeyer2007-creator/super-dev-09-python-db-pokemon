DROP DATABASE IF EXISTS poke_battle;

CREATE DATABASE poke_battle;

USE poke_battle;

CREATE TABLE categorias(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(20) NOT NULL
);

CREATE TABLE pokemons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(40) NOT NULL,
    descricao TEXT,
    numero CHAR(4) NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id),

    vida FLOAT NOT NULL,
    forca_ataque FLOAT NOT NULL,
    registro_ativo BOOLEAN NOT NULL
);


INSERT INTO categorias (nome) VALUES
('Fogo'),
('Água'),
('Planta'),
('Elétrico'),
('Psíquico');

INSERT INTO pokemons
(nome, descricao, numero, id_categoria, vida, forca_ataque)
VALUES
('Charmander', 'Pokémon lagarto de fogo.', '0004', 1, 39, 52),
('Squirtle', 'Pokémon tartaruga de água.', '0007', 2, 44, 48),
('Bulbasaur', 'Pokémon planta com uma semente nas costas.', '0001', 3, 45, 49),
('Pikachu', 'Pokémon rato elétrico.', '0025', 4, 35, 55),
('Mewtwo', 'Pokémon criado artificialmente com grande poder psíquico.', '0150', 5, 106, 110);


SELECT
    pokemons.id,
    pokemons.nome,
    pokemons.descricao,
    pokemons.numero,
    pokemons.id_categoria,
    categorias.nome,
    pokemons.vida,
    pokemons.forca_ataque,
    pokemons.registro_ativo
FROM pokemons
INNER JOIN categorias ON(pokemons.id_categoria = categorias.id);