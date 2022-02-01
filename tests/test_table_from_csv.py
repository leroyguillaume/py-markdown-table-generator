from markdown_table_generator import *

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
    [
        Cell("FreeBSD", Alignment.CENTER), 
        Cell("", Alignment.CENTER),
        Cell("", Alignment.CENTER),
    ],
    [
        Cell("Fedora", Alignment.CENTER),
        Cell("", Alignment.CENTER),
        Cell("Red Hat", Alignment.CENTER)
    ],
]


def test_table_from_csv_with_csv():
    table = table_from_csv([])
    assert table == []


def test_table_from_csv():
    with open("tests/table.csv", "r") as file:
        csv = file.readlines()
    table = table_from_csv(csv, ";", Alignment.CENTER)
    assert table == expected_table
