# Requests
import requests
import csv

# BeautifulSoup
from bs4 import BeautifulSoup


page = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page.content, 'html.parser')


# pulling category links
def category_link():
    main_url = 'http://books.toscrape.com/index.html'
    request = requests.get(main_url)
    if request.ok:
        souper = BeautifulSoup(request.text, 'html.parser')
        ul = souper.find('ul', class_=["nav", "nav-list"])

        li = ul.find_all('li')
        category_requests = []
        for item in li:
            link = item.find('a', href=True)
            if link is not None:
                print(link['href'])
        return category_requests
# print(category_link())

# pulling book titles
def book_titles(soup):
    book_title_tags = soup.find_all('h3')
    book_titles_list = []
    for tags in book_title_tags:
        book_titles_list.append(tags.text)
    return book_titles_list
# print(book_titles(soup))

# pulling book url using book title tags
def book_url(book_title_tags):

    book_url = []
    for article in book_title_tags:
        for link in article.find_all('a', href=True):
            url = link['href']
            links = 'https://books.toscrape.com/' + url
            if links not in book_url:
                book_url.append(links)

    return book_url

# obtaining product information using url obtained above
def product_information(url):
    information = []
    page = requests.get(url)
    soup = soup = BeautifulSoup(page.content, 'html.parser')
    # book_data = url.find_all('td')
    # book_price = url.find('p', class_ = 'price_color').text.strip()
    book_rating = '.star-rating'
    title = ('h1')
    book_availability = soup.find('p', class_='availability').text.strip()

    product_description = soup.find('article', class_="product_page").find_all('p').text.strip()
# individual product info values
    upc_data = soup.find('table', class_="table table-striped").find_all('td')[0].text.strip()
    product_type_data = soup.find('table', class_="table table-striped").find_all('td')[1].text.strip()
    price_exc_tax_data = soup.find('table', class_="table table-striped").find_all('td')[2].text.strip()
    price_inc_tax_data = soup.find('table', class_="table table-striped").find_all('td')[3].text.strip()
    tax_data = soup.find('table', class_="table table-striped").find_all('td')[4].text.strip()
    availability_data = soup.find('table', class_="table table-striped").find_all('td')[5].text.strip()
    num_reviews_data = soup.find('table', class_="table table-striped").find_all('td')[6].text.strip()
# print(upc_data product_type_data, price_inc_tax_data,Price_exc_tax_data,tax_data, availability_data, num_reviews_data)

    headers = ["page", "Title", "Description", "book_rating", "book_availability", "upc", "product_type",
                "price_exc_tax_name", "price_inc_tax_name", "tax",
                "Availability_name", "Num_reviews_name"]
# print(headers)
    row_data = [page, title, product_description, book_rating, book_availability,
                upc_data, product_type_data, price_exc_tax_data, price_inc_tax_data, tax_data,
                availability_data, num_reviews_data][0:12]
    dict = {"Title": title, "Description": product_description, "book_rating": book_rating,
            'book_availability': [availability_data], 'upc': [upc_data], 'product_type': [product_type_data],
            'price_exc_tax_name': [price_exc_tax_data], 'price_inc_tax_name': [price_inc_tax_data], 'tax_name':
            [tax_data], 'Availability_name': [availability_data], 'Num_reviews_name': [num_reviews_data]}

    return information

    print(product_information(soup))

    def write_csv(data, filename):
        csv_file = []
        with open(filename, "w", newline = "") as csvfile:
            writer =(csvfile, delimiter:=",")
            writer.writerow(headers)
            for row_data in data:
                writer.writerow(row_data)
    return csv_file

def main():
    url = "https://books.toscrape.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for n in range(0-52):

        category_link(soup)
        book_url(category_link)
        product_information(book_url)
        write_csv(product_information)
    return main