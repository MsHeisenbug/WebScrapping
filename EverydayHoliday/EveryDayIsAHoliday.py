# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:56:42 2019

@author: ms_heisenbug
"""
 
from bs4 import BeautifulSoup
import requests
import json

def get_url_text(url):
    response = requests.get(url, data={'key': 'value'})
    if(response.status_code == requests.codes.ok):
        return response.text
    else:
        return None
    
def arrange_data_from_url(url):
    links_of_months = arrange_data_for_months(url)
    links_of_days = [arrange_data_for_days(link) for link in links_of_months]
    #links_of_holidays = [arrange_data_for_days(link) for link in links_of_days]
    i = 0
    while i != 12:
        for link in links_of_days[i]:
            get_holidays(link)
        i = i + 1
    
    

def arrange_data_for_months(url):
    soup = BeautifulSoup(get_url_text(url), 'lxml')
    months = soup.find_all('h3', class_='card-title')
    return list([month.find('a')['href'] for month in months])
    
def arrange_data_for_days(url):
    soup = BeautifulSoup(get_url_text(url), 'lxml')
    return [a['href'] for a in soup.find_all('a', class_ = 'btn card-cta btn-solid-primary')]

def get_holidays(url):
    soup = BeautifulSoup(get_url_text(url), 'lxml')
    holidays = soup.find_all('div', class_ = 'card-block')
    for l in holidays:
        print(l)
    #data = '\n'.join(str(l for l in holidays))
    #dump_to_json(data)

def dump_to_json(data):  
    with open('holidays.txt', 'w', encoding='utf-8') as f:
        f.write(data)

arrange_data_from_url('https://www.daysoftheyear.com/days/2019')