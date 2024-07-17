stock = int(input('Please enter an initial stock level:'))
months = int(input('Please enter the number of month to plan:'))
sales_qty = [
    int(input('Please enter the planned sales quantity:'))
    for i in range(months)
]
print('The resulting production quantities are:')

for i, v in enumerate(sales_qty):
	if stock >= v:
		prod_qty = 0
		stock = stock - v
	else:
		prod_qty = abs(v - stock)
		stock = 0
	print(f'Production quantity month {i+1} - {prod_qty}')
