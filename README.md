# ETL-pipeline

This is my initial project about building an ETL-Pipeline.

# What is ETL-Pipeline?

ETL-Pipeline stands for Extract-Transform-Load. It's the set of processes used to move data from a source or multiple sources into a database such as a data warehouse.
In this example, I extracted the data from Redshift first, then I did some transformation:
remove duplicates, change the data type, get rid of null values. The last step is upload the processed data to an AWS s3 bucket.

# Requirements
The minimum requirements:

- Python 8+

# Instructions on how to execute the code
Make sure you are executing the code from the etl_pipeline folder.

Install all the libraries you will need to execute main.py. Please add python-dotenv to the requirements.txt.
  - pip install -r requirements.txt

Copy the .env.example file to .env and fill out the environment vars.

Run the main.py script. You will need to import dotenv and load the environment variables.

 - python main.py


# Requirements Docker
The minimum requirements:

Installation: Docker Desktop

Manual installation steps for older WSL version: Docker WSL 2

# Instructions on how to execute the code:

Copy the .env.example file to .env and fill out the environment vars.

Make sure you are executing the code from the etl_pipeline folder and you have Docker Desktop running.

To run it locally first build the image.

- docker image build -t etl-pipeline .
- 
Then run the etl job using docker:

  docker run --env-file .env etl-pipeline