import datetime
import os
from airflow import DAG
from airflow.contrib.operators.ecs_operator import ECSOperator

dag = DAG(
    dag_id="ecs_fargate_dag",
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
    },
    default_view="graph",
    schedule_interval=None,
    start_date=datetime.datetime(2020, 1, 1),
    tags=["example"],
)

# generate dag documentation
dag.doc_md = __doc__
# [START howto_operator_ecs]
hello_world = ECSOperator(
    task_id="hello_world",
    dag=dag,
    cluster="dbtrunner",
    task_definition="mlserviceTaskDefinition:39",
    launch_type="FARGATE",
    overrides={
        "containerOverrides": [],
    },
    network_configuration={
        "awsvpcConfiguration": {
            "securityGroups": ["sg-05d7d142199ea6d7a"],
            "subnets": ["subnet-095d01e7cf71a15e0", "subnet-07acea5008ff2050f"],
        },
    },
    tags={
        "Customer": "X",
        "Project": "Y",
        "Application": "Z",
        "Version": "0.0.1",
        "Environment": "Development",
    },
    awslogs_group="/aws/ecs/dbtrunner",
    awslogs_stream_prefix="/ecs/dbtrunner",  # replace with your container name
)

hello_world