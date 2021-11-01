from bs4 import BeautifulSoup
from doc import html_doc

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())


# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)

print(soup.p)
print(soup.p['class'])

# for e in soup.findAll('a'):
#     print(e)
    # print(e['href'])
    # print(e.get('href'))
    # print(e['class'])
    # print(e['id'])

print("\n\n\n")
# print(soup.find(id="link3"))

print(soup.get_text())