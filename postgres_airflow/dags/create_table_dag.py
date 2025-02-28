from airflow import DAG
from datetime import datetime
import psycopg2
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
}

def create_table():
    conn = psycopg2.connect(
        dbname="postgres", 
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432",
    )
    
    cur = conn.cursor()
    
    # create_table_sql = """
    #     CREATE TABLE IF NOT EXISTS my_table (
    #         id SERIAL PRIMARY KEY,
    #         name VARCHAR(100),
    #         age INT
    #     );
    # """
    # cur.execute(create_table_sql)
    # conn.commit()

    select_query = "SELECT * FROM my_table;"

    cur.execute(select_query)
    results = cur.fetchall()
    for row in results:
        print(row)
    
    cur.close()
    conn.close()

with DAG(
    dag_id="create_table_dag_with_psycopg2",
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=["database", "postgres"],
) as dag:

    create_table_task = PythonOperator(
        task_id="create_table",
        python_callable=create_table,
    )

    create_table_task