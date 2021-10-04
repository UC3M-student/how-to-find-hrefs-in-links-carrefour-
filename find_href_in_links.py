from helium import *
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.carrefour.es/"

def get_data(url_sample):
    Browser = start_chrome(url_sample, headless=True)
    browser_ = Browser.page_source
    soup  = BeautifulSoup(browser_,"html.parser")
    return soup

def link_library(soup):
    href_list = []
    hrefs = soup.find_all("a", {"class":"text-banner__link track-click"})
    w = "https://www.carrefour.es"
    for i in hrefs:
        i = i.get("href")
        href_list.append(i)
    href_list_remove = []
    for y in href_list:
        href_list_remove.append(y.replace(w,""))
    perfect_href_list = []
    for adds in href_list_remove:
        perfect_href_list.append(w + adds)
    return perfect_href_list

def link_library_inside(soup):
    href_list = []
    hrefs = soup.find_all("div", {"class":"item-distributor"})
    w = "https://www.carrefour.es"
    for i in hrefs:
        i = i.find("a").get("href")
        href_list.append(i)
    href_list_remove = []
    for y in href_list:
        href_list_remove.append(y.replace(w,""))
    perfect_href_list_inside = []
    for adds in href_list_remove:
        perfect_href_list_inside.append(w + adds)
    return perfect_href_list_inside



def link_actions(link_ibrary):
    link_list = []
    for i in link_ibrary:
        a = get_data(i)
        b1 = link_library_inside(a)
        if b1 == []:
            link_list.append(i)
            print("eureka2")
        else:
            for b in b1:
                link_list.append(b)
                print("very looking good")

    return link_list






a = get_data(url)
b = (link_library(a))
c = link_actions(b)
print(c)
