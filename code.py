''' This is the code for the project '''

''' importing all the modules required '''
import requests
import os 


''' calling the api '''
url_for_statistics = "https://covid-193.p.rapidapi.com/statistics"
url_for_history = "https://covid-193.p.rapidapi.com/history"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e1608910c9msh3d6426308d4b3b9p15de94jsn7fc358704657"
    }
querystring = {"day":"2020-04-06","country":"usa"}


'''creating the json of the data '''
response_for_statistics = requests.get(url_for_statistics,headers=headers)
country_dict = response_for_statistics.json()

response_for_history = requests.get(url_for_history,headers=headers,params=querystring)
history_dict = response_for_history.json()
print(history_dict['response'])


''' asking for the country input '''
# country = input('Enter the name of the country for which you want to check')



'''printing the country's statistics '''
# for each in country_dict['response']:
#     if each['country'] == country:
#         name = each['country']
#         new_cases = each['cases']['new']
#         total_cases = each['cases']['total']
#         total_deaths = each['deaths']['total']
#         print(f'Name of the country : {name}')
#         print(f'Number of new cases : {new_cases}')
#         print(f'Total number of cases : {total_cases}')
#         print(f'Total number of deaths : {total_deaths}')