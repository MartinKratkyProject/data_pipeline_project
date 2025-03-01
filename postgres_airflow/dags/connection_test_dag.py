from airflow import DAG
from datetime import datetime, timedelta
import psycopg2
from airflow.operators.python import PythonOperator
import os

default_args = {
    "owner": "martin_kratky",
    "start_date": datetime(2025, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "depends_on_past": False,
}

def make_conn_to_postgres():
    conn = psycopg2.connect(
        dbname="postgres", 
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432",
        # dbname=os.getenv("POSTGRES_DATABASE"), 
        # user=os.getenv("POSTGRES_USER"),
        # password=os.getenv("POSTGRES_PASSWORD"),
        # host=os.getenv("POSTGRES_HOST"),
        # port=os.getenv("POSTGRES_PORT"),
    )

    cur = conn.cursor()
    return conn, cur

def close_conn(conn, cur):
    cur.close()
    conn.close()

def run_query():
    conn, cur = make_conn_to_postgres()
    select_query = f"SELECT * FROM my_table;"

    cur.execute(select_query)
    results = cur.fetchmany(2)

    for row in results:
        print(row)
    
    close_conn(conn, cur)

with DAG(
    dag_id="TEST_DAG_connection_to_PG",
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=["database", "postgres"],
) as dag:

    run_query_task = PythonOperator(
        task_id="run_query",
        python_callable=run_query,
    )

    run_query_task