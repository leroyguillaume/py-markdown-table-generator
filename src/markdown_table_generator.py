"""Markdown table generator"""

from enum import Enum
from math import ceil, floor
from typing import List, Optional


class Alignment(Enum):
    """Alignment"""

    LEFT = 1
    CENTER = 2
    RIGHT = 3


class Cell:
    """Cell"""

    value: str
    alignment: Alignment

    def __init__(self, value: str, alignment: Alignment = Alignment.LEFT) -> None:
        self.value = value
        self.alignment = alignment

    def __eq__(self, other) -> bool:
        if isinstance(other, Cell):
            return self.value == other.value and self.alignment == other.alignment
        return False

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value


Table = List[List[Optional[Cell]]]


def generate_markdown(table: Table) -> str:
    """Generate markdown table

    Keyword arguments:
    table -- Table (row, column)
    """

    if len(table) == 0:
        return ""
    columns_size = __compute_columns_size(table)
    header_row = __generate_row(table[0], columns_size)
    dash_row = __generate_dash_row(table[0], columns_size)
    markdown = header_row + "\n" + dash_row
    for row_index in range(1, len(table)):
        row = table[row_index]
        markdown += "\n" + __generate_row(row, columns_size)
    return markdown


def table_from_csv(
    csv: List[str],
    separator: str = ",",
    alignment: Alignment = Alignment.LEFT,
) -> Table:
    """Create table (row, column) from CSV.

    Keyword arguments:
    csv -- List of CSV lines
    separator -- Column separator
    alignment -- Global table alignment
    """

    rows = [line.strip().split(separator) for line in csv]
    return table_from_string_list(rows, alignment)


def table_from_string_list(
    rows: List[List[Optional[str]]],
    alignment: Alignment = Alignment.LEFT
) -> Table:
    """Create table (row, column) from list of rows.

    Keyword arguments:
    rows -- List of rows
    alignment -- Global table alignment
    """

    table = []
    for row in rows:
        table_row = []
        for cell_value in row:
            if cell_value is None:
                table_row.append(None)
            else:
                cell = Cell(cell_value, alignment)
                table_row.append(cell)
        table.append(table_row)
    return table


def __align_center_string(string, size: int) -> str:
    offset = size / 2 - len(string) / 2
    left_offset = floor(offset)
    right_offset = ceil(offset)
    left_offset_string = __generate_string_with(" ", left_offset)
    right_offset_string = __generate_string_with(" ", right_offset)
    return left_offset_string + string + right_offset_string


def __align_left_string(string, size: int) -> str:
    offset = size - len(string)
    offset_string = __generate_string_with(" ", offset)
    return string + offset_string


def __align_right_string(string, size: int) -> str:
    offset = size - len(string)
    offset_string = __generate_string_with(" ", offset)
    return offset_string + string


def __compute_columns_size(table: Table) -> List[int]:
    columns_size = []
    for row in table:
        for column_index, cell in enumerate(row):
            if cell is not None:
                if len(columns_size) <= column_index:
                    columns_size.append(len(cell.value))
                elif len(cell.value) > columns_size[column_index]:
                    columns_size[column_index] = len(cell.value)
    return columns_size


def __generate_cell_value(cell: Cell, column_size: int) -> str:
    if cell.alignment == Alignment.LEFT:
        return __align_left_string(cell.value, column_size)
    if cell.alignment == Alignment.CENTER:
        return __align_center_string(cell.value, column_size)
    if cell.alignment == Alignment.RIGHT:
        return __align_right_string(cell.value, column_size)
    return NotImplemented


def __generate_dash_row(header_row: List[Optional[Cell]], columns_size: List[int]) -> str:
    string = "|"
    for column_index, column_size in enumerate(columns_size):
        cell = header_row[column_index]
        if cell is None or cell.alignment == Alignment.LEFT:
            string += __generate_string_with("-", column_size + 2) + "|"
        elif cell.alignment == Alignment.CENTER:
            string += ":" + __generate_string_with("-", column_size) + ":|"
        elif cell.alignment == Alignment.RIGHT:
            string += __generate_string_with("-", column_size + 1) + ":|"
    return string


def __generate_string_with(character: str, size: int) -> str:
    string = ""
    for _ in range(0, size):
        string += character
    return string


def __generate_row(row: List[Optional[Cell]], columns_size: List[int]) -> str:
    string = "|"
    for column_index, cell in enumerate(row):
        column_size = columns_size[column_index]
        if cell is None:
            string += " " + __generate_string_with(" ", column_size) + " |"
        else:
            string += " " + __generate_cell_value(cell, column_size) + " |"
    return string
