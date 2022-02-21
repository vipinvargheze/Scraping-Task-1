from bs4 import BeautifulSoup
import requests

from csv import writer


html_text = requests.get('https://www.gotoauto.ca/inventory/').text

soup = BeautifulSoup(html_text, 'lxml')

carz = soup.find_all('li' , class_ = 'vehicle-item')

with open('car_details.csv','w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Car_Name', 'MSRP' , 'Description']
    thewriter.writerow(header)
    for cars in carz:

        car_details = cars.find('h4' , class_ = 'name desc_l5').text

        car = car_details.replace('\t','').replace('\n','')

        price = cars.find('span', class_ = 'price').text


        link= 'https://www.gotoauto.ca '+ cars.find('a')['href']


        info = [car,price,link]
        print(info)
        thewriter.writerow(info)