import pandas as pd
import requests
import sched
import time

# Read the testfile
data = pd.read_csv(
    '/Users/ketansahu/Documents/DataEngineeringProject/GitHubRepo/users_app_data_stream.csv', sep=',')
print(data)
