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
    'retry_delay': timedelta(minutes=1),
    'depends_on_past': False
}

# function for creating a connection to postgres
def create_connection_to_postgres():
    postgres_connection = Variable.get("sqlalchemy_pg_conn")
    engine = create_engine(postgres_connection)

    return engine

# function for fetching latest record from postgres. Called by fetch_latest_record_task task
def fetch_latest_record(table_name):
    engine = create_connection_to_postgres()
    
    sql_query = f"""SELECT timestamp FROM "{table_name}" ORDER BY 1 DESC LIMIT 1;"""
    print(sql_query)

    with engine.connect() as conn:
        latest_record = conn.execute(sql_query).fetchone()
        latest_record = latest_record[0] if latest_record else 1898786817 #Sun Mar 03 2030 16:46:57 GMT+0000
  
    return latest_record

# function for fetching data from polygon API. Called by fetch_data_task task
def fetch_data():
    
    polygon_api_key = Variable.get("polygon_api_key")
    client = RESTClient(polygon_api_key)

    indices = Variable.get("tickers", deserialize_json=True)
    for indice in indices:
        aggs = []
        today = datetime.now()
        start = today - timedelta(days=365)
        from_date = start.strftime('%Y-%m-%d')
        to_date = today.strftime('%Y-%m-%d')

        for day in client.get_aggs(ticker=indice, multiplier=1, timespan='day', from_= from_date, to= to_date):
            aggs.append(day)

        df = pd.DataFrame(aggs)

        latest_record = fetch_latest_record(indice)

        df_filtered = df[df['timestamp'] > latest_record]

        engine = create_connection_to_postgres()
        df_filtered.to_sql(indice, con=engine, if_exists='append', index=False)
# DAG
with DAG(
    dag_id = 'load_new_data',
    default_args = default_args,
    schedule='0 18 * * *',
    catchup = False,
    description = 'This DAG updates a table in PG and stores data from polygon API into it.',
    tags = ['database', 'postgres']
) as dag:
    
  
    fetch_data_task = PythonOperator(
        task_id = 'fetch_data',
        python_callable = fetch_data, 
    )

    # dependencies
    fetch_data_task