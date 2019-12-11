import csv
from statistics import mean 
def calculate_percentage(sales):  
    return [100 * (b - a) / a for a, b in zip(sales[::1], sales[1::1])]    

def average(sales): 
    return mean(sales) 

def highest_sales(highest_month):
    return max(highest_month, key=highest_month.get)
  

def lowest_sales(lowest_month):
    return min(lowest_month, key=lowest_month.get)

with open('sales.csv', 'r') as sale_file:
    spreadsheet = csv.DictReader(sale_file)
    sales_month = []
    month = []
    for row in spreadsheet:
        sales = int(row['sales'])
        sales_month.append(sales)
        month_sales = (row['month'])
        month.append(month_sales)
        print(dict(row))
print(month)
month_sales = dict(zip(month, sales_month))
print(month_sales)
total_sales = sum(sales_month)
percentaje_month = calculate_percentage(sales_month)
roundpercentage=['%.2f' % elem for elem in percentaje_month]
average_month = average(sales_month)
highest_month = highest_sales(month_sales)
lowest_month = lowest_sales(month_sales)
print('lowest month: {}'.format(lowest_month))
print('highest month: {}'.format(highest_month))
print('The average: {}'.format(average_month))
print('Monthly percentage change: {}' .format(roundpercentage))
print('Total sales: {}'.format(total_sales))
