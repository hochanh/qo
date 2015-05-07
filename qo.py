#!/usr/bin/env python

"""Random quotes for embracing power"""

import os
import time
import random
import sys
from optparse import OptionParser, OptionGroup
from subprocess import call

def PrintErrMsg(msg):
    print msg
    sys.exit(1)

def _random_line(quotefile):
    """Return a random line from a file.
    Require: Quote file must fit into memory
    """
    line = next(quotefile)
    for num, qline in enumerate(quotefile):
        if random.randrange(num + 2): continue
        line = qline
    return line

def _one_quote_a_day(quotefile):
    """Return only one quote for one particular day 
    Require: Quote file must fit into memory
    """
    # Days since the epoch
    today = time.time() / 60 / 60 / 24
    lines = quotefile.readlines()
    today_line = int(today) % len(lines)
    return lines[today_line]

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
        quote = {'content': content.strip(), 'author': author.strip()}
    return quote

class QuoteDict(object):
    def __init__(self, quotedir='.', name='quotes'):
        "Init file directory and file name when start program"
        self.name = name
        self.quotedir = quotedir

    def print_quote(self, rand=True):
        "Print quote at random"
        path = os.path.join(os.path.expanduser(self.quotedir), self.name)
        if os.path.isdir(path):
            PrintErrMsg("Invalid Path!")
        if os.path.exists(path):
            with open(path, 'r') as qfile:
                if rand:
                    qline = _random_line(qfile)
                else:
                    qline = _one_quote_a_day(qfile)
                my_quote = _quote_from_quoteline(qline)
        else:
            PrintErrMsg("Quote file not found!")
        print my_quote['content']
        print "|", my_quote['author']

    def sort_quote(self):
        "Sort quotes using UNIX command sort"
        path = os.path.join(os.path.expanduser(self.quotedir), self.name)
        if os.path.exists(path):
            call(["sort", path,  "-o", path])
        else:
            PrintErrMsg("Command not found, are you using UNIX?")

    def edit_quote(self, editor="vi"):
        "Edit quotes using your text editor, default: vi"
        path = os.path.join(os.path.expanduser(self.quotedir), self.name)
        if os.path.exists(path):
            try:
                call([editor, path])
            except:
                PrintErrMsg("Default editor (vi) is not available, set your text editor using '--editor'")

def _build_parser():
    """Return a parser for the command-line interface."""
    usage = "Usage: %prog [-d DIR] [-f FILE] [-e --editor EDITOR] [-n]"
    parser = OptionParser(usage=usage)

    action = OptionGroup(parser, "Actions")
    action.add_option("-e", "--edit", dest="edit",
                      action="store_true", default=False,
                      help="edit quotes in quote file using your text editor", metavar="EDITOR")
    action.add_option("-s", "--sort", dest="sort",
                      action="store_true", default=False,
                      help="sort quotes in quote file")
    parser.add_option_group(action)

    config = OptionGroup(parser, "Configuration Options")
    config.add_option("-f", "--file", dest="name", default="quotes",
                      help="set the quotes file", metavar="FILE")
    config.add_option("-d", "--quote-dir", dest="quotedir", default="",
                      help="set the quotes directory", metavar="DIR")
    config.add_option("--editor", dest="editor", default="vi",
                      help="set your text editor for editing quotes", metavar="EDITOR")
    parser.add_option_group(config)

    output = OptionGroup(parser, "Output Options")
    output.add_option("-n", "--no-random",
                      action="store_false", dest="rand", default=True,
                      help="print one quote for one particular day")
    parser.add_option_group(output)

    return parser

def _main():
    """Run the command-line interface."""
    (options, args) = _build_parser().parse_args()

    qd = QuoteDict(quotedir=options.quotedir, name=options.name)
    if options.sort:
        qd.sort_quote()
        print "Quotes sorted!"
    elif options.edit:
        qd.edit_quote(editor=options.editor)
    else:
        qd.print_quote(rand=options.rand)

if __name__ == '__main__':
    _main()
