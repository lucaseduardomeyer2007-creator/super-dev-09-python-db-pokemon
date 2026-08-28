from fastapi import APIRouter, HTTPException, status

from src.repositories import pokemon_repository
from src.schemas.pokemon import PokemonCadastro, PokemonEditar 

router: APIRouter = APIRouter(prefix="/pokemons")


# @router.get("/pokemons")
@router.get("")
def listar_pokemons():
    return pokemon_repository.consultar_todos()


# @router.post("/pokemons")
@router.post("")
def cadastrar(pokemon: PokemonCadastro):
    return pokemon_repository.cadastrar(pokemon)


@router.put("/{id}")
def editar(id: int, pokemon: PokemonEditar):
    pokemon_banco = pokemon_repository.consultar_por_id(id)

    if pokemon_banco is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon não encontrado")

    pokemon_repository.editar(id, pokemon)
    return {
        "status": "ok"
    }


@router.delete("/{id}")
def apagar(id: int):
    pokemon = pokemon_repository.consultar_por_id(id)

    if pokemon is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon não encontrado")


    pokemon_repository.apagar(id)
    return {
        "status": "ok"
    }

@router.get("/{id}")
def consultar_por_id(id: int):
    pokemon = pokemon_repository.consultar_por_id(id)

    if pokemon is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon não encontrado")

    return pokemon