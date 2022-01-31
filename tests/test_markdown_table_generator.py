import markdown_table_generator

def test_generate_table():
    md_table = markdown_table_generator.generate_table({})
    assert "table" == md_table
