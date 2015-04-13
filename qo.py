#!/usr/bin/env python

""" Random quotes for embracing power

If you want to add, edit or remove quotes, use Vim or Notepad
"""

from __future__ import with_statement

import os, random
from optparse import OptionParser, OptionGroup

def random_line(quotefile):
    """Return a random line from a file.

    Require: Quote file must fit into memory
    """
    line = next(quotefile)
    for num, qline in enumerate(quotefile):
        if random.randrange(num + 2): continue
        line = qline
    return line

def _quote_from_quoteline(quoteline):
    """Parse a quoteline (from a quote file) and return a quote.

    A quoteline should be in the format:

        quote | author

    The quote returned will be a dictionary such as:

        { 'content': <quote content>,
          'author': <author> }
    """
    if quoteline.strip().startswith('#'):
        return None
    elif '|' in quoteline:
        content, _, author = quoteline.rpartition('|')
        quote = {'content': content.strip(), 'author': author.strip() }
    return quote

class QuoteDict(object):
    """ The quotes's files are read from disk when the QuoteDict is initialized. """
    def __init__(self, quotedir='.', name='quotes'):
        self.name = name
        self.quotedir = quotedir
        path = os.path.join(os.path.expanduser(self.quotedir), self.name)
        if os.path.exists(path):
            with open(path, 'r') as qfile:
                qline = random_line(qfile)
                self.quotes = _quote_from_quoteline(qline)

    def print_quote(self, author=True):
        print self.quotes['content']
        if author:
            print "-", self.quotes['author']

def _build_parser():
    """Return a parser for the command-line interface."""
    usage = "Usage: %prog [-qo DIR] [-f FILE] [-n]"
    parser = OptionParser(usage=usage)

    config = OptionGroup(parser, "Configuration Options")
    config.add_option("-f", "--file", dest="name", default="quotes",
                      help="the quotes file", metavar="FILE")
    config.add_option("-q", "--quote-dir", dest="quotedir", default="",
                      help="the quotes directory", metavar="DIR")
    parser.add_option_group(config)

    output = OptionGroup(parser, "Output Options")
    output.add_option("-n", "--no-author",
                      action="store_false", dest="author", default=True,
                      help="don't print the quote's author")
    parser.add_option_group(output)

    return parser

def _main():
    """Run the command-line interface."""
    (options, args) = _build_parser().parse_args()

    qd = QuoteDict(quotedir=options.quotedir, name=options.name)
    try:
        qd.print_quote(author=options.author)
    except:
        print ""

if __name__ == '__main__':
    _main()
