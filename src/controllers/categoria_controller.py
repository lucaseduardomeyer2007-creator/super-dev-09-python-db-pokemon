from fastapi import APIRouter, HTTPException, status

from src.repositories import categoria_repository
from src.schemas.categoria import CategoriaCadastro, CategoriaEditar


router = APIRouter()

@router.get("/categorias")
def listar_categorias():
    return categoria_repository.consultar_todos()


@router.post("/categorias")
def cadastrar_categoria(categoria: CategoriaCadastro):
    categoria_criada = categoria_repository.cadastrar(categoria)
    return categoria_criada

@router.delete("/categorias/{id}")
def apagar(id: int):
    categoria_repository.apagar(id)
    # N é a forma final, faremos diferente, falta tratar 404, deve ser um 
    # 204 No content 
    return {"status": "OK"}

@router.get("/categorias/{id}")
def consultar_por_id(id: int):
    categoria = categoria_repository.consultar_por_id(id)
    if categoria is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada")

    return categoria


@router.put("/categorias/{id}")
def editar(id: int, categoria: CategoriaEditar):
    # Buscar para verificar se a categoria existe no banco de dados ou não
    categoria_existente = categoria_repository.consultar_por_id(id)
    if categoria_existente is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada")

    categoria_repository.editar(id, categoria)
    return {"status": "OK"}
