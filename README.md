## Fall2023_IDS706 Mini Project 11: Data Pipeline with Databricks
### by Jiayi Zhou
### Purpose
This is for class data engineering mini project 11: Data Pipeline with Databricks. It uses Databricks notebook and create a data pipeline using Databricks. As for one data sink, it utilizes Delta Lake for data storage. The data source is from [fivethirtyeight](https://github.com/fivethirtyeight/data/blob/master/womens-world-cup-predictions/wwc-matches-20150701-205548.csv).

### Functionality
The code does: ETL-Query: [E] Extract a dataset from URL, [T] Transform, and [L] Load into Delta Lake:
  * [E] Extract a dataset from a URL with CSV format.
  * [T] Transform the data with Spark SQL by combining two datasets and get the result ready for analysis.
  * [L] Load the transformed data into the destination data store using Delta Lake.

## Pipeline functionality:
<img width="747" alt="Screenshot 2023-11-11 at 8 19 56 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject3_JiayiZhou/assets/143651921/43cd8878-b99b-42c5-b12a-95caba28f62e">

## Check format and test errors
1. Open codespaces or run repo locally with terminal open 
2. Format code `make format`
3. Lint code `make lint`

