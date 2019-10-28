products = []	# big list
while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input("Please enter product's prices: ")	# string, not integer or float
	price = int(price)	# note
	#p = []
	#p.append(name)	# small list
	#p.append(price) # small list
	#p = [name, price]	# faster
	#products.append(p)
	products.append([name, price])	# fastest
print(products)

for p in products:
	#print(p)	# print every small list
	#print(p[0]) # print product name
	print('The price of %s is %s' %(p[0], p[1]))

#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

with open('product.csv', 'w', encoding='utf-8') as f:	# 'w': write, as f: use f to represent products.txt
	f.write('Product,Price\n') # column name
	for p in products:
		#f.write(p[0] + ',' + p[1] + '\n')	# use + to combine name, price, ',', and line change, all string
		f.write(p[0] + ',' + str(p[1]) + '\n')	# need to cast to string again
# exit with, file is already closed. with: close automatically