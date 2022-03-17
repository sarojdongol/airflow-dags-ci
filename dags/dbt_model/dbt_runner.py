"""
Following code is template file to run dbt jobs using dbt operators.
"""
from airflow import DAG
from airflow_dbt.operators.dbt_operator import (
    DbtRunOperator,
)
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


default_args = {
    'owner': 'dbtwarehouse',
    'retries': 0,
    'email': ['saroj.dongol@intellify.com.au'],
    'email_on_failure': True
}


with DAG(
    dag_id="DBTrunner",
    description="Databricks silver Builder",
    start_date=datetime(2022, 3, 17),
    schedule_interval="@daily",
    default_args=default_args
) as dag:

    dbt_run = DbtRunOperator(
        task_id='dbt_run',
        dbt_bin='/usr/local/airflow/.local/bin/dbt',
        profiles_dir='/usr/local/airflow/dags/dbt_model/cartiga_dbt_model/',
        dir='/usr/local/airflow/dags/dbt_model/cartiga_dbt_model/'
    )
