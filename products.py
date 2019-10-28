# read file, and then write in new data
products = []	# big list
with open('products.csv', 'r', encoding='utf-8') as f:
 	for line in f:	# line is string
 		if 'Product,Price' in line:
 			continue	# 繼續
 		name, price = line.strip().split(',')	# 先把換行符號\n去掉 在進行split(',') 用逗點,當作切割的標準
 		products.append([name, price])	# only want to put real product and price in list, no header
print(products)	

# let user input
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

# print all transaction record
for p in products:
	#print(p)	# print every small list
	#print(p[0]) # print product name
	print('The price of %s is %s' %(p[0], p[1]))

#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

# write in file
with open('products.csv', 'w', encoding='utf-8') as f:	# 'w': write, as f: use f to represent products.txt
	f.write('Product,Price\n') # column name
	for p in products:
		#f.write(p[0] + ',' + p[1] + '\n')	# use + to combine name, price, ',', and line change, all string
		f.write(p[0] + ',' + str(p[1]) + '\n')	# need to cast to string again
# exit with, file is already closed. with: close automatically