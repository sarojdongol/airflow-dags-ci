FROM apache/airflow:2.2.4
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install git -y
ENV GIT_PYTHON_REFRESH=quiet
