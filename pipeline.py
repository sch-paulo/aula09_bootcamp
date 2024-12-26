from etl import pipeline_calculate_kpi_of_total_sales_consolidated
from tenacity_decorator import get_user_input

file = 'data'
output_format = 'parquet and csv'

try:
    get_user_input()
    pipeline_calculate_kpi_of_total_sales_consolidated(file, output_format)
except Exception as e:
    print(f"Finalmente falhou após várias tentativas: {e}")
