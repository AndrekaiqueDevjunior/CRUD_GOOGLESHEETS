---

# Projeto de Gestão de Funcionários com Flask e Google Sheets

Este projeto é uma aplicação web desenvolvida com Flask e Google Sheets para gerenciar informações de funcionários. Ele permite visualizar, adicionar, editar, excluir e buscar funcionários usando uma interface web moderna.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python para criar aplicações web.
- **Google Sheets API**: Interface para interagir com planilhas do Google Sheets.
- **HTML/CSS**: Linguagens de marcação e estilo para a criação da interface do usuário.
- **Bootstrap**: Framework CSS para estilizar e tornar a interface responsiva.
- **JavaScript**: Linguagem de script para adicionar interatividade à página.
- **Google OAuth2**: Para autenticação segura ao acessar a API do Google Sheets.

## Funcionalidades

- **Visualizar Funcionários**: Exibe uma lista paginada de funcionários.
- **Adicionar Funcionário**: Permite adicionar novos funcionários ao banco de dados.
- **Editar Funcionário**: Permite atualizar as informações de um funcionário existente.
- **Excluir Funcionário**: Permite excluir um funcionário do banco de dados.
- **Buscar Funcionário**: Permite buscar funcionários por nome.

## Tutorial de Uso

### 1. Configuração Inicial

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
   ```

2. **Instale as Dependências**
   Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configuração do Google Sheets**
   - Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).
   - Habilite a API do Google Sheets.
   - Crie uma credencial de Conta de Serviço e baixe o arquivo JSON.
   - Renomeie o arquivo JSON para `service_account.json` e coloque-o na raiz do projeto.

4. **Configuração da Planilha**
   - Crie uma planilha no Google Sheets e compartilhe-a com o e-mail da Conta de Serviço.
   - Copie o ID da planilha e substitua o valor em `spreadsheet_id` no arquivo `app.py`.

### 2. Executando o Projeto

1. **Inicie o Servidor Flask**
   ```bash
   python app.py
   ```

2. **Acesse a Aplicação**
   Abra seu navegador e acesse `http://127.0.0.1:5000` para começar a usar a aplicação.

### 3. Estrutura do Projeto

- **`app.py`**: Arquivo principal onde o aplicativo Flask é configurado e executado.
- **`google_sheets.py`**: Funções para interagir com a API do Google Sheets.
- **`templates/`**: Diretório contendo todos os arquivos HTML.
- **`static/`**: Diretório contendo arquivos CSS e JavaScript estáticos.

### 4. Endpoints da API

- **GET `/`**: Página inicial com a lista de funcionários.
- **GET `/add`**: Página para adicionar um novo funcionário.
- **POST `/add`**: Adiciona um novo funcionário ao banco de dados.
- **GET `/edit/<int:id>`**: Página para editar as informações de um funcionário.
- **POST `/edit/<int:id>`**: Atualiza as informações de um funcionário.
- **POST `/delete/<int:id>`**: Exclui um funcionário.
- **GET `/search`**: Busca funcionários por nome.
- **GET `/employee/<int:id>`**: Retorna dados de um funcionário em formato JSON.

### 5. Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. 

---

Certifique-se de substituir os placeholders (como `SEU_USUARIO` e `SEU_REPOSITORIO`) com suas informações reais. Adapte a documentação conforme necessário para refletir exatamente o que seu projeto faz e como ele é configurado.
