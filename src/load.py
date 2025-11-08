#Script que cria uma nova tabela e insere os dados processados
#Script that creates a new table and inserts the processed data

import os
import pandas as pd
import logging
import psycopg2
from sqlalchemy import create_engine
from config.db_config import get_db_connection
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

def get_sql_alchemy_engine():
    # Cria uma engine SQLAlchemy para conexão com o banco de dados

    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

        engine = create_engine(connection)
        logger.info("Engine SQLAlchemy criada com sucesso.")
        return engine

    except Exception as e:
        logger.error(f"Erro ao criar a engine SQLAlchemy: {e}")
        return None
    
def load_data(df: pd.DataFrame, table_name: str, if_exists: str = 'replace'):
    """Função para carregar dados em uma tabela do banco de dados.
    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem carregados.
        table_name (str): Nome da tabela onde os dados serão inseridos.
        if_exists (str): Comportamento se a tabela já existir ('fail', 'replace', 'append').
    """
    if df is None:
        logger.error("DataFrame vazio. Nenhum dado para carregar.")
        return
    
    logger.info(f"Iniciando o processo de carga de dados na tabela '{table_name}'.")

    engine = get_sql_alchemy_engine()
    if engine is None:
        logger.error("Não foi possível conectar-se ao banco de dados. Cancelando a carga de dados.")
        return
    
    try:
        df.to_sql(
            table_name,
            con=engine,
            if_exists=if_exists,
            index=False,
            chunksize=1000  # Ajuste o tamanho do chunk conforme necessário
        )
        logger.info(f"Carga de dados concluída com sucesso na tabela '{table_name}'. Total de registros carregados: {len(df)}")
    except Exception as e:  
        logger.error(f"Erro ao carregar os dados na tabela '{table_name}': {e}")
    finally:
        engine.dispose()
        logger.info("Conexão ao banco de dados fechada.")

