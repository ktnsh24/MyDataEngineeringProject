# import all libraries
import awswrangler as wr
import pandas as pd
import boto3
import pytz
import os
import numpy as np
import pandas as pd
import datetime
import time
from datetime import datetime
from collections import defaultdict
import json


# Read data from S3 "users-app-batch-client-data/incoming_client_data" bucket.
incoming_client_data_path = f"s3://users-app-batch-client-data/incoming_client_data/users_app_batch_client_data.csv"
users_app_data = wr.s3.read_csv([incoming_client_data_path])

# Data Processing
# converting last date
users_app_data['last_updated'] = pd.to_datetime(users_app_data['last_updated'])
users_app_data['last_updated'] = users_app_data['last_updated'].dt.strftime(
    '%Y-%m-%d')
users_app_data['last_updated'] = users_app_data['last_updated'].astype(
    'datetime64[ns]')

# convert datatype to integer
users_app_data['rating'] = pd.to_numeric(
    users_app_data['rating'], errors='coerce')
users_app_data['reviews'] = pd.to_numeric(
    users_app_data['reviews'], errors='coerce')
users_app_data['installs'] = users_app_data['installs'].str.replace(
    ',', '').str.replace('+', '').astype('int')
users_app_data['app_size'] = users_app_data['app_size'].str.replace(
    'M', 'e+6').str.replace('k', 'e+3').str.replace('Varies with device', '0').astype('float')
users_app_data['price'] = users_app_data['price'].str.replace(
    '$', '').astype('float')

# write data to S3 "users-app-batch-client-data/processed_client_data" bucket
#processed_client_data_path = f"s3://users-app-batch-client-data/processed_client_data/processed_users_app_batch_client_data.csv"
#wr.s3.to_csv(users_app_data, processed_client_data_path, index=False)
