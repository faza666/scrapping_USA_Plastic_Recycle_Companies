from bs4 import BeautifulSoup
import re


def read_company_data(html_file, request_number):
    error_flag = False
    with open(html_file) as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    try:
        company_name = soup.find(
            'h1', class_='blue-title', itemprop='name'
        ).text.strip()
    except Exception as e:
        print('company_name:')
        print(e)
        company_name = 'No data'
        error_flag = True

    try:
        company_location = soup.find(
            'td', itemprop='address'
        ).text.strip()
    except Exception as e:
        print('company_location:')
        print(e)
        company_location = 'No data'
        error_flag = True

    if company_location != 'No data':
        try:
            company_address = company_location.split(',')[0].strip()
        except Exception as e:
            print('company_address:')
            print(e)
            company_address = 'No data'
            error_flag = True

        try:
            company_city = company_location.split(',')[1].strip()
        except Exception as e:
            print('company_city:')
            print(e)
            company_city = 'No data'
            error_flag = True

        try:
            company_state = company_location.split(',')[2].strip().split(' ')[0]
        except Exception as e:
            print('company_state:')
            print(e)
            company_state = 'No data'
            error_flag = True

        try:
            company_postcode = company_location.split(',')[2].strip().split(' ')[1]
        except Exception as e:
            print('company_postcode:')
            print(e)
            company_postcode = 'No data'
            error_flag = True
    else:
        company_address = 'No data'
        company_city = 'No data'
        company_state = 'No data'
        company_postcode = 'No data'

    try:
        company_phone = soup.find(
            'td', itemprop='telephone'
        ).text.strip()
    except Exception as e:
        print('company_phone:')
        print(e)
        company_phone = 'No data'
        error_flag = True

    try:
        company_mail = soup.find(
            'td', itemprop='email'
        ).find('a').text.strip()
    except Exception as e:
        print('company_mail:')
        print(e)
        company_mail = 'No data'
        error_flag = True

    try:
        company_website = soup.find(
            'a', itemprop='url'
        ).text.strip()
    except Exception as e:
        print('company_website:')
        print(e)
        company_website = 'No data'
        error_flag = True

    try:
        material_type = soup.find('div', text=re.compile('Type of Recycled Materials'))\
            .find_next_sibling().text.strip()
    except Exception as e:
        # print('material_type:')
        # print(e)
        material_type = 'No data'

    try:
        materials_accepted = soup.find('div', text=re.compile('Materials Accepted:')) \
            .find_next_sibling().text.strip()
    except Exception as e:
        print('materials_accepted:')
        print(e)
        materials_accepted = 'No data'
        error_flag = True

    try:
        recycled_products = soup.find('div', text=re.compile('Recycled Products:')) \
            .find_next_sibling().text.strip()
    except Exception as e:
        print('recycled_products:')
        print(e)
        recycled_products = 'No data'
        error_flag = True

    try:
        last_update = soup.find('div', text=re.compile('Last Update')) \
            .find_next_sibling().text.strip()
    except Exception as e:
        print('last_update:')
        print(e)
        last_update = 'No data'
        error_flag = True

    company_data = (
        request_number,
        company_name,
        company_phone,
        company_mail,
        company_state,
        company_city,
        company_address,
        company_postcode,
        material_type,
        materials_accepted,
        recycled_products,
        company_website,
        last_update,
        company_location
    )
    return [company_data, error_flag]


if __name__ == '__main__':
    data = read_company_data(
        html_file='data/index_1.html',
        request_number=3
    )
    print(data)
