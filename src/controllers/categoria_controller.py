from fastapi import APIRouter

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
    # Não é a forma final, faremos diferente, falta tratar 404, deve ser um
    # 204 no content
    return {"status": "OK"}


    