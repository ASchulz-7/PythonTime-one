
import requests
from bs4 import BeautifulSoup, ResultSet
import csv

#pull book in with url, use soup to parse htlm

page = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page.content, 'html.parser')
SciFiURL = ("https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html")
response = requests.get(SciFiURL)
if response.status_code == 200:
    print("Yay!!")
else:
    print("error code not 200")
page_contents = response.text

soup = BeautifulSoup(response.text, 'html.parser')
# uploaded soup and pulled in science-fiction category page data
def soup_func(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    return soup

def category_link():
    main_url = 'http://books.toscrape.com/index.html'
    request = requests.get(main_url)
    if request.ok:
        soup = BeautifulSoup(request.text, 'html.parser')
        ul = soup.find('ul', class_ = ["nav", "nav-list"])

        li = ul.find_all('li')
        category_requests = []
        for item in li:
            link = item.find('a', href=True)
            if link is not None:
                print(link['href'])
        return category_request

def get_titles(url):
    Book_title_tags = soup.find_all('h3')
    Book_titles = []
    for tags in Book_title_tags:
        Book_titles.append(tags.text)
    return Book_titles
get_titles(soup)
print(get_titles(soup))

def obtain_book_price(url):
    book_price_tags = soup.find_all('p', class_ = "price_color")
    Book_price = []
    for tags in book_price_tags:
        Book_price.append(tags.text.replace('Â', ''))
    return Book_price

def extract_book_links(soup):
    h3_tags = soup.find_all('h3')
    book_links = []
    base_url = 'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html'
    for tag in h3_tags:
        book_links.append(f'https://books.toscrape.com/catalogue/{tag.contents[0]['href'].replace("../../../","")}')
#extracts all html code for scifi page
    next_page = soup.find(('li'), class_ = "next")
    if next_page:
        url_page = next_page.get('href')
        page += 1
    else:
        breakpoint()

    return book_links
#print(extract_book_links(soup))

def book_information(url):
    print("ready")
    response = requests.get(h3_tag)

    if response == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        titles = url.find ("title")
        product_description = url.find('article', class_="product_page").find_all('p')[3].text.strip()
        book_rating = url.find('p', class_='star-rating').text.strip()
        book_availability = url.find('p', class_='availability').text.strip()
        upc_data = url.find('table', class_="table table-striped").find_all('td')[0]
        product_type_data = url.find('table', class_="table table-striped").find_all('td')[1].text.stri
        Price_exc_tax_data = url.find('table', class_="table table-striped").find_all('td')[2].text.strip()
        price_inc_tax_data = url.find('table', class_ = "table table-striped").find_all ('td') [3].text.strip()
        tax_data = url.find('table', class_ = "table table-striped").find_all ('td') [4].text.strip()
        availability_data = url.find('table', class_ = "table table-striped").find_all ('td') [5].text.strip()
        num_reviews_data = url.find('table', class_ = "table table-striped").find_all ('td') [6].text.strip()

        headers = [page, "Title", "Description", "Rating", "Availability", "UPC", "Product Type",
           "Tax Excluded Price", "Tax Included Price", "Tax",
          " Availability", "Reviews"]

        row_data = [page, title.string, product_description, book_rating, book_availability, upc_data, product_type_data,
                Price_exc_tax_data, price_inc_tax_data, tax_data,
                availability_data, num_reviews_data][0:12]

        dict = ({
                        "url" : 'url',
                        "Title": titles,
                      "Description": product_description,
                         "Rating": book_rating,
                        "Availability": [availability_data],
                        "UPC": [upc_data],
                        "Type": [product_type_data],
                        "Price without Tax": [Price_exc_tax_data],
                        "Price with Tax": [price_inc_tax_data],
                        "Tax": [tax_data],
                        "Number of Reviews": [num_reviews_data]})

        return dict

        print(book_information())

def info_from_category(urls):
    info = []
    for link in urls:
        book_info = book_information(urls)
        info.append(book_info)

        write_csv(urls, book_info['category'])
    return urls
    print(info_from_category())
