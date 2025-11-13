# Projeto SALES-ETL

Um pipeline de ETL (Extract, Transform, Load) para processar dados de vendas.

## 🎯 Objetivo

Este projeto extrai dados brutos de vendas de um banco de dados, realiza transformações (como limpeza, junção de tabelas e cálculos) e carrega os dados processados em uma tabela analítica.

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [url-repositorio]
    cd SALES-ETL
    ```

2.  **Crie um Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # (Linux/macOS)
    .\venv\Scripts\activate   # (Windows)
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente:**
    * Copie o `.env.example` para um novo arquivo chamado `.env`:
      ```bash
      cp .env.example .env
      ```
    * Edite o arquivo `.env` com as credenciais corretas do seu banco de dados.

5.  **Execute o Pipeline Principal:**
    ```bash
    python src/main.py
    ```

## 🧪 Como Testar

Para rodar os testes unitários e garantir que a lógica de transformação está correta:

```bash
pytest
