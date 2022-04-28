from save_pages import get_company_link_list, download_pages
from write_to_csv_file import write_data

# URL to scrap:
url = 'https://www.enfrecycling.com/directory/plastic-plant/United-States'

# json file to write list of pages links:
json_file = 'all_companies.json'

# file name to write (.csv):
file_name_to_write = 'company_data.csv'


def main():
    get_company_link_list(url=url, json_file=json_file)
    download_pages(json_file=json_file)
    write_data(csv_file_name=file_name_to_write)


if __name__ == '__main__':
    main()
