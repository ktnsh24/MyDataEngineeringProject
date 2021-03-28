##

# Stream and Batch Processing of Intricate Users App Data

# Introduction
The best way to get a good understanding of any topic is to try it out and build something with it. Following this approach, to understand building an data processing pipeline I build my own. Based on data from open source plateform such as kaggle and python faker library that togather have been modified a little to enable joins.

The objective of the project is,
1. Build and understand a data processing framework used for stream and batch data loading by comapanies
2. Setup and understand cloud componanets involved in data streaming and batch processing (API gateway, kinesis, lambda, S3, Redshift)
3. Understand how to spot failure points in an data processing pipeline and how to build systems resistant to failures and errors
4. Understand how to approach or build an data processing pipeline from the ground up

# Contents
- [Project Overview and Goals](#Project-Overview-and-Goals)
- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
    - [Storing Data Stream](#storing-data-stream)
    - [Processing Data Stream](#processing-data-stream)
  - [Batch Processing](#batch-processing)
  - [Visualizations](#visualizations)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# Project Overview and Goals
For this project I will assume I work for a user behavior analytics company that for streaming purpose continiously in real time collecting users app data and for batch purpose collecting users app data end of the day from different data sources and joins them together to get a broader understanding of the customers. As a comapny, we target both app users and app developers with different services. These services can vary based on custmers and app developers requirement. One of the most valuable service my comapny provide to app users is recommandation app charts to users, so they can get diffrent choices of apps based on their past app use history. One the other side, ap developers can asked for anlaytics about users app download dehaviour based on their age, location, category of app, and time they spent on each apps. Based on this, I have set some goals around this project.

- Create a data pipeline which can help data scientist to access data fast and accuratley to develope their recommandation app charts algorithm for users
- Cretae a data pipeline which can provide data to draw analytics based on app developers requirement.

# The Data Set
The source of the part of this dataset is kaggle. The link is attched here. https://www.kaggle.com/lava18/google-play-store-apps
The kaggle dataset provides the detailed information about the Google Playstore apps. See googleplaystore.csv in my github repository.

[image](https://user-images.githubusercontent.com/36641367/111882339-58fd1900-89b5-11eb-9ff3-3cdec7dd34a4.png)

In order to make this dataset more interesting, I've merged a new user details dataset to Google Playstore app dataset. The user details are generated from the faker library of Python.
For the batch processing, the user details dataset include details about 200 users. The user details include user_id, user_name, user_location, and the amount of time (in minute) user spent on the each app. 
For the stream processing, the user details dataset include details about 1000 users. The user details include user_id, user_name, and user_location. 

The user detalis are randomly distributed over Google Play app dataset. Below, you can see part of the fake users details dataset.
Screenshot 2021-03-28 at 11.07.09 AM![image](https://user-images.githubusercontent.com/36641367/112747458-fd82ea80-8fb5-11eb-9f06-d48173562e87.png)

Apart from this, a new column download_date is added in the dataset. 
For the Batch processing, we assume that the different Google Playstore apps have been downloaded by different users in between 01-01-2020 and 01-01-2021. 
For stream processing, we assume that the download date is today and data is reaching to API end point on real time.
[image](https://user-images.githubusercontent.com/36641367/111883131-aed3c000-89b9-11eb-87cc-85be9ae0e730.png)

After merging all the dataset together, the dataset used for stream processing called "users_app_data_stream" and for batch processing called "users_app_data_batch".

- Why did I choose and what did I like in this dataset?

As described in the project overview section, as a analytics based comapany, we like to explore users behaviour and want to make their app experinace better. The kaggle dataset provide me detailed information about multiple apps. The apps are precisely distrubted in different app categories, which helps us to compare different apps based on their rating, reviews, installs, and updates. 

- What is problematic?

In this dataset most of the app type is free. Basically most of the app mentioned in this dataset belongs to free tier type and very few apps are paid type. which makes hard to understand that users buys app or not!!!!

# Data Cleaning and Preprocessing

Once the "users_app_data_stream" and "users_app_data_batch" are ready, it's a time to make sure that the data is ready enough for streaming and batch processing. 

In real life, data is reaching on API end point or any cloud database might incluse many nun, duplicates or unexpexted data types in it. Comapnies implemented different staratgy to tackle this issue. Below, I will describe how I manages this issue.

- Data Duplicates

The kaggle google data set include many duplicate entries but once the fake user dataset merged in it, all data rows become unique. Hence we don't have duplicate data in our final dataset.

- Data Cleaning

By running a simple pyhton code on the users app data I identify the data include nun in some rows. In the scenario of streaming, we will configure API end point to validate data. if the data include nun rows, the API end point will reject the data. However dataset include an exception, for the rating column which also include multiple nun values, I made sure the rating is always filled with some values. In order to fill this values I took the median of rating column and filled the nun values.
[image](https://user-images.githubusercontent.com/36641367/112536743-233da300-8dae-11eb-84c9-cf60f0114ecd.png)

- Data Preprocessing

In the data preprocessing stage, the data type of the different column is changed based on the type of data column persist. For example, column "last_updated" type is changed to datetime and the date order is changed to year-month-date.
Screenshot 2021-03-28 at 10.30.02 AM![image](https://user-images.githubusercontent.com/36641367/112746682-c6f6a100-8fb0-11eb-970c-6f3556c61a50.png)

# Used Tools
The data pipeline will build around mulitle tools. These tools can be categorised based on their functionality. Below you can see plateform design for streaming processing.
Plateform Design![image](https://user-images.githubusercontent.com/36641367/112756166-4356a780-8fe4-11eb-9bfa-00ee6608f359.png)

Below each funcationality is described with tools in detail. 

- Explain which tools do you use and why
- How do they work (don't go too deep into details, but add links)
- Why did you choose them
- How did you set them up

## Client
In this project, the data avilable for batch and stream processing at the client location is in .csv format. The .csv data will be read by python to post data on API endpoit.

In case of stream processing, the python script (see insert_data_to_api.py in repository) read the data from users_app_details_stream.csv dataset, convert it to JSON format and POST it provided API end Point.

In case of batch processing.............

## Connect
In the scenario of stream processing, the connect data pipeline will pull data from a API and send data to buffer. AWS API Gateway Post method is used to pull data from client. Everytime data will reach on API end point, it will trigger the lambda function and send data to AWS Kinesis. ............ 

## Buffer
Two most discussed message queue tools are AWS Kinesis and Kinesis firehose. We will use Kinesis to queue the data. The data will lineup in Kinesis everytime API end point trigger the lambda function in the AWS.
## Processing
## Storage
In this application, the service for storing purpose we want to use to hold and store the raw stream data of varying sizes is S3. S3 stands for simple storage service.
## Visualization

# Pipelines

- Explain the pipelines for processing that you are building
- Go through your development and add your source code

## Stream Processing
For ease of implementation and testing, we will build the data pipeline in stages. There are 5 stages and these 5 stages shown below.
DataPipelineDesign![image](https://user-images.githubusercontent.com/36641367/112758625-97b35480-8fef-11eb-899f-fe151b8be046.png)


### Storing Data Stream
### Processing Data Stream
## Batch Processing
## Visualizations

# Demo
- You could add a demo video here
- Or link to your presentation video of the project

# Conclusion
Write a comprehensive conclusion.
- How did this project turn out
- What major things have you learned
- What were the biggest challenges

# Follow Me On
https://www.linkedin.com/in/ketan-sahu/

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
