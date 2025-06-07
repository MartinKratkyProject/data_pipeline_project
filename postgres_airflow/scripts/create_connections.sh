#!/bin/bash

echo "Waiting for Airflow DB to be ready..."
airflow db upgrade

echo "Unpausing DAGs..."

airflow dags unpause create_table_and_store_data
airflow dags unpause load_new_data
airflow dags unpause redeploy_views

if ! airflow connections get 'postgres_default' &>/dev/null; then
    echo "Creating Postgres connection..."
    airflow connections add 'postgres_default' \
        --conn-uri 'postgresql+psycopg2://airflow:airflow@postgres:5432/airflow'
else
    echo "Postgres connection already exists"
fi

if ! airflow connections get 'redis_default' &>/dev/null; then
    echo "Creating Redis connection..."
    airflow connections add 'redis_default' \
        --conn-uri 'redis://redis:6379'
else
    echo "Redis connection already exists"
fi

echo "Airflow connections ensured!"

echo "Setting Airflow Variables..."

airflow variables set polygon_api_key "your_polygon_api_key"

airflow variables set sqlalchemy_pg_conn "postgresql+psycopg2://airflow:airflow@postgres:5432/postgres"

airflow variables set tickers '["AAPL", "TSLA", "NVDA", "GOOGL", "AMZN"]'

echo "Airflow Variables set!"