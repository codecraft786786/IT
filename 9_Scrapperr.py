import requests  
from bs4 import BeautifulSoup  
import json  

url = 'https://www.meesho.com/mamaearth-rice-face-wash-with-rice-water-niacinamide-for-glass-skin-100-ml/p/4vomcl'
response = requests.get(url) 
soup = BeautifulSoup(response.content, 'html.parser')  

scripts = soup.find_all('script', type='application/ld+json')  

for script in scripts:
    try:
        data = json.loads(script.string)  
    
        if "review" in data:
            for review in data["review"]:  
                print(f" Customer Name: {review['author']['name']}")  
                print(f" Rating: {review['reviewRating']['ratingValue']}")  
                print(f" Review: {review['reviewBody']}")  
                print(f" Tag: Not available in static HTML")  
                print("-" * 60)  
    except Exception as e:

        continue