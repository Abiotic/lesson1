def format_price(price):
	price = int(price)
	return f'Price is: {price} rubles'


number = float(input('Enter your number, please: '))
print(format_price(number))