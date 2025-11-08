#Contém credenciais e configurações de conexão ao banco de dados
#Contains credentials and connection settings to the database

import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
# Loads environment variables from the .env file
load_dotenv()

def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        print("Conexão ao banco de dados estabelecida com sucesso.")
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
# Exemplo de uso
# conn = get_db_connection()
# if conn:
#     print("Tudo certo!")
#     conn.close()