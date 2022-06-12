from bs4 import BeautifulSoup
from get_html import get_html_page
import json


def get_company_link_list(url, json_file):

    companies_list = []
    for page_requested in range(1, 3):
        if page_requested > 1:
            url = url + f'?page={page_requested}'
        page_requested += 1

        try:
            html_page = get_html_page(url)
            soup = BeautifulSoup(html_page, 'lxml')
            company_link_list = soup.find(
                'table', class_='enf-list-table'
            ).find_all('a')
        except Exception as ex:
            print(ex)
            company_link_list = None

        if company_link_list:
            for each in company_link_list:
                company_link = 'https://www.enfrecycling.com' + each.get('href')
                companies_list.append(company_link)

            with open(json_file, 'w') as file:
                json.dump(companies_list, file, indent=4)

            print('Got company links in json file')
        else:
            print('company_link_list is empty')
            return 0


def download_pages(json_file):

    with open(json_file) as file:
        url_list = json.load(file)
                                    # If need to continue
                                    # after connection error:
                                    # input last page number you've got:
    link_number = 0                         # =x
    for each_page_url in url_list:          # [x:]
        link_number += 1

        while_step = 1
        success_flag = False
        while not success_flag:
            try:
                html_page = get_html_page(each_page_url)
                with open(f'data/index_{link_number}.html', 'w') as html_file:
                    html_file.write(html_page)
                print(f'Link #{link_number}/{len(url_list)} done with {while_step} tries')
                success_flag = True
            except Exception as e:
                print(e)
                while_step += 1
                success_flag = False
                if while_step > 10:
                    print(f'Try {link_number} failed')
                    break
