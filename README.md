DOCUMENTATION

This project is a fully automated data engineering pipeline designed to extract stock market data from the Polygon API for Apple (AAPL), Amazon (AMZN), Google (GOOGL), Nvidia (NVDA), and Tesla (TSLA). The extracted data is processed and stored in a PostgreSQL database using Apache Airflow, ensuring efficient data management and scheduling.

To enhance scalability and maintainability, the entire ETL pipeline is containerized using Docker. Additional services such as pgAdmin, Redis, and Flower are integrated to monitor and manage the workflow, providing a robust infrastructure for data processing. As a result, this pipeline autonomously fetches and stores stock market data in the PostgreSQL database on a daily basis without requiring manual intervention.

The second part of this project is a full-stack web application that utilizes the PostgreSQL database populated by the data pipeline. The backend is built using Flask and is responsible for fetching the stored stock data and exposing it through API endpoints. To ensure a stable and efficient connection to the database, the backend leverages libraries such as psycopg2-binary and Flask-SQLAlchemy. This allows the application to seamlessly retrieve and serve the stock data to users, providing a reliable interface for accessing market insights.


ETL Pipeline Architecture

Technology      > Purpose

Apache Airflow  > Orchestrating ETL workflows;
Polygon API     > Fetching stock market data;
PostgreSQL      > Storing processed data;
Docker          > Containerizing services;
pgAdmin         > Managing PostgreSQL database;
Redis           > Message broker for Airflow;
Flower          > Monitoring Airflow tasks;

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
    001_airflow_postgres_redeploy_views.py  → Redeploys views with the latest and transformed data.


Project Setup & Installation

🔹 Prerequisites: Install Docker & Docker Compose; Get a Polygon API key

Those are the only requirements for this project to be fully functional. 
Once you have this setup ready, proceed with these steps:

1 🔹 Clone the Repository (main branch)

2 🔹 Open \data_pipeline_project\postgres_airflow\scripts\create_connections.sh file and replace your_polygon_api_key with your actual Polygon API key. 

3 🔹 Start Services using Docker Compose (docker compose up --build)

Service credencials:
pgAdmin: http://localhost:5050 (User=admin@admin.com, Password=admin)
PG server (password=airflow)
Airflow UI: http://localhost:8080 (User=airflow, Password=airflow)



Troubleshooting 

Here are some tips to help you troubleshoot potential issues when running this project.

1. Data not available in UI.
    In case you opend the frontend webpage (http://localhost:8081/) and you don't see any data, only the message "Loading stock data...", go to http://localhost:8080/dags/load_new_data/grid and trigger this DAG manually. 
    (This may happen if you are using the default, free of charge Polygon API key due to number of connections restriction. You can also encounter this issue when you are running the project for the first time).
2. Missing variables and connections in Airflow UI.
    Sometimes, the Airflow instance is created without necessary variables and connections. In this case, go to \data_pipeline_project\postgres_airflow\scripts\create_connections.sh file and make sure it's using LF end of the line sequence instead of CRLF. After you do the change, run docker build command again.