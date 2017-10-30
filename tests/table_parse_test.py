import pytest
import BeautifulSoup
import os
from scrape5e.logs import application_log, remove_all_logs
import json

from scrape5e.docparser import extract_all_tables_from_page

@pytest.fixture(params=[
    "sample/gods.htm",
    "sample/armor.htm",
    "sample/barbarian.htm",
    "sample/dwarf.htm"
])
def test_content(request):
    full_content_path = os.path.join(os.path.dirname(__file__), request.param)
    with open(full_content_path, mode='r') as read_stream:
        yield BeautifulSoup.BeautifulSoup(read_stream.read())
    remove_all_logs()


def test_extract_table_data(test_content):
    application_log.debug(json.dumps(extract_all_tables_from_page(test_content), indent=4, sort_keys=True))
