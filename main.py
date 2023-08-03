from bs4 import BeautifulSoup as bt
import requests
from geopy.distance import geodesic
import pystyle as p
print(p.Box.Lines('Wassim404',))
country = input("entre the country name : ")
city1 = input("entre city 1: ")
city2 = input("entre city 2: ")
page_path = requests.get(f"https://ara.timegenie.com/latitude_longitude/country/{country[0:2]}")
page_content = page_path.content
bs = bt(page_content,'html.parser')

# finder2 = bs.findAll("span")[4].text
# finder3 = bs.findAll("h5")[6].text
# finder4 = bs.findAll("span")[7].text
# first_placr = (finder1,finder2)
# # second_pace = (finder3,finder4)
# dis = int(geodesic(first_placr,second_pace).km)
# print(dis,'km')
finder0 = bs.find_all("h5")
for i in range(len(finder0)):
    if finder0[i].text == city1.strip():
        for j in range(len(finder0)):
            if finder0[j].text == city2.strip():
                # print(f"{finder0[i+2].text} to {finder0[j+2].text}")
                # print(bs.findAll("span")[i+3].text)
                # print(bs.findAll("span")[j+3].text)
                f1 = finder0[i+2].text
                f2 = bs.findAll("span")[i+3].text
                f3 = finder0[j+2].text
                f4 = bs.findAll("span")[j+3].text
                f_place = (f1,f2)
                s_place = (f3,f4)
                distance = float(geodesic(f_place,s_place).km)
                print(distance,'km')





