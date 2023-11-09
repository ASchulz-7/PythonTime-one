
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
#images = soup.find_all('img', {'src' : True})
#for img in images:
 #   if img['src'].endswith('15c9.jpg'):
  #  print(img['src'])




#book_category = soup.find('ul', class_ = "breadcrum").find_all ('a')[2].text.strip()
book_price = soup.find('p', class_ = 'price_color').text.strip()

book_rating = soup.find('p', class_ = 'star-rating Five').text.strip()

book_availability = soup.find('p', class_ = 'availability').text.strip()

product_description = soup.find('article', class_ = "product_page").find_all('p')[3].text.strip()
#print(product_description)

#pulls in titles
book_info_type = soup.find_all('th')
#headers, obtained from product info chart
def get_chart_data(soup):
    Book_chart_tags = soup.find('table', class_ = "table table-striped").find_all ('td')[0:7]
    chart_data = []
    for tags in Book_chart_tags:
        chart_data.append(tags)
    return chart_data
print(get_chart_data(soup))


#book_data = soup.find_all('td')
#individual product info values
def get_upc_data(soup):
    Book_UPC_tags = soup.find('table', class_ = "table table-striped").find_all ('td')[0]
    upc_data = []
    for tags in Book_UPC_tags:
        upc_data.append(tags)
    return upc_data
print(get_upc_data(soup))
#issue with it seperating each value...
upc_data = soup.find('table', class_ = "table table-striped").find_all ('td') [0].text.strip()

product_type_data = soup.find('table', class_ = "table table-striped").find_all ('td') [1].text.strip()
def product_type_data(soup):
    Prod_type_tag = soup.find('table', class_ = "table table-striped").find_all ('td') [1]
    prod_type_data = []
    for tags in Prod_type_tag:
        prod_type_data.append(tags)
    return prod_type_data
print(product_type_data(soup))

Price_exc_tax_data = soup.find('table', class_ = "table table-striped").find_all ('td') [2].text.strip()
#def Price_exc_tax_data(soup):
 #   Price_exc_tag = soup.find('table', class_ = "table table-striped").find_all ('td') [2]
#    Price_exc_data = []
  #  for tags in Price_exc_data:
#        Price_exc_data.append(tags)
 #   return Price_exc_data
#print(Price_exc_data (soup))

price_inc_tax_data = soup.find('table', class_ = "table table-striped").find_all ('td') [3].text.strip()
tax_data = soup.find('table', class_ = "table table-striped").find_all ('td') [4].text.strip()
availability_data = soup.find('table', class_ = "table table-striped").find_all ('td') [5].text.strip()
num_reviews_data = soup.find('table', class_ = "table table-striped").find_all ('td') [6].text.strip()
#print(upc_data, product_type_data, price_inc_tax_data,Price_exc_tax_data,tax_data, availability_data, num_reviews_data)

headers = [page, "Title", "Description", "Rating", "Availability", "UPC", "Product Type",
           "Tax Excluded Price", "Tax Included Price", "Tax",
          " Availability", "Reviews"]

#print(headers)
row_data = [page, title.string, product_description, book_rating, book_availability, upc_data, product_type_data, Price_exc_tax_data, price_inc_tax_data, tax_data,
            availability_data, num_reviews_data][0:12]
dict = ({"Title" : title, "Description" : product_description, "Rating" : book_rating,
        "Availability" : [availability_data], "UPC": [upc_data], "Type" : [product_type_data],
        "Price without Tax" : [Price_exc_tax_data], "Price with Tax" : [price_inc_tax_data], "Tax" : [tax_data],
        "Availability" : [availability_data], "Number of Reviews" : [num_reviews_data]})

SciFiURL = ("https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html")
response = requests.get(SciFiURL)
if response.status_code == 200:
    print("Yay!!")
else:
    print("error code not 200")
page_contents = response.text

soup = BeautifulSoup(response.text, 'html.parser')
# uploaded soup and pulled in science-fiction category page data

def get_titles(soup):
    Book_title_tags = soup.find_all('h3')
    Book_titles = []
    for tags in Book_title_tags:
        Book_titles.append(tags.text)
    return Book_titles
get_titles(soup)
#print(get_titles(soup))

def obtain_book_price(soup):
    book_price_tags = soup.find_all('p', class_ = "price_color")
    Book_price = []
    for tags in book_price_tags:
        Book_price.append(tags.text.replace('Â', ''))
    return Book_price
#print(obtain_book_price(soup))


def extract_book_links(soup):
    h3_tags = soup.find_all('h3')
    book_links = []
    base_url = 'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html'
    for tag in h3_tags:
        book_links.append(f'https://books.toscrape.com/catalogue/{tag.contents[0]['href'].replace("../../../","")}')
#extracts all html code for scifi page
    return book_links
print(extract_book_links(soup))

print(f'Book Data {dict}')


#df = pd.DataFrame(dict)
#df
#df.to_csv('data_attempt1.csv')



