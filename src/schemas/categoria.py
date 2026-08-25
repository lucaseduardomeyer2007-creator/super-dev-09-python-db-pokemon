from dataclasses import dataclass



# Representar a tabela do banco de dados
@dataclass
class Categoria:
    id: int
    nome: str


# Representar o dado da categoria  que veio no payload da request realizada
# pelo front-end, ou seja, os dados que front mandou 

@dataclass
class CategoriaCadastro:
    nome: str


@dataclass
class CategoriaEditar:
    nome: str