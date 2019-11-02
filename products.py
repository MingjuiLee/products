import os	# operating systen

# read file: 只做read file的部分 不做檢查檔案是否存在
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
	 	for line in f:	# line is string
	 		if 'Product,Price' in line:
	 			continue	# 繼續
	 		name, price = line.strip().split(',')	# 先把換行符號\n去掉 在進行split(',') 用逗點,當作切割的標準
	 		products.append([name, price])	# only want to put real product and price in list, no header
	return products


# let user input
def user_input(products):
	while True:
		name = input('Please enter product name: ')
		if name == 'q':
			break
		price = input("Please enter product's prices: ")	# string, not integer or float
		price = int(price)	# note
		products.append([name, price])	# fastest
	print(products)
	return products  # have changed, so return

# print all transaction record
def print_products(products):	# 傳遞products 避免伸手去外面拿
	for p in products:
		print('The price of %s is %s' %(p[0], p[1]))	# normal func, no need to return

# write in file: 名副其實 function應該簡潔單純”單一“
def write_file(filename, products):    # paeameters
	with open(filename, 'w', encoding='utf-8') as f:	# 'w': write, as f: use f to represent products.txt
		f.write('Product,Price\n') # column name
		for p in products:	# 要一筆一筆從products裡面讀 再寫回去
			f.write(p[0] + ',' + str(p[1]) + '\n')	# need to cast to string again
# exit with, file is already closed. with: close automatically

# main function 程式的進入點
def main():
	filename = 'products.csv'	# 降低重複性 比較好的做法
	if os.path.isfile(filename):	# check file exist or not
		print('yeah! Find this file!')
		products = read_file(filename)	
	else:
		print("Can't find file")

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()	# 呼叫main function 進入程式

# refractor 重構 重新架構