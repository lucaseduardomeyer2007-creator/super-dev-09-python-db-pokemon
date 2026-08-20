from fastapi import FastAPI
from pathlib import Path
import sys

# Permite rodar com ´py src/app.py´: coloca a raiz do projeto no sys.path
# para que os imports `from src import .` funcionem corretamente
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Swagger = http://localhost:8000/docs

app = FastAPI(
    title="Pokemon API",
    description="Projeto para batalhas de pokemons",
    version="0.1.0"
)

@app.get("/mensagem")
def mensagem():
    """Rota para uma mensagem de boas vindas"""
    return {"mensagem: Olá mundo"}

#Query params: numero1 numero2
# http://localhost:8000/calculadora/somar?numero1=2&numero2=5
@app.get("/calculadora/somar")
def somar(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {
        "resultado": soma
    }


# http://127.0.0.1:8000/calculadora/imc?peso=70&altura=1.50
@app.get("calculadora/imc")
def calcular_imc(peso: float, altura: float):
    imc = peso / altura **2

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Acima do peso"
    else:
        classificacao = "Obesidade"
   
    return {
       "peso": peso,
       "altura": altura,
       "imc": round(imc, 2),
       "Classificacao": classificacao
   }


# 0. Criar endpoint / concatenar
#      Recebe nome e sobrenome
#      Retorna o nome completo
#1. Criar endpoint /calcular/desconto
#      Recebe preco e percentual como query param
#      Calcular o valor do desconto
#      Retornar o preço, percentual, valor do desconto e valor com desconto
#2. Criar endpoint /calcular/media
#      Recebe nota1, nota2, nota3, nota 4
#      Calcular a média
#      Retornar as notas e a média





if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)

