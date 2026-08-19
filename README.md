# Projeto de batalhas de pokemons

## Instalação

Criar env: 'py -m venv env'

Ativar env Windows: 'env\Scripts\activate

Ativar env Linux: 'source env/Bin/activate'

Instalar uma dependencia: 'pip install <nome>'

Salvar quais dependencias o projeto tem: 'pip freeze > requirements.txt'

Instalar todas as dependencias do projeto: 'pip install -r requirements.txt'

Desativar env: 'deactivate'


Fluxo de novo projeto:
"""shell
py -m venv env
env\Scripts\activate
pip install "fastapi[standard]"
pip freeze > requirements.txt
"""