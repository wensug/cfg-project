import csv
from statistics import mean 
def calculate_percentage(sales):  
    # for a, b in zip(sales1[::1], sales1[1::1]):
    #     return 100 * (b - a) / a 
    return [100 * (b - a) / a for a, b in zip(sales[::1], sales[1::1])]    

def average(sales): 
    return mean(sales) 

def highest_sales(sales):
    return max(sales)


with open('sales.csv', 'r') as sale_file:
    spreadsheet = csv.DictReader(sale_file)
    sales_month = []
    for row in spreadsheet:
        sales = int(row['sales'])
        sales_month.append(sales)
        print(dict(row))
total_sales = sum(sales_month)
percentaje_month = calculate_percentage(sales_month)
roundpercentage=['%.2f' % elem for elem in percentaje_month]
average_month = average(sales_month)
highest_month = highest_sales(sales_month)
print('highest month: {}'.format(highest_month))
print('The average: {}'.format(average_month))
print('Monthly percentage change: {}' .format(roundpercentage))
print('Total sales: {}'.format(total_sales))
