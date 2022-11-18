# Data-Manipulation-with-pandas

## Course Description
In this course, I'll practice how to manipulate DataFrames, as I extract, filter, and transform real-world datasets for analysis. Using pandas I’ll explore all the core data science concepts. Using real-world data, including Walmart sales figures and global temperature time series, I’ll learn how to import, clean, calculate statistics, and create visualizations.

### Chapter 1: Transforming DataFrames
- head() returns the first few rows (the “head” of the DataFrame).
- info() shows information on each of the columns, such as the data type and number of missing values.
- shape returns the number of rows and columns of the DataFrame.
- describe() calculates a few summary statistics for each column.
#### Pandas DataFrames consist of three components, stored as attributes:
- values: A two-dimensional NumPy array of values.
- columns: An index of columns: the column names.
- index: An index for the rows: either row numbers or row names.

You can sort the rows by passing a column name to **.sort_values()**.


## Chapter 2: Aggregating DataFrames
In this chapter, I'll practice how to calculate summary statistics on DataFrame columns, and master grouped summary statistics and pivot tables.
