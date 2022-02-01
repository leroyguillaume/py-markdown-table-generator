# py-markdown-table-generator <!-- omit in toc -->

Python library to generate Markdown table.

- [Usage](#usage)
  - [CLI](#cli)
  - [Library](#library)
- [Build](#build)
- [Test](#test)
- [Contribute](#contribute)

## Usage

```bash
pip3 install py-markdown-table-generator-gleroy
```

### CLI

```bash
csv-to-md -s ";" -a c tests/table.csv

# |   OS    |      Creator      |  Company  |
# |:-------:|:-----------------:|:---------:|
# | Ubuntu  | Mark Shuttleworth | Canonical |
# | FreeBSD |                   |           |
# | Fedora  |                   |  Red Hat  |

csv-to-md -s ";" -a r tests/table.csv

# |      OS |           Creator |   Company |
# |--------:|------------------:|----------:|
# |  Ubuntu | Mark Shuttleworth | Canonical |
# | FreeBSD |                   |           |
# |  Fedora |                   |   Red Hat |
```

### Library

```python
from markdown_table_generator import generate_markdown, table_from_string_list

# ====================================================
# Generate markdown table from list of list of strings
# ==================================================== 
rows = [
    ["OS", "Creator", "Company"],
    ["Ubuntu", "Mark Shuttleworth", "Canonical"],
    ["FreeBSD", None, None],
    ["Fedora", None, "Red Hat"],
]
table = table_from_string_list(rows, Alignment.CENTER)
markdown = generate_markdown(table)
print(markdown)

# |   OS    |      Creator      |  Company  |
# |:-------:|:-----------------:|:---------:|
# | Ubuntu  | Mark Shuttleworth | Canonical |
# | FreeBSD |                   |           |
# | Fedora  |                   |  Red Hat  |


# ====================================================
# Generate markdown table from CSV
# ==================================================== 
csv = """
OS;Creator;Company
Ubuntu;Mark Shuttleworth;Canonical
FreeBSD;;
Fedora;;Red Hat
"""
table = table_from_csv(csv.splitlines(), ";", Alignment.RIGHT)
markdown = generate_markdown(table)
print(markdown)

# |      OS |           Creator |   Company |
# |--------:|------------------:|----------:|
# |  Ubuntu | Mark Shuttleworth | Canonical |
# | FreeBSD |                   |           |
# |  Fedora |                   |   Red Hat |
```

## Build

```bash
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m build
```

## Test

```bash
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
pytest
```

## Contribute

```bash
ln -s "$(pwd)/sh/pre-commit.sh" .git/hooks/pre-commit
```
... and let's code!
