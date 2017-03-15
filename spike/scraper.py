import BeautifulSoup
import os

def get_sample_gods_content():
    full_content_path = os.path.join(os.path.dirname(__file__), "sample/gods.htm")
    with open(full_content_path, mode='r') as read_stream:
        return read_stream.read()

def html_table_to_dict(tabel_element):
    # type: (BeautifulSoup.Tag) -> None
    table_dict = {}
    table_as_list_list = []
    for table_row in tabel_element.findAll("tr"):
        for table_headder in table_row.findAll("th"):


def main():
    content = get_sample_gods_content()
    soup = BeautifulSoup.BeautifulSoup(content)
    html_table_to_dict(soup.find("table"))


if __name__ == '__main__':
    main()