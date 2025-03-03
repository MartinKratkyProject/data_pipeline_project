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