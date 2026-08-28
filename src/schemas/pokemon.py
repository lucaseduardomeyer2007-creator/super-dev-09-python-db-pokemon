from dataclasses import dataclass

from src.schemas.categoria import Categoria

@dataclass
class Pokemon:
    id: int
    nome: str
    descricao: str
    numero: str
    categoria: Categoria # Composição
    vida: float
    forca_ataque: float
    registro_ativo: bool


# Representar os dados que vieram do front-end
@dataclass
class PokemonCadastro:
    nome: str
    descricao: str
    numero: str
    id_categoria: int
    vida: float
    forca_ataque: float


@dataclass
class PokemonEditar:
    nome: str
    descricao: str
    numero: str
    id_categoria: int
    vida: float
    forca_ataque: float