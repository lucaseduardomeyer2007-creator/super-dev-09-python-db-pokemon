from typing import List, Optional

from src.database.conexao import conectar
from src.schemas.categoria import Categoria, CategoriaCadastro, CategoriaEditar


def consultar_todos() -> List[Categoria]:
    # `with` garante que a conexão com o banco de dados seja fechada, 
    # independente se deu algum erro ou não. Caso contrário cada requisição 
    # deixaria uma conexão aberta
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, nome FROM categorias")
            registros = cursor.fetchall()

    categorias = []
    for registro in registros:
        categoria = Categoria(id=registro[0], nome=registro[1])
        categorias.append(categoria)
    return categorias


def cadastrar(categoria: CategoriaCadastro):
    """Responsável por cadastrar a categoria no banco de dados"""
    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            # Executa o comando de insert passando os dados para substituir
            # o(s) %s
            cursor.execute(sql, (categoria.nome,))
            # Pega o id que foi gerado no bd
            novo_id = cursor.lastrowid
            # Efetivar o comando de insert no banco de dados
            conexao.commit()
    # Retornar os dados da categoria com o id gerado
    return Categoria(id=novo_id, nome=categoria.nome)


def apagar(id: int):
    """Responsável por apagar a categoria do banco de dados"""
    sql = "DELETE FROM categorias WHERE id = %s"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()


def consultar_por_id(id: int) -> Optional[Categoria]:
    """Reponsável por consultar a categoria filtrando por id"""
    sql = "SELECT id, nome FROM categorias WHERE id = %s"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
    if registro is None:
        return None
    return Categoria(id=registro[0], nome=registro[1])


def editar(id: int, categoria: CategoriaEditar):
    """Responsável alterar os dados cadategoria no banco de dados"""
    sql = "UPDATE categorias SET nome = %s WHERE id = %s"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (categoria.nome, id))
            conexao.commit()
