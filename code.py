''' This is the code for the project '''

''' importing all the modules required '''
import requests
import os 


''' calling the api '''
url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e1608910c9msh3d6426308d4b3b9p15de94jsn7fc358704657"
    }



'''creating the json of the data '''
response = requests.get(url,headers=headers)
country_dict = response.json()



''' asking for the country input '''
country = input('Enter the name of the country for which you want to check')



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

def wrong_func():
    print('this is not supposed to be here')