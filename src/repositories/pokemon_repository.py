from typing import Optional

from src.database.conexao import conectar
from src.schemas.categoria import Categoria
from src.schemas.pokemon import Pokemon, PokemonCadastro, PokemonEditar


def consultar_todos() -> list[Pokemon]:
    """Responsável por consultar todos os pokemons incluindo sua categoria"""
    sql = """SELECT
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
INNER JOIN categorias ON(pokemons.id_categoria = categorias.id)
WHERE pokemons.registro_ativo = 1"""
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            registros = cursor.fetchall()

    pokemons: list[Pokemon] = []
    for registro in registros:
        # Instanciar um objeto da classe Categoria
        categoria: Categoria = Categoria(
            id=registro[4],
            nome=registro[5]
        )

        registro_ativo = False
        if registro[8] == 1:
            registro_ativo = True

        # Instanciar um objeto da classe Pokemon
        pokemon: Pokemon = Pokemon(
            id=registro[0],
            nome=registro[1],
            descricao=registro[2],
            numero=registro[3],
            categoria=categoria,
            vida=registro[6],
            forca_ataque=registro[7],
            registro_ativo=registro_ativo
        )

        pokemons.append(pokemon)
    return pokemons


def cadastrar(pokemon: PokemonCadastro) -> Pokemon:
    sql = """INSERT INTO pokemons 
    (nome, descricao, id_categoria, vida, forca_ataque, numero)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (pokemon.nome, pokemon.descricao, pokemon.id_categoria, pokemon.vida, pokemon.forca_ataque, pokemon.numero))
            novo_id = cursor.lastrowid
            conexao.commit()
    return Pokemon(
        id=novo_id,
        nome=pokemon.nome,
        descricao=pokemon.descricao,
        numero=pokemon.numero,
        categoria=None,
        vida=pokemon.vida,
        forca_ataque=pokemon.forca_ataque,
        registro_ativo=True
    )


def editar(id: int, pokemon: PokemonEditar):
    sql = """UPDATE pokemons SET 
        nome=%s,
        descricao=%s,
        numero=%s,
        id_categoria=%s,
        vida=%s,
        forca_ataque=%s
    WHERE id=%s
    """
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (
                pokemon.nome, 
                pokemon.descricao, 
                pokemon.numero, 
                pokemon.id_categoria, 
                pokemon.vida, 
                pokemon.forca_ataque,
                id,
            ))
            conexao.commit()


def apagar(id: int):
    # Alternativa para n apagar o registro fisicamente
    # Desativar o registro, atualizando o registro_ativo
    sql = "UPDATE pokemons SET registro_ativo = 0 WHERE id = %s"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()


def consultar_por_id(id: int) -> Optional[Pokemon]:
    """Responsável por consultar pokemons incluindo sua categoria filtrando por id"""
    sql = """SELECT
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
INNER JOIN categorias ON(pokemons.id_categoria = categorias.id)
WHERE pokemons.registro_ativo = 1 AND pokemons.id = %s"""
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

    if registro is None:
        return None

    # Instanciar um objeto da classe Categoria
    categoria: Categoria = Categoria(
        id=registro[4],
        nome=registro[5]
    )

    # Instanciar um objeto da classe Pokemon
    pokemon: Pokemon = Pokemon(
        id=registro[0],
        nome=registro[1],
        descricao=registro[2],
        numero=registro[3],
        categoria=categoria,
        vida=registro[6],
        forca_ataque=registro[7],
        registro_ativo=True
    )

    return pokemon