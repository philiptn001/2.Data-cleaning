# Data_Cleaning
Project to learn data cleaning to get rid of unnecessary information and abnormalities.

Process:
* Dropping Unwanted Columns
* Cleaning Columns
* Filtering Rows
* Merging Two Dataframes

Steps:
* Load the dataset into a dataframe
* Calculate and print the number of nan (not a number) in each column
* Drop the columns of dataframe by the below-mentioned black list:
'Edition Statement',
'Corporate Author',
'Corporate Contributors',
'Former owner',
'Engraver',
'Contributors',
'Issuance type',
'Shelfmarks'
* Replace the cell value of "Place of Publication" with "London" if it contains "London", and replace all '-' characters with space
* Keep the first 4 digit number in "Date of Publication"
* Convert "Date of Publication" cells to numbers
* Replace NaN with 0 for the cells of "Date of Publication"
* Replace the spaces in the column names with the underline character ('_')
* Filter the rows and only keep books which are published in "London" after 1866.
* Load the City dataset into a dataframe
* Group by the resultant dataframe based on the country column While grouping by, to keep the name of countries set as_index=False Use count() to calculate the number of publications by country.
* Print the dataframe
