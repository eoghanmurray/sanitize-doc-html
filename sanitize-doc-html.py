#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup, Comment
import os, sys, optparse, codecs

valid_tags = 'p i strong b a h1 h2 h3 h4 pre br img ul ol li'.split()
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
    for tag in soup.findAll(True):
        if tag.name not in valid_tags:
            tag.hidden = True
        tag.attrs = [(attr, val) for attr, val in tag.attrs
                     if attr in valid_attrs]
    output = soup.renderContents()
    if options.output_name:
        open(os.path.abspath(options.output_name), 'w').writelines(output)
    else:
        print(output)

if __name__ == "__main__":
    main()
