
import requests

import pandas as pd
from bs4 import BeautifulSoup, ResultSet
from pandas import DataFrame
import csv

#pull book in with url, use soup to parse htlm
page = requests.get("https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html")
soup = BeautifulSoup(page.content, 'html.parser')
titles = soup.find ("title")
for title in titles:
    print(title.string)
book_url = soup.find('a')['href']
 #Prints only the jpg we need
images = soup.find_all('img', {'src' : True})
for img in images:
    if img['src'].endswith('15c9.jpg'):



#book_category = soup.find('ul', class_ = "breadcrum").find_all ('a')[2].text.strip()
book_price = soup.find('p', class_ = 'price_color').text.strip()

book_rating = soup.find('p', class_ = 'star-rating Five').text.strip()

book_availability = soup.find('p', class_ = 'availability').text.strip()

product_description = soup.find('article', class_ = "product_page").find_all('p')[3].text.strip()
#print(product_description)

#pulls in titles
book_info_type = soup.find_all('th')
upc_name = soup.find('table', class_ = "table table-striped").find_all ('th') [0].text.strip()
product_type_name = soup.find('table', class_ = "table table-striped").find_all ('th') [1].text.strip()
price_exc_tax_name = soup.find('table', class_ = "table table-striped").find_all ('th') [2].text.strip()
price_inc_tax_name = soup.find('table', class_ = "table table-striped").find_all ('th') [3].text.strip()
tax_name = soup.find('table', class_ = "table table-striped").find_all ('th') [4].text.strip()
Availability_name = soup.find('table', class_ = "table table-striped").find_all ('th') [5].text.strip()
Num_reviews_name = soup.find('table', class_ = "table table-striped").find_all ('th') [6].text.strip()
#headers, obtained from product info chart



#book_data = soup.find_all('td')
#individual product info values
upc_data = soup.find('table', class_ = "table table-striped").find_all ('td') [0].text.strip()
product_type_data = soup.find('table', class_ = "table table-striped").find_all ('td') [1].text.strip()
Price_exc_tax_data = soup.find('table', class_ = "table table-striped").find_all ('td') [2].text.strip()
price_inc_tax_data = soup.find('table', class_ = "table table-striped").find_all ('td') [3].text.strip()
tax_data = soup.find('table', class_ = "table table-striped").find_all ('td') [4].text.strip()
availability_data = soup.find('table', class_ = "table table-striped").find_all ('td') [5].text.strip()
num_reviews_data = soup.find('table', class_ = "table table-striped").find_all ('td') [6].text.strip()
#print(upc_data, product_type_data, price_inc_tax_data,Price_exc_tax_data,tax_data, availability_data, num_reviews_data)

headers = [page, "Title", "Description", book_rating, book_availability, upc_name, product_type_name,
           price_exc_tax_name, price_inc_tax_name, tax_name,
           Availability_name, Num_reviews_name]
#print(headers)
row_data = [page, title.string, product_description, book_rating, book_availability, upc_data, product_type_data, Price_exc_tax_data, price_inc_tax_data, tax_data,
            availability_data, num_reviews_data][0:12]
dict = ({"Title" : title, "Description" : product_description, book_rating : book_rating,
        book_availability : [availability_data], upc_name : [upc_data], product_type_name : [product_type_data],
        price_exc_tax_name : [Price_exc_tax_data], price_inc_tax_name : [price_inc_tax_data], tax_name : [tax_data],
        Availability_name : [availability_data], Num_reviews_name : [num_reviews_data]})
df = pd.DataFrame(dict)
df
df.to_csv('data_attempt.csv')





