##

# Stream and Batch Processing of Intricate Users App Data

# Introduction
The best way to get a good understanding of any topic is to try it out and build something with it. Following this approach, to understand building a data processing pipeline I build my own. Based on data from an open-source platform such as kaggle and python faker library that together have been modified a little to enable joins.

The objective of the project is,
1. Build and understand a data processing framework used for stream and batch data loading by companies
2. Setup and understand cloud components involved in data streaming and batch processing (API gateway, kinesis, lambda, S3, Redshift)
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
For this project, I will assume I work for a user behavior analytics company that for streaming purpose continuously in real-time collecting users app data and for the batch purpose collecting users app data end of the day from different data sources and joins them together to get a broader understanding of the customers. As a comapny, we target both app users and app developers with different services. These services can vary based on custmers and app developers requirement. One of the most valuable service my comapny provide to app users is recommandation app in real time based on the app they downloaded. One the other side, app developers can asked for anlaytics about users app download dehaviour based on their age, location, category of app, and time they spent on each apps. Based on this, I have set some goals around this project.

- Create a data pipeline which can help data scientist to access data fast and accurately to develop their recommendation app charts algorithm for users
- Create a data pipeline that can provide fault-tolerant data to draw analytics based on app developers requirement

# The Data Set
The source of the part of this dataset is kaggle. The link is attached here. https://www.kaggle.com/lava18/google-play-store-apps
The kaggle dataset provides detailed information about the Google Play Store apps. See googleplaystore.csv in my GitHub repository.

![](Images/KaggleDataset.png)

In order to make this dataset more interesting, I've merged a new user details dataset to the Google Play Store app dataset. The user details are generated from the faker library of Python.
For the batch processing, the user details dataset include details about 200 users. The user details include user_id, user_name, user_location, and the amount of time (in minute) user spent on the each app. 
For the stream processing, the user details dataset include details about 1000 users. The user details include user_id, user_name, and user_location.  

The user details are randomly distributed over the Google Play Store app dataset. Below, you can see part of the fake user's details dataset.

![](Images/FakeUserDataset.png)


Apart from this, a new column download_date is added to the dataset. 
For the Batch processing, we assume that the different Google Play Store apps have been downloaded by different users between 01-01-2020 and 01-01-2021. 
For stream processing, we assume that the download date is today and data is reaching to API end point on real time.

After merging all the dataset together, the dataset used for stream processing called "users_app_data_stream" and for batch processing called "users_app_data_batch".

users_app_data_stream
add data set here.

users_app_data_stream
add data set here

- Why did I choose, and what did I like in this dataset?

As described in the project overview section, as an analytics-based company, we like to explore users behavior and want to make their app experience better. The kaggle dataset provide me detailed information about multiple apps. The apps are precisely distrubted in different app categories, which helps us to compare different apps based on their rating, reviews, installs, and updates.

- What is problematic?

In this dataset most of the app type is free. Basically, most of the app mentioned in this dataset belongs to the free tier type and very few apps are paid type, which makes hard to understand that users buys app or not!!!!

# Data Cleaning and Preprocessing

Once the "users_app_data_stream" and "users_app_data_batch" are ready, it's time to make sure that the data is ready enough for streaming and batch processing. 

In real life, data is reaching on the API endpoint or any cloud database might include many nun, duplicates or unexpexted data types in it. Comapnies implemented different staratgy to tackle this issue. Below, I will describe how I manages this issue.

- Data Duplicates

The kaggle google data set include many duplicate entries but once the fake user dataset merged in it, all data rows become unique. Hence, we don't have duplicate data in our final dataset.

- Data Cleaning

By running a simple python code on the user's app data I identify the data to include Nun in some rows. In the scenario of streaming, we will configure the API end point to validate data. If the data include nun rows, the API end point will reject the data. However, the dataset include an exception, for the rating column which also includes multiple nun values, I made sure the rating is always filled with some values. In order to fill this values I took the median of rating column and filled the nun values.

![](Images/FillNan.png)

- Data Preprocessing

In the data preprocessing stage, the data type of the different column is changed based on the type of data column persist. For example, the column "last_updated" type is changed to DateTime and the date order is changed to year-month-date.

![](Images/users_app_datatype.png)


# Used Tools
The data pipeline will build around multiple tools. These tools can be categorized based on their functionality. Below you can see the platform design for streaming processing.

![](Images/PlateformDesign.png)

Below each functionality is described with used tools in detail.  

## Client
In this project, the data available for batch and stream processing at the client location is in .csv format. The .csv data will be read by python to post data on the API endpoint.

In the case of stream processing, the python script (see insert_data_to_api.py in the repository) read the data from the users_app_details_stream.csv dataset, convert it to JSON format and POST it to the provided API endpoint.

In the case of batch processing,.............

## Connect
In the scenario of stream processing, a data pipeline will pull data from an API and send data to the buffer. AWS API Gateway POST method is used to pull data from the client. Every time data will reach to the API endpoint, it will trigger the lambda function and send data to AWS Kinesis. 

In the scenario of batch processing,............ 

## Buffer
The two most discussed message queue tools are AWS Kinesis and Kinesis firehose. We will use Kinesis in stream processing to queue the data. The data will lineup in Kinesis every time the API endpoint trigger the lambda function in the AWS.

## Processing
AWS lambda is used to perform stream processing at different stages. The lambda is used to send data from API to Kinesis, Kinesis to S3 bucket, Kinesis to DynamoDB.

In case of batch processing, AWS Glue is used to perform ETL jobs. Glue take the data from S3 bucket, transform it and, and upload it into redshift schema.

## Storage
In the case of stream processing, the service for storing purpose we want to use to hold and store the raw stream data of varying sizes is S3, DynamoDB and Redshift. S3 stands for simple storage service, and it works as a data lake in an AWS environment. S3 will store the data in JSON format. Later the data can be used according to required applications. DynamoDB is a NoSQL database and saving the user's app data in wide column format. AWS redshift is a data warehouse. Redshift allows us to create schema inside its cluster and saved streamed data in a table.

In case batch processing,........

## Visualization
Postman REST API is used to print the data based on input user_id. REST API GET method allows us to call database. Here, we are extracting the data from the DynamoDB.
Apart from it, as a BI tool, Looker is used to performing analytics on data. The Looker is connected to Redshift.

# Pipelines

- Explain the pipelines for processing that you are building
- Go through your development and add your source code

## Stream Processing
For ease of implementation and testing, we will build the data pipeline in stages. There are 5 stages and these 5 stages shown below.

![](Images/DataPipelineDesign.png)



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
