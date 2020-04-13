''' This file prints some statistics for the selected country '''

''' importing all the modules required '''
import requests
import os 

''' asking for the country input '''
country = input('Enter the name of the country for which you want to check')

''' calling the api '''
url_for_statistics = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': ""
    }


'''creating the json of the data '''
response_for_statistics = requests.get(url_for_statistics,headers=headers)
country_dict = response_for_statistics.json()


'''printing the country's statistics '''
for each in country_dict['response']:
    if each['country'] == country:
        name = each['country']
        new_cases = each['cases']['new']
        total_cases = each['cases']['total']
        total_deaths = each['deaths']['total']
        print(f'Name of the country : {name}')
        print(f'Number of new cases for today: {new_cases}')
        print(f'Total number of cases : {total_cases}')
        print(f'Total number of deaths : {total_deaths}')

