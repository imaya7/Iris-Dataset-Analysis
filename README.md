# Iris-Dataset-Analysis
Exploring the Pandas Library

# Overview
This project is designed to analyze the Fisher's Iris data set, which contains data examined by Ronald Fisher on 3 different species of irises. The analysis was performed by merging two datasets containing petal and sepal measurements, the analysis included calculations over the average, median, and standard deviation. As well as the correlation between the different variables. This project also calculates the similarity between the species based on measurements. 

# Files Structure 
-  pandasAssignmnet.py - script analysis 
-  Petal_Data.csv -CSV containing petal measurements 
-  Sepal_data.csv -CSV containing sepal measurements

# Librarys 
- Pandas Library
- os Library

# Code Explanation 
The code starts by defining the file paths and then uses pandas to load the datasets, and then it merges the two datasets. The script then goes through the data and calculates the average, median, and standard deviation for each variable(the variables include petal length, petal width, sepal length, and sepal width for all the species. The code also calculates the correlation matrix for these variables. Additionally, the script calculates the similarities between each species by comparing the average values of each variable, the differences are summed to get the similarity score and sorted by least to most similar. Note the highest score = least similar and the lowest score = most similar. 

# Pandas Objects 
- pd - alias for pandas
- Dataframe - create dataframe
- Groupby -  created by grouping
- Series - dataframe resulting from calculations
  
# Pandas Methods 
- .read_csv - reads csv into dataframe
- .merge -merges two dataframes
- .mean - calculates mean 
- .median - calculates median 
- .std - calculates standard deviation 
- .drop - drops row/column
- .corr -correlation of columns

# Error Handling 
The script includes error handling for common problems such as missing files, empty files, and parsing errors. It can even raise an exception in the case of any unexpected errors that might happen. 

# Output
The code writes all the calculation information into a text file named iris_data_analysis. The file includes the average, median, standard deviation, correlation, similarity scores, and similarity score explanations. 

# Limitations 
- The code assumes that the CSV files are correctly formatted which could raise an error if they weren't correctly formatted
- The code also assumes that the CSV files are located in the same directory script

# Conclusion 
This project provides a good analysis of the Fisher's Iris data set, including calculations and similarity scores. The error handling in the code ensures that common problems are addressed to ensure that the code is reliable and usable. The project also allowed for the exploration of the panda's library module and hands-on learning experience while using the panda's library for this analysis. 

  
