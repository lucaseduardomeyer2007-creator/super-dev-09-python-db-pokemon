from fastapi import APIRouter

from src.repositories import categoria_repository
router = APIRouter()

router.get("/categorias")
def listar_categorias():
    return categoria_repository.consultar_todos()