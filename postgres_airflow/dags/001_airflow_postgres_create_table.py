from airflow import DAG
from datetime import datetime, timedelta
import psycopg2
import pandas as pd
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'admin',
    'start_date': datetime(2025, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
    'depends_on_past': False
}

# function for creating a connection to postgres
def create_connection_to_postgres():
    conn = psycopg2.connect(
        dbname="postgres", 
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432",
    )

    cur = conn.cursor()
    return conn, cur

# function for closing the connection
def close_connection(conn, cur):
    cur.close()
    conn.close()

# function for creating a table. Called by create_table_task task
def create_table():
    conn, cur = create_connection_to_postgres()
    create_table_query = f"""
        -- DROP TABLE IF EXISTS polygon_data;
        CREATE TABLE IF NOT EXISTS polygon_data (id INT, name VARCHAR);
        """
    
    cur.execute(create_table_query)
    conn.commit()

    close_connection(conn, cur)

# DAG
with DAG(
    dag_id = 'create_table_and_store_data',
    default_args = default_args,
    schedule = None,
    catchup = False,
    description = 'This DAG creates a table in PG and stores data from polygon API into it.',
    tags = ['database', 'postgres']
) as dag:
    
    # tasks
    create_table_task = PythonOperator(
        task_id = 'create_table',
        python_callable = create_table,
    )

    # dependencies
    create_table_task