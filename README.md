qo: empowered QuOtes in fish-shell
==================================

## Installation

- Requirement: Python2
- Download `qo.py` and `quotes`, put it wherever you like.
- Put `alias` and `fish_greeting` in to your fish as follow

```bash
alias qo="python /path/to/your/qo/qo.py -q /path/to/your/quotes/dir -f you/quotes/file"

set -e fish_greeting
function fish_greeting
    qo
end
```

## Configuration

### Quotes file

One quote each line with the form: `Quote | Author`

Unfornately you have to edit your favorite quotes by hand, i.e. using your own text editor.

### More config

```
qo -h
```

### Even more

Edit [qo.py](qo.py) yourself.

`qo.py` may run in `bash` or other shells. I don't know.
