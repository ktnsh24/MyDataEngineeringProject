#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import requests
import sched, time
s = sched.scheduler(time.time, time.sleep)


# write all the rows from users_app_data_stream to the api as PUT request
def sample_function(sc):

    myURL = "https://zp91xerpvb.execute-api.us-east-1.amazonaws.com/prod_temp/my-first-api"

    # Read the testfile
    data = pd.read_csv(
        '/Users/ketansahu/Documents/DataEngineeringProject/GitHubRepo/users_app_data_stream.csv', sep=',')
    for i in data.index:
        #print(i)
        try:
            # convert the row to json
            export = data.loc[i].to_json()

            # send it to the api
            response = requests.post(myURL, data=export)

            # print the returncode
            print(export)
            print(response)
        except:
            print(data.loc[i])
    s.enter(60, 1, sample_function, (sc,))
    
    
s.enter(60, 1, sample_function, (s,))
print("data is send")
s.run()

