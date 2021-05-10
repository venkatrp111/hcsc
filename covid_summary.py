"""Code to generate summary dataset"""
import os
import sys
import logging
import pandas as pd

logging.basicConfig(filename='logging.txt', filemode='w', format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S ')
counties_df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
population_survey_df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv', encoding='latin-1', usecols=['POPESTIMATE2019', 'STATE', 'COUNTY'])

def data_cleaning(covid19_df, population_df):
    """Function for data cleaning"""
    print('Cleaning the data . . .')
    # Renaming Column names
    covid19_df_rename = {'date': 'Date', 'county': 'County', 'state': 'State',
                         'fips': 'FIPS', 'cases': 'Cases', 'deaths': 'Deaths'}
    covid19_df.columns = [covid19_df_rename.get(x) for x in covid19_df.columns]
    #formating the state and county
    population_df['STATE'] = population_df['STATE'].map('{:0>2}'.format)
    population_df['COUNTY'] = population_df['COUNTY'].map('{:0>3}'.format)
    #creating fips by joining state and county
    population_df['FIPS'] = population_df['STATE'] + population_df['COUNTY']
    #dropping state and county column
    population_df = population_df.drop(['STATE', 'COUNTY'], axis=1)
    #dealing na values in fips column
    covid19_df['FIPS'] = covid19_df['FIPS'].fillna(0).astype(int)
    #formating fips column
    covid19_df['FIPS'] = covid19_df['FIPS'].map('{:0>5}'.format)

    #converting all the date formats to single format
    covid19_df['Date'] = pd.to_datetime(covid19_df['Date'], format='%Y-%m-%d')

    # sorting the df by date
    covid19_df = covid19_df.sort_values(by='Date', ascending=True, ignore_index=True)

    return (covid19_df, population_df)

def merge_dfs(covid_df, popltn_df):
    """Function for merging dataframes"""
    print('Merging data frames ... ')
    merged_df = pd.merge(covid_df, popltn_df, on=['FIPS'], how='left')
    #dealing na values
    merged_df['POPESTIMATE2019'] = merged_df['POPESTIMATE2019'].fillna(0).astype(int)
    merged_df.columns = ['Date', 'County', 'State', 'FIPS', 'Daily Cases',
                         'Daily Deaths', 'POPESTIMATE2019']
    #sorting the df
    merged_df = merged_df.sort_values(by=['Date', 'State', 'County'], ascending=[True, True, True])
    return merged_df

def total_counts(merged_df):
    """Function for generating summary dataset"""
    #calculating cumulative cases and deaths
    print('Generating counts ...')
    merged_df['Cumulative Cases'] = merged_df.groupby(by=['FIPS'])['Daily Cases'].transform(lambda x: x.cumsum())
    merged_df['Cumulative Deaths'] = merged_df.groupby(by=['FIPS'])['Daily Deaths'].transform(lambda x: x.cumsum())
    merged_df = merged_df[['FIPS', 'Date', 'County', 'State', 'POPESTIMATE2019',
                           'Daily Cases', 'Daily Deaths', 'Cumulative Cases', 'Cumulative Deaths']]
    merged_df.to_csv('covid_summary.csv', index=False)
    print('Summary Data set generated')

def main():
    """Generating summary dataset"""
    try:
        (covid_d, pop_d) = data_cleaning(counties_df, population_survey_df)
        merged_df = merge_dfs(covid_d, pop_d)
        #changing the directory according to output path
        os.chdir(sys.argv[1])
        total_counts(merged_df)
    except IndexError:
        print("Summary data set not generated, Please provide correct output")
        logging.warning('Summary data set not generated, Please provide correct output')
    except FileNotFoundError:
        print('Summary data set not generated, No such file or directory')
        logging.warning('Summary data set not generated, No such file or directory')

if __name__ == "__main__":
    main()
    