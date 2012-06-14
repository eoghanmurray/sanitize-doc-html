from BeautifulSoup import BeautifulSoup, Comment
import codecs
import sys
valid_tags = 'p i strong b a h1 h2 h3 h4 pre br img ul li'.split()
valid_attrs = 'href src'.split()
value = open(sys.argv[1]).read()
soup = BeautifulSoup(value)
for comment in soup.findAll(
    text=lambda text: isinstance(text, Comment)):
    comment.extract()
for tag in soup.findAll(True):
    if tag.name not in valid_tags:
        tag.hidden = True
    tag.attrs = [(attr, val) for attr, val in tag.attrs
                 if attr in valid_attrs]
print soup.renderContents()
