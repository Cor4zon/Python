"""
<head><title>The Dormouse's story</title><p>Hey Jude</p></head>
"""

from bs4 import BeautifulSoup
from doc import html_doc

soup = BeautifulSoup(html_doc, 'html.parser')

head_tag = soup.head
print(head_tag)

print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)

print(title_tag.contents)
