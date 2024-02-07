# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:16:57 2023

@author: PrabhatRanjan
"""

from entsoe import EntsoePandasClient
import pandas as pd
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H%M%S")
df = pd.read_excel('mapping.xlsx')
map_dict = dict(df.values)
map_key_list = [keys for keys in map_dict]

client = EntsoePandasClient(api_key="f31fc9e5-c47e-49c1-b39a-ffc9f7b556b7")


start = input("Input the start date in the format (YYYYMMDD) >> \t")
end = input("Input the end date in the format (YYYYMMDD) >> \t")

for i in range(0, len(map_key_list)):
    print("{}. {}\t: {}".format(i, map_key_list[i], map_dict[map_key_list[i]]))

area = int(input("Select an area (just input the number only) >> \t"))
print('The selected area is {}\t: {}\n'.format(map_key_list[area], map_dict[map_key_list[area]]))

print("\n The time zone is automatically selected as CET or Europe/Brussels... \n")

start = pd.Timestamp(str(start), tz='Europe/Brussels')
end = pd.Timestamp(str(end), tz='Europe/Brussels')
country_code = map_key_list[area]
#country_code_from = 'FR'  # France
#country_code_to = 'DE_LU' # Germany-Luxembourg
type_marketagreement_type = 'A01'
contract_marketagreement_type = "A01"

requests = ['query_day_ahead_prices', 'query_net_position',
            'query_crossborder_flows', 'query_scheduled_exchanges',
            'query_net_transfer_capacity_dayahead', 'query_net_transfer_capacity_weekahead',
            'query_net_transfer_capacity_monthahead', 'query_net_transfer_capacity_yearahead',
            'query_intraday_offered_capacity', 'query_offered_capacity',
            'query_aggregate_water_reservoirs_and_hydro_storage', 'query_load',
            'query_load_forecast', 'query_load_and_forecast', 'query_generation_forecast',
            'query_wind_and_solar_forecast', 'query_intraday_wind_and_solar_forecast',
            'query_generation', 'query_generation_per_plant', 'query_installed_generation_capacity',
            'query_installed_generation_capacity_per_unit', 'query_imbalance_prices',
            'query_contracted_reserve_prices', 'query_contracted_reserve_amount',
            'query_unavailability_of_generation_units',
            'query_unavailability_of_production_units', 'query_unavailability_transmission',
            'query_withdrawn_unavailability_of_generation_units',
            'query_physical_crossborder_allborders', 'query_generation_import',
            'query_procured_balancing_capacity']

for i in range(0, len(requests)):
    print("{}. {}".format(i, requests[i]))
request = int(input("Select an request (just input the number only) >> \t"))
print('The selected request is {}\t: {}\n'.format(request,requests[request]))

# methods that return Pandas Series
count = 0
match request:
    case(0):
        df = client.query_day_ahead_prices(country_code, start=start,end=end)
    case(1):
        df = client.query_net_position(country_code, start=start, end=end, dayahead=True)
    case(2):
        df = client.query_crossborder_flows(country_code_from, country_code_to, start, end)
    case(3):
        df = client.query_scheduled_exchanges(country_code_from, country_code_to, start, end, dayahead=False)
    case(4):
        df = client.query_net_transfer_capacity_dayahead(country_code_from, country_code_to, start, end)
    case(5):
        df = client.query_net_transfer_capacity_weekahead(country_code_from, country_code_to, start, end)
    case(6):
        df = client.query_net_transfer_capacity_monthahead(country_code_from, country_code_to, start, end)
    case(7):
        df = client.query_net_transfer_capacity_yearahead(country_code_from, country_code_to, start, end)
    case(8):
        df = client.query_intraday_offered_capacity(country_code_from, country_code_to, start, end,implicit=True)
    case(9):
        df = client.query_offered_capacity(country_code_from, country_code_to, start, end, contract_marketagreement_type, implicit=True)
    case(10):
        df = client.query_aggregate_water_reservoirs_and_hydro_storage(country_code, start, end)
    case(11):
        df = client.query_load(country_code, start=start,end=end)
    case(12):
        df = client.query_load_forecast(country_code, start=start,end=end)
    case(13):
        df = client.query_load_and_forecast(country_code, start=start, end=end)
    case(14):
        df = client.query_generation_forecast(country_code, start=start,end=end)
    case(15):
        df = client.query_wind_and_solar_forecast(country_code, start=start,end=end, psr_type=None)
    case(16):
        df = client.query_intraday_wind_and_solar_forecast(country_code, start, end, psr_type=None)
    case(17):
        df = client.query_generation(country_code, start=start,end=end, psr_type=None)
    case(18):
        df = client.query_generation_per_plant(country_code, start=start,end=end, psr_type=None)
    case(19):
        df = client.query_installed_generation_capacity(country_code, start=start,end=end, psr_type=None)
    case(20):
        df = client.query_installed_generation_capacity_per_unit(country_code, start=start,end=end, psr_type=None)
    case(21):
        df = client.query_imbalance_prices(country_code, start=start,end=end, psr_type=None)
    case(22):
        df = client.query_contracted_reserve_prices(country_code, start=start, end=end, type_marketagreement_type=type_marketagreement_type, psr_type=None)
    case(23):
        df = client.query_contracted_reserve_amount(country_code, start=start, end=end, type_marketagreement_type=type_marketagreement_type, psr_type=None)
    case(24):
        df = client.query_unavailability_of_generation_units(country_code, start=start,end=end, docstatus=None, periodstartupdate=None, periodendupdate=None)
    case(25):
        df = client.query_unavailability_of_production_units(country_code, start, end, docstatus=None, periodstartupdate=None, periodendupdate=None)
    case(26):
        df = client.query_unavailability_transmission(country_code_from, country_code_to, start, end, docstatus=None, periodstartupdate=None, periodendupdate=None)
    case(27):
        df = client.query_withdrawn_unavailability_of_generation_units(country_code, start, end)
    case(28):
        df = client.query_physical_crossborder_allborders(country_code, start, end, export)
    case(29):
        df = client.query_generation_import(country_code, start, end)
    case(30):
        df = client.query_procured_balancing_capacity(country_code, start, end, process_type, type_marketagreement_type=None)
    case _:
        print('Bad Case, Retry!!')
        exit()

name = country_code+"_"+current_time+"_"+requests[request]+".csv"
df.to_csv("results/"+name)
