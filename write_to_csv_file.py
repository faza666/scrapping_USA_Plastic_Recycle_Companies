import csv
import os
from read_data import read_company_data


def write_data(csv_file_name):
    with open(csv_file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'P/n',
                'Company name',
                'Phone number',
                'e-mail',
                'State',
                'City',
                'Address',
                'Post code',
                'Type of Recycled Materials',
                'Materials Accepted',
                'Recycled Products',
                'Website',
                'Last update',
                'Location'
            )
        )

    steps_count = 0
    for each_file in os.listdir('data'):

        steps_count += 1
        try:
            company_data = read_company_data(f'data/index_{steps_count}.html', steps_count)
            with open(csv_file_name, 'a') as file:
                writer = csv.writer(file)
                writer.writerow(
                    company_data[0]
                )
            if company_data[1]:
                print(f"Company #{steps_count}) has an error")
        except Exception as e:
            print(e)

    print(f'Writing file is complete')
