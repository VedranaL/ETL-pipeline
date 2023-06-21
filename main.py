import os

#from dotenv import load_dotenv

from src.extract import extract_transaction_data
from src.transform import identify_and_remove_duplicated_data
from src.load_data_to_s3 import df_to_s3


#load_dotenv()
user = os.getenv("user")
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

# transforming data and connecting with redshift
online_trans_cleaned = extract_transaction_data(dbname, host, port, user, password)
print("Extraction completed")

# removing duplicates
online_trans_deduped = identify_and_remove_duplicated_data(online_trans_cleaned)
print("Removed duplicated data")

# load data to s3

s3_bucket="waia-data-dump"
key="bootcamp2/etl/vl_online_trans_cleaned.csv"

df_to_s3(online_trans_deduped, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)


