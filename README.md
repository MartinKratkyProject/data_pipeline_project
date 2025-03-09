DOCUMENTATION

This project is a fully automated data engineering pipeline designed to extract stock market data from the Polygon API for Apple (AAPL), Amazon (AMZN), Google (GOOGL), Nvidia (NVDA), and Tesla (TSLA). The extracted data is processed and stored in a PostgreSQL database using Apache Airflow, ensuring efficient data management and scheduling.

To enhance scalability and maintainability, the entire ETL pipeline is containerized using Docker. Additional services such as pgAdmin, Redis, and Flower are integrated to monitor and manage the workflow, providing a robust infrastructure for data processing. As a result, this pipeline autonomously fetches and stores stock market data in the PostgreSQL database on a daily basis without requiring manual intervention.

The second part of this project is a full-stack web application that utilizes the PostgreSQL database populated by the data pipeline. The backend is built using Flask and is responsible for fetching the stored stock data and exposing it through API endpoints. To ensure a stable and efficient connection to the database, the backend leverages libraries such as psycopg2-binary and Flask-SQLAlchemy. This allows the application to seamlessly retrieve and serve the stock data to clients, providing a reliable interface for accessing market insights.


ETL Pipeline Architecture

Technology      Purpose

Apache Airflow  Orchestrating ETL workflows
Polygon API     Fetching stock market data
PostgreSQL      Storing processed data
Docker          Containerizing services
pgAdmin         Managing PostgreSQL database
Redis           Message broker for Airflow
Flower          Monitoring Airflow tasks

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


Backend Structure
# here will be technical documentation of the backend app......


Project Setup & Installation

🔹 Prerequisites: Install Docker & Docker Compose; Get a Polygon API key

1 🔹 Clone the Repository (main branch)

2 🔹 Start Services using Docker Compose

3 🔹  Access the Services

🔹 pgAdmin: http://localhost:5050 (User: admin@example.com, Password: admin)

 🔹   Create a new server:
        NAME: postgres_test,
        HOST: postgres,
        PORT: 5432,
        DATABASE: airflow,
        USERNAME: airflow,
        PASSWORD: airflow

🔹 Airflow UI: http://localhost:8080 (User: airflow, Password: airflow)

 🔹   Create a new connection: postgres:
        Connection Id: postgres_default,
        Connection Type: Postgres,
        Host: postgres,
        Database: airflow,
        Login: airflow,
        Password: airflow,
        Port: 5432

  🔹  redis:
        Connection Id: redis_default,
        Connection Type: Redis,
        Host: redis,
        Login: ,
        Password: ,
        Port: 6379

  🔹  Create new variables:
        polygon_api_key     >  your_api_key ,
        sqlalchemy_pg_conn  > postgresql+psycopg2://airflow:airflow@postgres:5432/postgres ,
        tickers             >  ["AAPL", "TSLA", "NVDA", "GOOGL", "AMZN"]