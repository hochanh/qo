qo: empowered QuOtes in fish-shell
==================================

## Install

- Requirement: Python2
- Download `qo.py` and `quotes` at put it wherever you like.
- Put `alias` and `fish_greeting` in to your fish as follow

```bash
alias qo="python /path/to/your/quotes/qo.py"

set -e fish_greeting
function fish_greeting
    qo
end
```

## Configurations

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
