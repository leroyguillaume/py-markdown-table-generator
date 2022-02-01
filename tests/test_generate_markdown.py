from markdown_table_generator import *

table = [
    [
        Cell("OS"),
        Cell("Creator", Alignment.CENTER),
        Cell("Company", Alignment.RIGHT),
    ],
    [Cell("Ubuntu"), Cell("Mark Shuttleworth"), Cell("Canonical")],
    [Cell("FreeBSD"), None, None],
    [Cell("Fedora"), None, Cell("Red Hat", Alignment.RIGHT)],
]


def test_generate_markdown_with_empty_table():
    markdown = generate_markdown([])
    assert markdown == ""


def test_generate_markdown():
    markdown = generate_markdown(table)
    with open("tests/table.md", "r") as file:
        expected_markdown = file.read()
    assert markdown == expected_markdown
