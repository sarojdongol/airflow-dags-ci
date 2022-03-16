import pytest
from airflow.models import DagBag
import os
import glob
import importlib.util
from airflow.models import DAG


def test_dagbag():
    '''
    purpose of this test to assert if there any import error on the dags
    '''
    dag_bag = DagBag(include_examples=False)
    assert not dag_bag.import_errors