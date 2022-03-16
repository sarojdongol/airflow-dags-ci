"""
Following code is template file to run dbt jobs using dbt operators.
"""
from airflow import DAG
from airflow_dbt.operators.dbt_operator import (
    DbtRunOperator,
    DbtTestOperator
)
default_args = {
    'owner': 'dbtwarehouse',
    'retries': 0,
    'email': ['saroj.dongol@intellify.com.au'],
    'email_on_failure': True
}
with DAG(
    dag_id="DBT runner",
    description="Databricks silver Builder",
    schedule_interval="@daily",
    default_args=default_args
) as dag:

    dbt_run = DbtRunOperator(
        task_id='dbt_run'
    )

    dbt_test = DbtTestOperator(
        task_id='dbt_test'
    )

dbt_run >> dbt_test