## Fall2023_IDS706 Individual Project 3: Databricks ETL (Extract Transform Load) Pipeline
### by Jiayi Zhou [![CI](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject3_JiayiZhou/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject3_JiayiZhou/actions/workflows/cicd.yml)
### Purpose
This is for class data engineering individual project 3: Databricks ETL (Extract Transform Load) Pipeline. It uses Databricks notebook that performs ETL (Extract, Transform, Load) operations, checked into the repository. It utilizes Delta Lake for data storage, Spark SQL for data transformations, and automated trigger to initiate the pipeline.

### Video
[YouTube]()

### Functionality
The code does: ETL-Query: [E] Extract a dataset from URL, [T] Transform, and [L] Load into Delta Lake:
  * [E] Extract a dataset from a URL with CSV format.
  * [T] Transform the data with Spark SQL by combining two datasets and get the result ready for analysis.
  * [L] Load the transformed data into the destination data store using Delta Lake.

**Key Components:**
1. **Data Extraction:**
   - Utilizes the `requests` library to fetch data from specified URLs.
   - Downloads and stores the data in the Databricks FileStore.

2. **Databricks Environment Setup:**
   - Establishes a connection to the Databricks environment using environment variables for authentication (SERVER_HOSTNAME and ACCESS_TOKEN).

3. **Data Transformation and Load**
    - Transform the csv file into a Spark dataframe which is then converted into a Delta Lake Table and stored in the Databricks environement

4. **Query Transformation and Vizulization:**
   - Defines a Spark SQL query to perform a predefined transformation on the retrieved data.
   - Uses the predifined transformation Spark dataframe to create vizualizations

**Preparation:**
1. Create a Databricks workspace on Azure 
2. Connect Github account to Databricks Workspace 
3. Create global init script for cluster start to store enviornment variables 
4. Create a Databricks cluster that supports Pyspark 
5. Clone repo into Databricks workspace 
6. Create a job on Databricks to build pipeline 
7. Extract task (Data Source): `mylib/extract.py`
8. Transform and Load Task (Data Sink): `mylib/transform.py`
9. Query and Viz Task: `mylib/query_viz.py`

## Job Run from Automated Trigger:
<img width="747" alt="Screenshot 2023-11-11 at 8 19 56 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject3_JiayiZhou/assets/143651921/43cd8878-b99b-42c5-b12a-95caba28f62e">

## Check format and test errors
1. Open codespaces or run repo locally with terminal open 
2. Format code `make format`
3. Lint code `make lint`

## Sample Viz from Query:
<img width="720" alt="Screenshot 2023-11-11 at 7 35 46 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject3_JiayiZhou/assets/143651921/8f95409c-e213-40dc-b386-87ac8b3f0b1d">

