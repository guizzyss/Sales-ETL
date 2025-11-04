#Script que faz a limpeza, cálculos e formtações nos dados brutos
#Script that performs cleaning, calculations, and formatting on raw data

import pandas as pd
import logging

logging = logging.getLogger(__name__)

def transform_data(sales_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """Função para transformar os dados de vendas e produtos.
    Args:
        sales_df (pd.DataFrame): DataFrame contendo os dados de vendas brutas.
        products_df (pd.DataFrame): DataFrame contendo os dados de produtos.
    Returns:
        pd.DataFrame: DataFrame transformado com cálculos e formatações aplicadas.
    """
    if sales_df is None or products_df is None:
        logging.warning("Dataframes nulos não podem ser transformados.")
        return None
    
    logging.info("Iniciando o processo de transformação")

    try:
        #1. Juntar os dados de vendas e de produtos
        df = pd.merge(sales_df, products_df, on='product_id', how='left')
        logging.info("Dados de vendas e produtos mesclados com sucesso.")

        #2. Tratar valores nulos
        df['category'] = df['category'].fillna('Desconhecido')

        #3. Calcular a receita total por venda
        df['total_revenue'] = df['quantity_sold'] * df['price_per_unit']

        #4. Formatr a coluna de data para o formato datetime
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        logging.info("Transformações aplicadas com sucesso.")

        #5. Retornar o Dataframe transformado
        final_df = df[['sale_id', 'product_id', 'product_name', 'category', 'quantity_sold', 'price_per_unit', 'total_revenue','sale_date']]

        return df
    except Exception as e:
        logging.error(f"Erro durante a transformação dos dados: {e}")
        return None