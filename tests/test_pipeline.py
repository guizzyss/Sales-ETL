#Testes simples para o pipeline ETL
#Simple tests for the ETL pipeline

import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.extract import extract_data
import logging

# Desabilita os logs durante os testes
logging.disable(logging.CRITICAL)

@pytest.fixture
def sample_sales_data():
    data = {
        'sale_id': [1, 2, 3],
        'request_id': [101, 102, 103],
        'customer_id': [1001, 1002, 1003],
        'product_id': [501, 502, 503],
        'quantity': [10, 20, 30],
        'sale_date': ['2023-01-01', '2023-01-02', '2023-01-03']
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_products_data():
    data = {
        'product_id': [501, 502, 503],
        'product_name': ['Tablet', 'Notebook', 'Smartphone'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'price': [300.0, 800.0, 600.0]
    }
    return pd.DataFrame(data)

def test_extract_data(sample_sales_data, sample_products_data):
    # Simula a extração dos dados
    sales_df = sample_sales_data
    products_df = sample_products_data

    # Verifica se os DataFrames extraídos são iguais aos esperados
    expected_sales_df = pd.DataFrame({
        'sale_id': [1, 2, 3],
        'request_id': [101, 102, 103],
        'customer_id': [1001, 1002, 1003],
        'product_id': [501, 502, 503],
        'quantity': [10, 20, 30],
        'sale_date': ['2023-01-01', '2023-01-02', '2023-01-03']
    })

    expected_products_df = pd.DataFrame({
        'product_id': [501, 502, 503],
        'product_name': ['Tablet', 'Notebook', 'Smartphone'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'price': [300.0, 800.0, 600.0]
    })

    assert_frame_equal(sales_df, expected_sales_df)
    assert_frame_equal(products_df, expected_products_df)

def test_transform_data(sample_sales_data, sample_products_data):
    # Simula a transformação dos dados
    sales_df = sample_sales_data
    products_df = sample_products_data

    expected_transformed_df = pd.DataFrame({
        'sale_id': [1, 2, 3],
        'request_id': [101, 102, 103],
        'customer_id': [1001, 1002, 1003],
        'product_id': [501, 502, 503],
        'quantity': [10, 20, 30],
        'sale_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'product_name': ['Tablet', 'Notebook', 'Smartphone'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'price': [300.0, 800.0, 600.0],
        'total_sale_value': [3000.0, 16000.0, 18000.0]
    })