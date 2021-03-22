##
<<<<<<< Updated upstream
# Fascinating Insight of Intricate Users App Data with Stream Processing

=======

# Title Of Your Project
Add a catchy title to your project. Something that people immediately know what you are doing
>>>>>>> Stashed changes

# Introduction & Goals
- Introduce your project to the reader
- Orient this section on the Table of contents
- Write this like an executive summary
  - With what data are you working
  - What tools are you using
  - What are you doing with these tools
  - Once you are finished add the conclusion here as well

# Contents

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


# The Data Set
The source of the part of this dataset is kaggle. The link is attched here. https://www.kaggle.com/lava18/google-play-store-apps
The kaggle dataset provides the details about the Google Playstore apps.
Screenshot 2021-03-20 at 7.47.37 PM![image](https://user-images.githubusercontent.com/36641367/111882339-58fd1900-89b5-11eb-9ff3-3cdec7dd34a4.png)

In order to make this dataset more interesting, I've merged a new user details dataset to Google Playstore app dataset. The user details are generated from the faker library of Python.
The user details dataset include details about 200 users. The user details include user_id, user_name, user_location, and the amount of time (in minute) user spent on the each app. The user detalis are randomly distributed over Google Play app dataset. 

Apart from this, a new column download_date is added in the dataset. By adding this new column download_date, we assume that the different Google Playstore apps have been used by different users in between 01-01-2020 and 01-01-2021.
Screenshot 2021-03-20 at 8.17.45 PM![image](https://user-images.githubusercontent.com/36641367/111883131-aed3c000-89b9-11eb-87cc-85be9ae0e730.png)

After merging all the dataset together, I called the dataset is "users app data".




- Explain the data set
- Why did you choose it?
- What do you like about it?
- What is problematic?
- What do you want to do with it?

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
