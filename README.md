# data_pipeline_project

This is a data pipeline project.

1. Select the purpouse of this project. (What data will I gather...)    |  ETA - 23.2.  Done 18.2.
2. Find a good source of data (.csv, .excl, url).                       |  ETA - 2.3.   Done 18.2.
3. Set up airflow for scheduling ETL/ELT pipelines.                     |               Done 9.2. 
    -   set up docker                                                     
        -   set up WSL2
4. Store data in PostgreSQL DB.                                         |  ETA - 9.3.
    -   set up PostgreSQL DB.

    PREPARATION: 
        -   both services (airflow and postgres) will run on separate containers using docker. 
        -   docker-compose.yaml: The first step will be creating a docker-compose.yaml file with 3 services - postgres, airflow and additional pgAdmin. 
        -   NOTE: probably the backend and frontend applications will be running on separate containers. 
    PREREQUISITIES: 
        -   create a new empty folders in D: disk for storing the data from postgres. Volumes in yaml file will be bind to these files (one folder might be enought).

5. Test ETL/ELT pipelines.                                              |  ETA - 23.3.
6. Prepare Flask application for backend.                               |  ETA - 6.4.
    -   set up flask application in python
    -   create connection with backend and database
    -   test connection
7. Prepare frontend appliation with .Vue                                |  ETA - 4.5.
8. Test project                                                         |  ETA - 25.5.
9. Deploy project into www.                                             |  ETA - 8.6.