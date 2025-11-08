#Script que faz a conexão ao banco de dados e extrai os dados necessários
#Script that connects to the database and extracts the necessary data

import pandas as pd
import logging
from config.db_config import get_db_connection

logger = logging.getLogger(__name__)

def read_data(query):
    """Função para ler dados do banco de dados usando uma query SQL.
    Args:
        query (str): A consulta SQL a ser executada.
    Returns:
        pd.DataFrame: DataFrame contendo os dados extraídos.
    """
    connection = get_db_connection()
    if connection is None:
        logger.error("Falha na conexão ao banco de dados.")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de falha na conexão

    try:
        df = pd.read_sql_query(query, connection)
        logger.info("Dados extraídos com sucesso.")
        return df
    except Exception as e:
        logger.error(f"Erro ao executar a query: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro na query
    finally:
        connection.close()
        logger.info("Conexão ao banco de dados fechada.")

# Exemplo de uso
# if __name__ == "__main__": 
#     sample_query = "SELECT * FROM sua_tabela LIMIT 10;" # Substitua 'sua_tabela' pelo nome real da tabela
#     data = read_data(sample_query)
#     print(data.head())

def extract_data():
    logger.info("Iniciando o processo de extração de dados.")
    conn=None

    try:
        conn = get_db_connection()
        df=pd.read_sql_query("SELECT * FROM Vendas;", conn)
        logger.info(f"Extração concluída. Total de registros extraídos: {len(df)}")
        return df
    except Exception as e:
        logger.error(f"Erro durante a extração de dados: {e}")
        return None
    finally:
        if conn:
            conn.close()
            logger.info("Conexão ao banco de dados fechada.")