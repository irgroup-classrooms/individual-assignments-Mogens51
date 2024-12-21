import re 


def main():
    
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    regex = r'\d+'

    # Match the regex with the text
    orders = re.findall(regex, text)

    # Print the results
    print(orders)
    
# Python code
if __name__ == '__main__':
    main()
import re
from collections import Counter

def extract_order_numbers(text):
    regex = r'\d+'
    return re.findall(regex, text)

def extract_product_names(text):
    regex = r'[A-Za-z\s]+'
    return re.findall(regex, text)

def extract_prices(text):
    regex = r'\$\d+\.\d{2}'
    return re.findall(regex, text)

def extract_order_dates(text):
    regex = r'\d{2}/\d{2}/\d{4}'
    return re.findall(regex, text)

def find_expensive_orders(text):
    prices = extract_prices(text)
    return [price for price in prices if float(price[1:]) > 500]

def change_date_format(text):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', text)

def extract_long_product_names(text):
    product_names = extract_product_names(text)
    return [name for name in product_names if len(name) > 6]

def count_product_occurrences(text):
    product_names = extract_product_names(text)
    return Counter(product_names)

def find_orders_with_99(text):
    regex = r'\$\d+\.99'
    return re.findall(regex, text)

def find_cheapest_product(text):
    prices = extract_prices(text)
    prices_float = [float(price[1:]) for price in prices]
    return min(prices_float)

def main():
    with open(r'C:\Users\topg\Documents\TH-Köln\Semester_3\DIS08_DatenmodellierungData_Modelling\lokalGithub\individual-assignments-Mogens51\labs\04\orders.csv') as f_in:
        text = f_in.read()

    print("Bestellnummern:", extract_order_numbers(text))
    print("Produktnamen:", extract_product_names(text))
    print("Preise:", extract_prices(text))
    print("Bestelldaten:", extract_order_dates(text))
    print("Bestellungen über $500:", find_expensive_orders(text))
    print("Geändertes Datum:", change_date_format(text))
    print("Produkte mit mehr als 6 Zeichen:", extract_long_product_names(text))
    print("Produktvorkommen:", count_product_occurrences(text))
    print("Bestellungen mit Preisen, die auf .99 enden:", find_orders_with_99(text))
    print("Günstigstes Produkt:", find_cheapest_product(text))

if __name__ == '__main__':
    main()
