# argexplain

A simple Python script that explains the arguments it receives, as well as lines it receives from `stdin`.

## Examples

One argument that includes a space:

```bash
$ argexplain "hello world"
Received 0 lines from stdin

Received 1 arguments from the command-line after parsing via argparse:
  0) 'hello world'
```

Two arguments:

```bash
$ argexplain hello world
Received 0 lines from stdin

Received 2 arguments from the command-line after parsing via argparse:
  0) 'hello'
  1) 'world'
```

One argument, separated by a non-breaking space:

```bash
$ argexplain hello world
Received 0 lines from stdin

Received 1 arguments from the command-line after parsing via argparse:
  0) 'hello\xa0world'
```

Verbose mode:

```bash
$ argexplain hello world -v
Received 0 lines from stdin

Received 1 arguments from the command-line after parsing via argparse:
                     0) hello\xa0world                      
┏━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━┓
┃ Char. ┃ Codepoint ┃ Name                 ┃ Repr.  ┃ Hex  ┃
┡━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━┩
│ h     │ h         │ LATIN SMALL LETTER H │ 'h'    │ 0x68 │
│ e     │ e         │ LATIN SMALL LETTER E │ 'e'    │ 0x65 │
│ l     │ l         │ LATIN SMALL LETTER L │ 'l'    │ 0x6c │
│ l     │ l         │ LATIN SMALL LETTER L │ 'l'    │ 0x6c │
│ o     │ o         │ LATIN SMALL LETTER O │ 'o'    │ 0x6f │
│ \xa0  │ \xa0      │ NO-BREAK SPACE       │ '\xa0' │ 0xa0 │
│ w     │ w         │ LATIN SMALL LETTER W │ 'w'    │ 0x77 │
│ o     │ o         │ LATIN SMALL LETTER O │ 'o'    │ 0x6f │
│ r     │ r         │ LATIN SMALL LETTER R │ 'r'    │ 0x72 │
│ l     │ l         │ LATIN SMALL LETTER L │ 'l'    │ 0x6c │
│ d     │ d         │ LATIN SMALL LETTER D │ 'd'    │ 0x64 │
└───────┴───────────┴──────────────────────┴────────┴──────┘
```

Via stdin:

```bash
$ argexplain <<< "hello
> world"
Received 2 lines from stdin:
  0) 'hello'
  1) 'world'
```

## Installation

`argexplain` is not (yet) on PyPI, so you'll need to install directly from GitHub.

### Via pipx (recommended):

```console
pipx install git+https://github.com/tchamberlin/argexplain
```

### Via pip:

```console
pip install git+https://github.com/tchamberlin/argexplain
````


## Development

```console
git clone git+https://github.com/tchamberlin/argexplain
cd argexplain
hatch shell
```
