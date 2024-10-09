
# Automação de Cadastro de Produtos com PyAutoGUI

Este repositório contém um script em Python que automatiza o processo de login e cadastro de produtos em uma plataforma de vendas. O script utiliza a biblioteca **PyAutoGUI** para simular interações humanas com o navegador e a **Pandas** para ler e manipular um arquivo CSV contendo os detalhes dos produtos a serem cadastrados.

## Principais Funcionalidades

- Abertura automática do navegador e acesso ao sistema da empresa.
- Login automático com preenchimento de email e senha.
- Importação de uma base de dados de produtos a partir de um arquivo CSV.
- Preenchimento e envio automatizado dos formulários de cadastro de produtos.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento do script.
- **PyAutoGUI**: Biblioteca para automação de interações com a interface gráfica.
- **Pandas**: Biblioteca para manipulação de dados em arquivos CSV.
Certifique-se de ajustar as coordenadas de clique e fazer os ajustes necessários no código para o seu ambiente.

## Como Utilizar

1. Clone este repositório e instale as dependências necessárias:
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git
   pip install -r requirements.txt
   ```

2. Coloque o arquivo `produtos.csv` na mesma pasta do script e execute o script:
   ```bash
   python nome_do_script.py
   ```

