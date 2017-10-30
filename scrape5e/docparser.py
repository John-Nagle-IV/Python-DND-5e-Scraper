import BeautifulSoup

NO_TABLE = {
    "default": [
        {}
    ]
}

def extract_table_data(table_element):
    # type: (BeautifulSoup.Tag) -> dict
    current_fieldnames = []
    field_obj = {}
    current_title = "default"
    for table_row in table_element.findAll("tr"):
        row = [table_header.text for table_header in table_row.findAll("th")]
        if len(row) == 1:
            current_title = row[0]
        elif len(row) > 1:
            current_fieldnames = row
        else:
            data = [table_data.text for table_data in table_row.findAll("td")]
            field_obj.setdefault(current_title, []).append(dict(zip(current_fieldnames, data)))
    caption = table_element.find("caption")
    if current_title == "default" and caption:
        field_obj[caption.text.replace("Table: ", "")] = field_obj["default"]
        del field_obj["default"]
    return field_obj


def extract_all_tables_from_page(page):
    # type: (BeautifulSoup) -> list
    all_tables = [extract_table_data(table) for table in page.findAll("table")]
    return list(filter(lambda data: data != NO_TABLE, all_tables))
