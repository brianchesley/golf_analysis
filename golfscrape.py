import requests
# a great library for accessing the web
from bs4 import BeautifulSoup
# our HTML parsing library
import csv
# the library to read and write csv files

def get_links():
    #this will compile a list of links we want. 
    urls = []
    base_url = "http://www.pgatour.com/stats/stat.109."
    for i in range(1980,2013):
        urls.append((base_url + str(i) + ".html", i))
    return urls

print get_links()

def scrape_money_leaders_year(url):
    #Downloads the money winners by year for the PGA tour
    #using Requests
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    money = []
    for item in soup.findAll("td", "hidden-small")[4::3]:
        money.append(item.text)
    return money



def get_cpi():
    url = "http://www.minneapolisfed.org/community_education/teacher/calc/hist1913.cfm"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    info = []
    for e in soup.findAll('td')[203:]:
        info.append(e.text)
    del info[2::3]
    pairs = dict(zip(info[::2], info[1::2])) 
    return pairs


 

def write_csv(money_winners_list, year):
    Money_list = open("money_list_by_year.csv", 'ab')
    money_winners_list.insert(0, year)
    writer = csv.writer(Money_list, delimiter=',')
    writer.writerow(money_winners_list)
    Money_list.close()
    
def main():
    cpi_dict = get_cpi()
    urls = get_links()
    for url_list in urls:
        money_list = scrape_money_leaders_year(url_list[0])
        corrected_ml = [int(i.replace(',','')) * (229.6 / float(cpi_dict[str(url_list[1])])) for i in money_list]
        write_csv(corrected_ml, url_list[1])
    transpose_data()

def transpose_data():
    a = zip(*csv.reader(open("money_list_by_year.csv", "rb")))
    csv.writer(open("money_list_by_year.csv", "wb")).writerows(a)


#main()

