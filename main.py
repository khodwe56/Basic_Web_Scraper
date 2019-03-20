# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:02:36 2019

@author: Omkar
"""

from bs4 import BeautifulSoup
import requests

search_term = input("Enter the search term\n")
params  = {"q":search_term}

req = requests.get("http://www.bing.com/search",params = params)
bsoup = BeautifulSoup(req.text)
get_results = bsoup.find("ol",{"id":"b_results"})
get_links = get_results.findAll("li",{"class":"b_algo"})

for links in get_links:
    desc_link = links.find("a").text
    actual_link = links.find("a").attrs["href"]
    
    if desc_link and actual_link:
        print(desc_link)
        print(actual_link)
        print("The Summary is : ",links.parent.parent.find("p").text)



