

from typing import List, Optional
from src.database.conexao import conectar
from src.schemas.categoria import Categoria, CategoriaCadastro


def consultar_todos() -> List[Categoria]:
    # `with` garante que a conexão com o banco de dados seja fechada,
    # independente se deu algum erro ou não, Caso contrário cada requisição 
    # deixaria uma conexão aberta
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, nome FROM categorias")
            registros = cursor.fetchall()
        

    categorias = []
    for registro in registros:
        categoria = Categoria(id= registro[0], nome=registro[1])
        categorias.append(categoria)
    return categorias


def cadastrar(categoria: CategoriaCadastro):
    """Responsável por cadastrar a categoria no banco de dados"""
    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            # Executa o comando da insert passando os dados para substituir o(s) %s
            cursor.execute(sql, (categoria.nome,))
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


