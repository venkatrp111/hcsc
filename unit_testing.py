"""Unit testing for output validation"""
import os
import sys
from covid_summary import data_cleaning, merge_dfs, total_counts, counties_df, population_survey_df

#Unit testing the csv files
print('Unit Testing csv files')
if counties_df.empty:
    print('Counties CSV file is empty')
else:
    print('Counties CSV file is not empty')

if population_survey_df.empty:
    print('Population CSV file is empty')
else:
    print('Population CSV file is not empty')


#Unit testing data_cleaning function
print('Unit testing data_cleaning function ...')
(covid_d, pop_d) = data_cleaning(counties_df, population_survey_df)
print(covid_d)
print(pop_d)

#Unit testing merge_dfs function
print('Unit testing merge_dfs function ...')
merged_df = merge_dfs(covid_d, pop_d)
print(merged_df)

   
#output validation
os.chdir(sys.argv[1])
total_counts(merged_df)
path = sys.argv[1]+'/covid_summary.csv'
isFile = os.path.isfile(path)
if isFile:
    print("output successfully generated, output csv is generated in expected path")
else:
    print("output csv is not generated as expected")



print('All test cases passed')    