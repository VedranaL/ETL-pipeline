# ETL-pipeline

This is my initial project about building an ETL-Pipeline.

# What is ETL-Pipeline?

ETL-Pipeline stands for Extract-Transform-Load. It's the set of processes used to move data from a source or multiple sources into a database such as a data warehouse.
In this example, I extracted the data from Redshift first, then I did some transformation:
remove duplicates, change the data type, ger rid of null values. The last step is upload the processed data to an AWS s3 bucket.
