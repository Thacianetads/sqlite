# 🛠️ Projeto SQLite com Python: Cadastro de Carros

Este projeto é um exemplo simples de como usar SQLite3 com Python para criar, inserir e consultar dados em um banco de dados local. O banco armazena informações de carros (modelo, marca e ano).

# 📁 Estrutura do Projeto
   
   ├── carros.db         
   ├── create_table.py   
   ├── insert_row.py      
   ├── select_rows.py     
   └── README.md       

# 🧩 Requisitos

- Python 3.x

# ⚙️ Como usar

1. Clone o repositório
2. Crie a tabela no banco de dados: python create_table.py
   Isso criará o arquivo carros.db com a tabela carros se ainda não existir.
3. Insira dados no banco
   Isso irá inserir um carro com os dados: Marea, Fiat, 1999.
4. Listar os carros cadastrados: python select_rows.py
   Isso irá exibir todos os carros cadastrados no terminal.

# 💻 Scripts explicados

create_table.py

- Cria o banco de dados carros.db e a tabela carros com as colunas:

 - id (chave primária, autoincremento)

 - modelo

 - marca

 - ano

insert_row.py

- Insere um novo registro na tabela carros.

select_rows.py

- Consulta todos os registros da tabela carros e imprime no terminal.
