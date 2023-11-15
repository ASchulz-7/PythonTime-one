
import requests
from bs4 import BeautifulSoup, ResultSet
import csv

#pull book in with url, use soup to parse htlm

page = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page.content, 'html.parser')
titles = soup.find ("title")
for title in titles:
    print(title.string)
book_url = soup.find('a')['href']
 #Prints only the jpg we need
images = soup.find_all('img', {'src' : True})
for img in images:
    if img['src'].endswith('15c9.jpg'):

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


    if response == 200:
        soup = BeautifulSoup(response.content, "html.parser")

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



        print(book_information())

def info_from_category(urls):
    info = []
    for link in urls:
        book_info = book_information(urls)
        info.append(book_info)

        write_csv(urls, book_info['category'])
    return urls
    print(info_from_category())
