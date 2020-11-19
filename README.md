# Salary Estimator - Data Scientist vs Data Analyst: Project Overview
* Created a tool that estimates data scientists' and data analysts' salaries () to help job seekers understand and negatiate their income when they get a job
* Scarped over 2000 jobs descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, spark, and sql.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask



# Code and Resources Used
**Python Version:** 3.8

**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

**For Web Framework Requirements:** ```pip install -r requirements.txt```

**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium

**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

# Web Scraping
Adjusted the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com/  With each job, we got the follow:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

# Data Cleaning
After scraping the data, I needed to clean the data so that it was usable for my model.  I made the following changes and created the following variables:
* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Parsed rating out of company text
* Made a new column for company state
* Transformed founded date into age of the company
* Made columns for if different skills were listed in the job description:
  * Python
  * Excel
  * AWS
  * Spark
  * SQL
* Column for simplified job title and seniority
* Column for description length

# EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

### Data Scientist
![alt text](https://github.com/nelsonhwu/ds_salary_proj/blob/master/Images/Data_Scientist/avg_salary_by_job_simp.png "Avg Salary by Simplified Job Title")
![alt text](https://github.com/nelsonhwu/ds_salary_proj/blob/master/Images/Data_Scientist/graph_for_job_state.png "Number of Jobs by State")
![alt text](https://github.com/nelsonhwu/ds_salary_proj/blob/master/Images/Data_Scientist/corr_heatmap.png "Correlation Heat Map")
![alt text](https://github.com/nelsonhwu/ds_salary_proj/blob/master/Images/Data_Scientist/word_cloud.png "Job Description Word Cloud")

### Data Analyst
