products = []	# big list
while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input("Please enter product's prices: ")
	#p = []
	#p.append(name)	# small list
	#p.append(price) # small list
	#p = [name, price]	# faster
	#products.append(p)
	products.append([name, price])	# fastest
print(products)