# Sistema de Aluguel de Veículos

Este é um sistema de aluguel de veículos desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e SQLite3 para o banco de dados. O sistema permite que os usuários realizem diversas operações, como cadastrar clientes, cadastrar veículos, alugar veículos e listar todas as informações cadastradas.

## Funcionalidades

- **Cadastro de Clientes**: Os usuários podem se cadastrar fornecendo informações como nome, CPF, CNH, email, telefone e CEP.
- **Cadastro de Veículos**: É possível cadastrar veículos com detalhes como modelo, marca, ano, placa, etc.
- **Aluguel de Veículos**: Os clientes cadastrados podem alugar veículos disponíveis.
- **Listagem de Informações**: O sistema permite listar todos os clientes, veículos e aluguéis realizados.

## Requisitos

- Python 3.x
- Bibliotecas padrão do Python (Tkinter e SQLite3 já estão incluídas na instalação padrão do Python).

## Estrutura do Projeto

- `TelaPrincipal.py`: Arquivo principal do sistema, responsável pela interface inicial.
- `TelaCadastroClientes.py`: Interface para cadastrar clientes.
- `TelaCadastroVeículos.py`: Interface para cadastrar veículos.
- `TelaAluguel.py`: Interface para realizar aluguéis.
- `TelaListarClientes.py`: Interface para listar clientes cadastrados.
- `TelaListarVeiculos.py`: Interface para listar veículos cadastrados.
- `TelaListarAluguel.py`: Interface para listar aluguéis realizados.
- `database.py`: Script para manipulação do banco de dados.
- `DataBase.bd`: Arquivo do banco de dados SQLite3.
- `Imagens/`: Diretório contendo imagens utilizadas na interface gráfica.
