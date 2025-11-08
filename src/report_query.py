#Query SQL para gerar relatórios a partir dos dados carregados
#SQL query to generate reports from the loaded data

# Relatório de Vendas por Produto

SALES_BY_PRODUCT_QUERY = """
SELECT 
    s.product_id,
    p.product_name,
    SUM(s.quantity) as total_quantity_sold,
    SUM(s.total_price) as total_sales
FROM sales s
JOIN products p ON s.product_id = p.id
GROUP BY s.product_id, p.product_name
ORDER BY total_sales DESC;
"""