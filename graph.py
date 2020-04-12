import requests
import datetime
import matplotlib.pyplot as plt
country = input('Enter the name of the country for which you want to check')

url_for_history = "https://covid-193.p.rapidapi.com/history"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e1608910c9msh3d6426308d4b3b9p15de94jsn7fc358704657"
    }
total_cases = 0
total_deaths = 0
cases_dict = {}
death_dict = {}
def test_func(date_selected):
    global total_cases
    global total_deaths


    querystring = {"day":date_selected, "country":country}
    response_for_history = requests.get(url_for_history,headers=headers,params=querystring)
    history_dict = response_for_history.json()
    
    start_of_day_cases = history_dict['response'][-1]['cases']['total']
    end_of_day_cases = history_dict['response'][0]['cases']['total']
    day_cases = int(end_of_day_cases) - int(start_of_day_cases)
    total_cases = total_cases + day_cases 
    cases_dict[date_selected.isoformat()] = day_cases
    

    end_of_day_deaths = history_dict['response'][0]['deaths']['total']
    start_of_day_deaths = history_dict['response'][-1]['deaths']['total']
    death_for_day = int(end_of_day_deaths) - int(start_of_day_deaths)
    total_deaths = total_deaths + death_for_day
    death_dict[date_selected.isoformat()] = death_for_day
    
    print(f'{date_selected}              {death_for_day}                           {day_cases}')


start_date = datetime.date(2020, 4, 1)
end_date = datetime.date.today() - datetime.timedelta(1)


print('Date --------------- Death count --------------- Daily Cases')
while(start_date <= end_date):
    test_func(start_date)
    start_date = start_date + datetime.timedelta(1)

print(f'Total Deaths --------- {total_deaths}')
print(f'Total Cases ---------------------------------------  {total_cases}')


width = 0.3
plt.bar(death_dict.keys(), death_dict.values(), width, color = 'g')
plt.show()

plt.bar(cases_dict.keys(), cases_dict.values(), width, color = 'k')
plt.show()













