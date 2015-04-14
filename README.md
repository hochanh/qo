qo: empowered QuOtes in fish-shell
==================================

## Installation

- Requirement: Python 2.7 or later
- Download `qo.py` and `quotes`, put it wherever you like.
- Put `alias` and `fish_greeting` in to your fish as follow

```bash
alias qo="python /path/to/your/qo/qo.py -d /path/to/your/quotes/dir -f /path/to/your/quotes/file"

set -e fish_greeting
function fish_greeting
    echo ""
    set qo (qo)
    set -l textcol red
    set -l author  cyan
    set_color $textcol -b normal
    echo -e -s $qo | cut -d '|' -f1 | sed 's/^/  /'
    set_color $author -b normal 
    echo -s $qo | cut -d '|' -f2 | sed 's/^/  -/'
end
```

## Configuration

### Quotes files:

- One quote each line with the form: `Quote | Author`
- You can have more than one quote files, default `quotes`:

```bash
qo -f /path/to/quotes/file
```

### More options:

#### Edit quotes

Unfornately you have to edit your favorite quotes by hand, i.e. using your own text editor.

```bash
qo -e
```

#### Sort quotes in quotes file

```bash
qo -s
```

### Even more

Edit [qo.py](qo.py) yourself.

`qo.py` may run in `bash` or other shells. I don't know.
