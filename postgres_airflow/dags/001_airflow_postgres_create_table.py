from airflow import DAG
from datetime import datetime, timedelta
import pandas as pd
from airflow.operators.python import PythonOperator
from polygon import RESTClient
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

# function for droping a table. Called by drop_table_task task
def drop_table():
    engine = create_connection_to_postgres()
    create_table_query = f"""
        DROP TABLE IF EXISTS polygon_data CASCADE;
        """
    
    with engine.connect() as conn:
        conn.execute(create_table_query)

# function for fetching data from polygon API. Called by fetch_data_task task
def fetch_data():
    engine = create_connection_to_postgres()
    polygon_api_key = 'rZAf7cgy4CA0Fa_Z78cfyKJlBJJG1VNP'
    client = RESTClient(polygon_api_key)
    ticker = 'SPY'
    aggs = []

    today = datetime.now()
    start = today - timedelta(days=730)
    from_date = start.strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    for day in client.get_aggs(ticker=ticker, multiplier=1, timespan='day', from_= from_date, to= to_date):
        aggs.append(day)

    df = pd.DataFrame(aggs)
    df.to_sql('polygon_data', con=engine, if_exists='append')

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
    drop_table_task = PythonOperator(
        task_id = 'drop_table',
        python_callable = drop_table,
    )

    fetch_data_task = PythonOperator(
        task_id = 'fetch_data',
        python_callable = fetch_data,    
    )

    # dependencies
    drop_table_task >> fetch_data_task