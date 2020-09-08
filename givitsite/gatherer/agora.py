#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import urllib
from bs4 import BeautifulSoup
import re
import csv
from datetime import datetime
from friendreq.models import ItemRequest
from friendreq.models import ITEM_CHOICES
from friendreq.models import ItemsFound


def givit_main():
    iseek_dict_eng = dict(ITEM_CHOICES)
    iseek_dict = {'20016': 'מיטה', '20008': 'כיסא', '20009': 'ארון',
                  '20017': 'ספה', '10029': 'מכונת כביסה', '10006': 'מקרר'}
    region_dict = {'Tel Aviv': 'תל אביב-יפו', 'Jerusalem': 'ירושלים',
                   'Beer Sheva': 'באר שבע', 'Haifa': 'חיפה', 'Modiin': 'מודיעין', 'Hasharon': 'הוד השרון'}
    items_list = get_items_list()
    i = 0
    counter = 0
    for i in range(len(items_list)):
        iseek = items_list[i][2]
        my_soup = Agora_Getrequest(iseek)
        url_list = find_furniture(
            my_soup, region_dict.get(items_list[i][3]), iseek_dict.get(items_list[i][2]))
        for item in range(len(url_list)):
            items_list[i].append(url_list[item])
        if len(items_list[i]) > 6:
            print(items_list[i][6])
            counter += 1
            print(str(counter) + " new item added")
            request_id = int(items_list[i][0])
            url = items_list[i][6]
            picture = items_list[i][6]
            city = items_list[i][3]
            title = iseek_dict_eng.get(items_list[i][2])
            newFound = ItemsFound(
                request_id=request_id, url=url, picture=picture, city=city, title=title)
            newFound.save()
        url_list = []


def get_items_list():
    """
    this function open our wishlist and return item_list such that every item in this list is a list with all the
    information about.
    Returns:
    item_list (list of lists): list of all items in our wishlist.
    """
    wish_list = ItemRequest.objects.all()
    items_list = [list(item.values()) for item in wish_list.values()]
    return items_list


def Agora_Getrequest(iseek):
    """
    this function gets iseek which allow us to nevigate to the specific url and return beatifulsoup object.
    Parameters:
    iseek (string): iseek is the category number of the product that we need for the url.
    Returns:
    BeautifulSoup object: which represents the document as a nested data structure.
    """
    url = 'https://www.agora.co.il/toGet.asp?'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0'
    values = {'searchType': 'subCategory', 'dealType': '1', 'iseek': iseek}
    data = urllib.parse.urlencode(values)
    new_url = url + data
    data = data.encode('utf-8')
    req = urllib.request.Request(new_url, data, headers)
    webpage = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser', from_encoding="utf-8")
    return soup


def find_furniture(soup, area, name):
    """
    this function gets soup, area and name of the product we are looking for
    and return all the rows that found on the website as url_list.
    Parameters:
    soup (beautifulsoup object): which represents the document as a nested data structure.
    area (string): the area that we want to pick the product from.
    name (string): the name of the product we search for.
    Returns:
    url_list (list): list of all url that match to what we search.
    """
    url_list = []
    t = soup.findAll('tbody', class_='objectGroup')
    for i in range(len(t)):
        c1 = t[i].find_all('td', class_='area')
        c2 = t[i].find_all('td', class_='newWindow')
        c5 = t[i].find_all('td', class_='objectName')
        c6 = t[i].find_all('td', class_='objectState')
        item_name = str(c5[0].text)
        check_item_state = (str((c6[0].select('span'))))
        item_state = str(re.match('.*(condition[2,1]).*', check_item_state))
        if area in (c1[0].text) and str(re.match(name, item_name)) != 'None' and item_state != 'None':
            c3 = c2[0].find_all('a')
            string1 = str(c3[0])
            string2 = str(re.findall('href="(\S*)"', string1))
            string4 = 'https://www.agora.co.il/' + string2[2:-2]
            url_list.append(string4)
    return url_list


def find_new_furniture(soup, area, name):
    """
    this function is the same as find_furniture, the only diffrent is that here we search only item that add this day.
    Parameters:
    soup (beautifulsoup object): which represents the document as a nested data structure.
    area (string): the area that we want to pick the product from.
    name (string): the name of the product we search for.
    Returns:
    url_list (list): list of all url that match to what we search.
    """
    url_list = []
    t = soup.findAll('tbody', class_='objectGroup')
    for i in range(len(t)):
        c1 = t[i].find_all('td', class_='area')
        c2 = t[i].find_all('td', class_='newWindow')
        c4 = t[i].find_all('td', class_='regDate')
        c5 = t[i].find_all('td', class_='objectName')
        c6 = t[i].find_all('td', class_='objectState')
        upload_time = str(c4[0].text)
        item_name = str(c5[0].text)
        check_item_state = (str((c6[0].select('span'))))
        hour = datetime.now().hour
        my_regex = str(hour+1)+':[0-9][0-9]'
        item_state = str(re.match('.*(condition[2,1]).*', check_item_state))
        if area in (c1[0].text) and str(re.match(my_regex, upload_time)) != 'None' and str(re.match(name, item_name)) != 'None' and item_state != 'None':
            c3 = c2[0].find_all('a')
            string1 = str(c3[0])
            string2 = str(re.findall('href="(\S*)"', string1))
            string4 = 'https://www.agora.co.il/' + string2[2:-2]
            url_list.append(string4)
    return url_list
