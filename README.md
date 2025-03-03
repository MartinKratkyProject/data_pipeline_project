DOCUMENTATION

This project is a data engineering pipeline that extracts stock market data from the Polygon API for Apple (AAPL), Amazon (AMZN), Google (GOOGL), Nvidia (NVDA), and Tesla (TSLA). The data is processed and stored in a PostgreSQL database using Apache Airflow.
The ETL pipeline is containerized using Docker, and services such as pgAdmin, Redis, and Flower are used for monitoring and managing the workflow.

Technology      Purpose

Apache Airflow  Orchestrating ETL workflows
Polygon API     Fetching stock market data
PostgreSQL      Storing processed data
Docker          Containerizing services
pgAdmin         Managing PostgreSQL database
Redis           Message broker for Airflow
Flower          Monitoring Airflow tasks

ETL Pipeline Architecture

🔹 Step 1: Extraction
    Fetch historical stock data from Polygon API.
    Store raw data temporarily in Pandas DataFrame.

🔹 Step 2: Transformation
    Filter new data using the latest available timestamp from PostgreSQL.

🔹 Step 3: Loading
    Append new records into the PostgreSQL database.

🔹 Airflow DAGs
    001_airflow_postgres_create_table.py    → Fetches stock data and stores it in PostgreSQL.
    001_airflow_postgres_load_new_data.py   → Extracts and loads the latest stock data.


Project Setup & Installation

🔹 Prerequisites
    Install Docker & Docker Compose
    Get a Polygon API key

1   Clone the Repository
2   Start Services using Docker Compose
3   Access the Services
🔹 pgAdmin: http://localhost:5050 (User: admin@example.com, Password: admin)
    Create a new server:
        NAME: postgres_test
        HOST: postgres
        PORT: 5432
        DATABASE: airflow
        USERNAME: airflow
        PASSWORD: airflow 
🔹 Airflow UI: http://localhost:8080 (User: airflow, Password: airflow)
    Create a new connection: postgres
        Connection Id: postgres_default
        Connection Type: Postgres
        Host: postgres
        Database: airflow
        Login: airflow
        Password: airflow
        Port: 5432
    redis:
        Connection Id: redis_default
        Connection Type: Redis
        Host: redis
        Login:
        Password:
        Port: 6379
    Create new variables:
        Key                 Val
        polygon_api_key     your_api_key
        sqlalchemy_pg_conn  postgresql+psycopg2://airflow:airflow@postgres:5432/postgres
        tickers             ["AAPL", "TSLA", "NVDA", "GOOGL", "AMZN"]