from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from sqlalchemy import create_engine
from airflow.models import Variable


default_args = {
    'owner': 'admin',
    'start_date': datetime(2025, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
    'depends_on_past': False
}

# function for creating a connection to postgres
def create_connection_to_postgres():
    postgres_connection = Variable.get("sqlalchemy_pg_conn")
    engine = create_engine(postgres_connection)

    return engine

# function for redeploying dependent views
def redeploy_views():
    engine = create_connection_to_postgres()

    tickers = Variable.get("tickers", deserialize_json=True)
    for ticker in tickers:
        engine.execute(f"""DROP VIEW IF EXISTS vw_{ticker};""")
        engine.execute(f"""CREATE OR REPLACE VIEW vw_{ticker} AS(
                            SELECT * FROM "{ticker}"
                        );""")

# DAG
with DAG(
    dag_id = 'redeploy_views',
    default_args = default_args,
    schedule = None,
    catchup = False,
    description = 'This DAG creates a new dependent views and copy data from source table.',
    tags = ['database', 'postgres']
) as dag:
    
    # tasks
    redeploy_views_task = PythonOperator(
        task_id = 'redeploy_views',
        python_callable = redeploy_views,
    )

    # dependencies
    redeploy_views_task