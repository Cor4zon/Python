from bs4 import BeautifulSoup
import requests
page_link ='https://rockbunker.ru/futbolki/'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")


# extract all html elements where price is stored
prices = page_content.find_all(class_='main_price')
# prices has a form:
#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]

# you can also access the main_price class by specifying the tag of the class
prices = page_content.find_all('div', attrs={'class':'section-square__price __no-disc js-price'})

import re

# just = 'Standard Price:20000'
# price = re.findall("\d+", just)[0]

res = []
for i in prices:
    # print(i.contents[0])
    print(type(i.contents[0]))
    print(i.contents[0])
    res.append(re.findall("\d+", i.contents[0]))

print(res)