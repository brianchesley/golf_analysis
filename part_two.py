
def get_cpi():
    url = "http://www.minneapolisfed.org/community_education/teacher/calc/hist1913.cfm"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    
def adjust_for_price():