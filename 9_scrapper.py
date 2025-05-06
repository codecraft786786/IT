import requests

import bs4

request1 = requests.get('https://www.flipkart.com/samsung-galaxy-s24-5g-onyx-black-256-gb/p/itm0456c01739016?pid=MOBGX2F3ZUBMWBGP&lid=LSTMOBGX2F3ZUBMWBGPME7BYW&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=en_DCF19ODqZOwr-jU8gliCnYvGDUHvqbljT8jeC7mk2lE0Ya7j7Z2jQXQjArOvENgBkx7kBhwszopWeFBHvbWTT_UFjCTyOHoHZs-Z5_PS_w0%3D&ppt=None&ppn=None&ssid=d8kllal5mo0000001746550203558')
request1

request1.content

soup = bs4.BeautifulSoup(request1.text)

reviews = soup.findAll('div', {'class' : 'ZmyHeo'});
for review in reviews:
    print(review.get_text() + "\n\n" )

retings = soup.find('div',{'class':'ipqd2A'}).get_text();
print(retings)

individual_ratings = soup.findAll('div', {'class' : 'XQDdHH Ga3i8K'});
for indi_rating in individual_ratings:
    print(indi_rating.get_text() + "\n" )

tags = soup.find('div',{'class':'x+7QT1'}).get_text();
tags

customer_name = soup.findAll('p',{'class':'_2NsDsF AwS1CA'});
for cust_name in customer_name:
    print(cust_name.get_text() + "\n")

price = soup.find('div',{'class':'hl05eU'}).get_text();
print(price)