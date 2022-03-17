"""
Following code is template file to run dbt jobs using dbt operators.
"""
from airflow import DAG
from airflow_dbt.operators.dbt_operator import (
    DbtRunOperator,
    DbtTestOperator
)
from airflow.operators.python_operator import PythonOperator
from git import Repo
import os
import logging
import shutil
from datetime import datetime


default_args = {
    'owner': 'dbtwarehouse',
    'retries': 0,
    'email': ['saroj.dongol@intellify.com.au'],
    'email_on_failure': True
}

def IsWorkspaceAvailable(workspace_name):
    check_result = os.path.isdir(workspace_name)
    if check_result == True:
        logging.info("Workspace Exists so removing it")
        shutil.rmtree(workspace_name)


def GitClone(git_url, user_name, access_token=None, branch_name=None):
    ''''''
    if access_token == None:
        raise Exception("Token cannot be None")
    else:
        IsWorkspaceAvailable("dbt_workspace")
        url_after_split = git_url.split("@")[1]
        Repo.clone_from(
            f"https://{user_name}:{access_token}@{url_after_split}",
            'dbt_workspace',
            branch=branch_name)


with DAG(
    dag_id="DBT_runner",
    description="Databricks silver Builder",
    start_date=datetime(2022, 3, 17),
    schedule_interval="@daily",
    default_args=default_args
) as dag:

    clone_dbt_repo = PythonOperator(task_id="clone_dbt_repo", python_callable=GitClone, op_kwargs={
            "git_url": "https://sarojdongol@bitbucket.org/cartiga/cartiga_dw.git",
            "user_name": "sarojdongol",
            "access_token": "zgqdr93kXMuVDcJrxDTQ",
            "branch_name": "silvertbl/accountfirm"

        })

clone_dbt_repo