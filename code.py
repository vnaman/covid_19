''' This is the code for the project '''

''' importing all the modules required '''
import requests
import datetime

''' asking for the country input '''
country = input('Enter the name of the country for which you want to check')

url_for_history = "https://covid-193.p.rapidapi.com/history"
url_for_statistics = "https://covid-193.p.rapidapi.com/statistics"


headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e1608910c9msh3d6426308d4b3b9p15de94jsn7fc358704657"
    }


def test_func(date_selected):
    querystring = {"day":date_selected, "country":country}
    response_for_history = requests.get(url_for_history,headers=headers,params=querystring)
    history_dict = response_for_history.json()

    end_of_day_deaths = history_dict['response'][0]['deaths']['total']
    start_of_day_deaths = history_dict['response'][-1]['deaths']['total']
    death_for_day = int(end_of_day_deaths) - int(start_of_day_deaths)
    print(f'{date_selected}              {death_for_day}')


start_date = datetime.date(2020, 4, 1)
end_date = datetime.date.today() - datetime.timedelta(1)


print('Date --------------- Death count')
while(start_date <= end_date):
    test_func(start_date)
    start_date = start_date + datetime.timedelta(1)





















# response_for_statistics = requests.get(url_for_statistics,headers=headers)
#     country_dict = response_for_statistics.json()

#     for each in country_dict['response']:
#         if each['country'] == country:
#             new_cases = each['cases']['new']
#             total_cases = each['cases']['total']
#             print(f'Number of new cases : {new_cases}')
#             print(f'Total number of cases : {total_cases}')




