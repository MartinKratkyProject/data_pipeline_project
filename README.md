# data_pipeline_project

This is a data pipeline project.

1. Select the purpouse of this project. (What data will I gather...)    |  ETA - 23.2.  Done 18.2.
2. Find a good source of data (.csv, .excl, url).                       |  ETA - 2.3.   Done 18.2.
3. Set up airflow for scheduling ETL/ELT pipelines.                     |               Done 9.2. 
    -   set up docker                                                     
        -   set up WSL2
4. Store data in PostgreSQL DB.                                         |  ETA - 9.3.   Done 23.2.
    -   set up PostgreSQL DB.

    PREPARATION: 
        -   both services (airflow and postgres) will run on separate containers using docker. 
        -   docker-compose.yaml: The first step will be creating a docker-compose.yaml file with 3 services - postgres, airflow and additional pgAdmin. 
        -   NOTE: probably the backend and frontend applications will be running on separate containers. 
    PREREQUISITIES: 
        -   create a new empty folders in D: disk for storing the data from postgres. Volumes in yaml file will be bind to these files (one folder might be enought).

5. Test ETL/ELT pipelines.                                              |  ETA - 23.3.  Done 27.2.
5.1. Store actual polygon data in postres using dags.                   |  ETA - 23.3.      
6. Prepare Flask application for backend.                               |  ETA - 6.4.
    -   set up flask application in python
    -   create connection with backend and database
    -   test connection
7. Prepare frontend appliation with .Vue                                |  ETA - 4.5.
8. Test project                                                         |  ETA - 25.5.
9. Deploy project into www.                                             |  ETA - 8.6.


# ------------------------------------- DOCUMENTATION -------------------------------------

1. The purpose of this project is the demonstration of using different data engineering platforms in a single env, creating a robust and scalable structure for web designed app.
The app is meant to provide latest stock market data in forms of meaningful visualization.

2. For the stock market data, I choose to go with https://polygon.io/. Polygon web site provides large sets of different investment data. I decided to use data getting from 
available polygon API. 

