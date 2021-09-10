import argparse
import codecs
import csv


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--items', help='The list of items that needs to be added')
    parser.add_argument('--customers', help='The file containing the list of customers that need the items')
    args = parser.parse_args()
    return args.items, args.customers


def load_data(f: str):
    data = []
    with open(f, 'r', newline='') as csv_file:
        data = list(csv.DictReader(csv_file))
    return data


def combine_list(customers: list, items: list):
    """creates a single list.  For every item in items is repeated for every customer in customers"""
    new_list = []
    for customer in customers:
        for item in items:
            new_list.append({'id': customer['ID'].strip(),
                             'prod nbr': item['Product ID'].strip(),
                             'price basis': item['Price Basis'].strip(),
                             'price formula': item['Price Formula'].strip(),
                             'cost basis': item['Cost Basis'].strip(),
                             'cost formula': item['Cost Formula'].strip()
                             })
    return new_list


def write_combined_file(d: list):
    fieldnames = ['id', 'prod nbr', 'price basis', 'price formula', 'cost basis', 'cost formula']
    with open('c:/users/awhite/downloads/out.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for e in d:
            writer.writerow(e)


def main():
    item_file, customer_file = get_args()
    print(item_file, customer_file)
    items = load_data(item_file)
    customers = load_data(customer_file)
    combined = combine_list(customers, items)
    for e in combined:
        print(e)
    write_combined_file(combined)


if __name__ == '__main__':
    main()
