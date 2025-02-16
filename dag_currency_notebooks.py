from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime

with DAG(
    'Executando-notebook-elt',
    start_date=datetime(2025, 1, 1),
    schedule_interval="0 9 * * *",
    ) as dag_executando_notebook_extracao:
    
    extraindo_dados = DatabricksRunNowOperator(
        task_id='extraindo_taxas',
        databricks_conn_id= 'databricks_default',
        job_id=262931903736481,
        notebook_params={"data_execucao": '{{data_interval_end.strftime("%Y-%m-%d")}}'})
    
    transformando_dados = DatabricksRunNowOperator(
        task_id='transformando_dados',
        databricks_conn_id= 'databricks_default',
        job_id=865323238643086,
        notebook_params={"data_execucao": '{{data_interval_end.strftime("%Y-%m-%d")}}'})
    
    enviando_relatorio = DatabricksRunNowOperator(
        task_id='enviando_relatorio',
        databrick_conn_id= 'databricks_default',
        job_id=643100594161279
    )

extraindo_dados >> transformando_dados >> enviando_relatorio