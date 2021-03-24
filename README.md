##

# Stream and Batch Processing of Intricate Users App Data

# Introduction
The best way to get a good understanding of any topic is to try it out and build something with it. Following this approach, to understand building an data processing pipeline I build my own. Based on data from open data sources such as kaggle and python faker library that togather have been modified a little to enable joins.

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
For this project I will assume I work for a user behavior analytics company that continiously in real time collecting users app data from different data sources and joins them together to get a broader understanding of the customers. As a comapny, we provide recommandation app charts to users and users app download dehaviour to different app comapnies based on their age, location, category of app, and time they spent on each apps. 

# The Data Set
The source of the part of this dataset is kaggle. The link is attched here. https://www.kaggle.com/lava18/google-play-store-apps
The kaggle dataset provides the detailed information about the Google Playstore apps.
Screenshot 2021-03-20 at 7.47.37 PM![image](https://user-images.githubusercontent.com/36641367/111882339-58fd1900-89b5-11eb-9ff3-3cdec7dd34a4.png)

In order to make this dataset more interesting, I've merged a new user details dataset to Google Playstore app dataset. The user details are generated from the faker library of Python.
The user details dataset include details about 200 users. The user details include user_id, user_name, user_location, and the amount of time (in minute) user spent on the each app. The user detalis are randomly distributed over Google Play app dataset. 

Apart from this, a new column download_date is added in the dataset. By adding this new column download_date, we assume that the different Google Playstore apps have been used by different users in between 01-01-2020 and 01-01-2021. We assume, the data is streaming from date 01-01-2020 to 01-01-2021.
Screenshot 2021-03-20 at 8.17.45 PM![image](https://user-images.githubusercontent.com/36641367/111883131-aed3c000-89b9-11eb-87cc-85be9ae0e730.png)

After merging all the dataset together, I called the dataset "users app data".

- Why did I choose and what did I like in this dataset?
As described in the project overview section, as a analytics based comapany, we like to explore users behaviour and want o make their app experinace better. The kaggle dataset provide me detailed information about multiple apps. The apps are precisely distrubted in different app categories, which helps us to comapre different apps based on their rating, reviews, installs, and updates. 

- What is problematic?
In this dataset most of the app type is free. Basically most of the app mentioned in this dataset belongs to free tier type and very few apps are paid type. which makes hard to understand that users buys app or not!!!!

# Used Tools
- Explain which tools do you use and why
- How do they work (don't go too deep into details, but add links)
- Why did you choose them
- How did you set them up

## Connect
## Buffer
## Processing
## Storage
## Visualization

# Pipelines
- Explain the pipelines for processing that you are building
- Go through your development and add your source code

## Stream Processing
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
Add the link to your LinkedIn Profile

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
