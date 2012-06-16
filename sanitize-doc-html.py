#!/usr/bin/env python
from bs4 import BeautifulSoup, Comment
import os, sys, optparse, codecs

valid_tags = 'p i em b strong blockquote a h1 h2 h3 h4 pre br img ul ol li'.split()
valid_attrs = 'href src'.split()

def main():
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option("-o", "--output", dest="output_name",
                    action="store",
                    default=False,
                    help="The name of the output html file")
    options, args = parser.parse_args()

    value = open(sys.argv[1]).read()
    soup = BeautifulSoup(value)
    for comment in soup.findAll(
        text=lambda text: isinstance(text, Comment)):
        comment.extract()
    for tag in soup.find_all(True):
        if tag.name not in valid_tags:
            tag.hidden = True
        tag.attrs = dict((attr, val) for attr, val in tag.attrs.items() if attr in valid_attrs)
        if tag.name == 'i':
            tag.name = 'em'
        if tag.name == 'b':
            tag.name = 'strong'
    output = soup.prettify(formatter="html")
    if options.output_name:
        open(os.path.abspath(options.output_name), 'w').write(output)
    else:
        print(output)

if __name__ == "__main__":
    main()
