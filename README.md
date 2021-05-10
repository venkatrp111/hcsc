New York Times COVID-19 Data
Source https://github.com/nytimes/covid-19-data/blob/master/README.md
Download Link https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

Sample Data

        date	county	state	fips	cases	deaths
0	2020-01-21	Snohomish	Washington	53061.0	1	0.0
1	2020-01-22	Snohomish	Washington	53061.0	1	0.0
2	2020-01-23	Snohomish	Washington	53061.0	1	0.0

The Federal Information Processing Standard Publication 6-4 (FIPS 6-4) is a five-digit Federal Information Processing Standards code which uniquely identified counties and county equivalents in the United States, certain U.S. possessions, and certain freely associated states.

2019 Population Estimate Data
Source https://www.census.gov/data/datasets/timeseries/demo/popest/2010s-counties-total.html
Download Link https://www2.census.gov/programssurveys/popest/datasets/2010-2019/counties/totals/coest2019alldata.csv

Sample data(required columns) 

	STATE	COUNTY	POPESTIMATE2019
0	1	0	4903185
1	1	1	55869
2	1	3	223234

Goal: The goal of the project is to create a repeatable pipeline that merges these two datasets into a single Dataframe and output file.

Required dependencies :
Sys
Pandas
Os

Instructions to run the script
1)Make sure all dependencies are satisfied

2)Make sure to run script by providing arguments as follows
python covid_summary.py outputpath
Example: python covid_summary.py /Users/venkat/Downloads/output

outputpath is the output path where the generated summary dataset is saved,
Make sure to give correct output path


Process used to generate the summary dataset.
1)Initially all the csv files are read, I have used pandas in this script to merge the given 2 files.
2)Capitalized the first letter of column names
3)Creating Fips code from state and county: FIPS code is not directly available in population estimate data, so, I have generated it from state and county
4)retained only required columns
5)Dealing with NA records 
6) finally these preprocessed files are merged to single data frame and downloaded in csv format to provided output path

Unit testing
unit_testing.py:
In this python script unit testing of input csv files and all functions are done
Unit testing is done for output validation 

Coding standards
Used pylint to check pep8 style coding standards

Improvements/Add on
Creating a website using flask, html, css and heroku to display the generated summary data set and show some visualizations like highly affected counties	




	