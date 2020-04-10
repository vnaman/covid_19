''' This is the code for the project '''

''' importing all the modules required '''
import requests
import os 

''' asking for the country input '''
country = input('Enter the name of the country for which you want to check')

''' calling the api '''
url_for_statistics = "https://covid-193.p.rapidapi.com/statistics"
url_for_history = "https://covid-193.p.rapidapi.com/history"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e1608910c9msh3d6426308d4b3b9p15de94jsn7fc358704657"
    }
querystring = {"day":"2020-04-06","country":country}

'''creating the json of the data '''
response_for_statistics = requests.get(url_for_statistics,headers=headers)
country_dict = response_for_statistics.json()
response_for_history = requests.get(url_for_history,headers=headers,params=querystring)
history_dict = response_for_history.json()



'''printing the country's statistics '''
for each in country_dict['response']:
    if each['country'] == country:
        name = each['country']
        new_cases = each['cases']['new']
        total_cases = each['cases']['total']
        total_deaths = each['deaths']['total']
        print(f'Name of the country : {name}')
        print(f'Number of new cases : {new_cases}')
        print(f'Total number of cases : {total_cases}')
        print(f'Total number of deaths : {total_deaths}')

''' calculating day wise deaths'''
end_of_day_deaths = history_dict['response'][0]['deaths']['total']
start_of_day_deaths = history_dict['response'][-1]['deaths']['total']
death_for_day = int(end_of_day_deaths) - int(start_of_day_deaths)
print(f'death count for today is {death_for_day}')