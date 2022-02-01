from markdown_table_generator import *

rows = [
    ["OS", "Creator", "Company"],
    ["Ubuntu", "Mark Shuttleworth", "Canonical"],
    ["FreeBSD", None, None],
    ["Fedora", None, "Red Hat"],
]
expected_table = [
    [
        Cell("OS", Alignment.CENTER),
        Cell("Creator", Alignment.CENTER),
        Cell("Company", Alignment.CENTER),
    ],
    [
        Cell("Ubuntu", Alignment.CENTER),
        Cell("Mark Shuttleworth", Alignment.CENTER),
        Cell("Canonical", Alignment.CENTER),
    ],
    [Cell("FreeBSD", Alignment.CENTER), None, None],
    [
        Cell("Fedora", Alignment.CENTER),
        None,
        Cell("Red Hat", Alignment.CENTER)
    ],
]


def test_table_from_string_list_with_empty_list():
    table = table_from_string_list([])
    assert table == []


def test_table_from_string_list():
    table = table_from_string_list(rows, Alignment.CENTER)
    assert table == expected_table
