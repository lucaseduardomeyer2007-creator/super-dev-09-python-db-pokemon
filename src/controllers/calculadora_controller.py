from fastapi import APIRouter

router = APIRouter()


@router.get("/mensagem")
def mensagem():
    """Rota para uma mensagem de boas vindas"""
    return {"mensagem: Olá mundo"}


#Query params: numero1 numero2
# http://localhost:8000/calculadora/somar?numero1=2&numero2=5
@router.get("/calculadora/somar")
def somar(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {
        "resultado": soma
    }


# http://127.0.0.1:8000/calculadora/imc?peso=70&altura=1.50
@router.get("calculadora/imc")
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


# http://localhost:8000/concatenar/nome_completo?nome=Lucas&sobrenome=Eduardo
@router.get("/concatenar")
def nome_completo(nome: str, sobrenome: str):
    resultado = f"{nome} {sobrenome}"
    return {
        "Resultado": resultado
    }


# http://localhost:8000/calcular_desconto
@router.get("/calcular/desconto")
def calcular_desconto(preco: float, percentual: float):
    valor_desconto = preco * (percentual / 100)
    valor_com_desconto = preco - valor_desconto

    return {
    "preço": preco, 
    "Percentual": percentual,
    "Valor do desconto": round(valor_desconto, 2),
    "Valor com o desconto": round(valor_com_desconto, 2)
    }


@router.get("/calcular/media")
def calcular_media(nota1: float, nota2: float, nota3: float, nota4: float):
    media = (nota1 + nota2+ nota3 + nota4) / 4


    return {
        "nota 1": nota1,
        "nota 2": nota2,
        "nota 3": nota3,
        "nota 4": nota4,
        "media": round(media, 2)
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



