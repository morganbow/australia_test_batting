# Australia Test Batting: Overview
My first project from scratch. I used Ken Jee's youtube series 'Data Science Project from Scratch' to help understand the structure of a data science project. the series is linked in my resources.
Scraped data off of cricinfo for Australia test batting stats. 
Cleaned the data and created further variables to analyse.
Found strong correlations between multiple variables.
Will create a model to try predict batting average from other independent variables such as HS, 50_convergences, etc

# Resources
Ken Jee's project from Scratch series: https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t \
Beautiful Soap tutorial: https://www.youtube.com/watch?v=XQgXKtPSzUI

# Code
Python 3.7\
Packages: pandas, numpy, matplotlib, seaborn

# Scraping data
This was my first solo data science project and therefore my first time scraping data. I used beautiful soap, which I learnt how to use from a Youtube video by Data Science Dojo that is linked in my resources.
The scraping was successful apart from the headers didn't appear as I hoped, so I entered them manually.

# Data Cleaning
Created new variables: Career Length, Career Midpont, Matches per Year, 50convergence ratio.
Removed 0 innings data. 
Removed data with no average.
Removed the not out sign from high scores to make the data an int.

# EDA
Most of the histograms for the data seemed to show that the data is exponentially distributed, the 'Average' variable however looked to be normally distributed when the outliers in the data were removed from the histogram. I looked into the data and realised a strong correlation between many of the variables. I also put some of the continous data into ranges to look at some pivot tables. Finally I looked at some scatter plots of the variable 'Average' against some of the variables I will look to model it against. 






