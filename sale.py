import csv
def calculate_percentage(sales1):  
    for a, b in zip(sales1[::1], sales1[1::1]):
        print 100 * (b - a) / a

with open('sales.csv', 'r') as sale_file:
    spreadsheet = csv.DictReader(sale_file)
    sales_month = []
    for row in spreadsheet:
        sales = int(row['sales'])
        sales_month.append(sales)
        print(dict(row))
total_sales = sum(sales_month)
calculate_percentage(sales_month)
print(total_sales)
