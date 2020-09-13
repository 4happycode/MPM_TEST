# python_3
 
def larrgestPalindrome(n): 
  
	upper_limit = 0
	i1=''
	j1=''
   
	for i in range(1, n+1): 
	  
		upper_limit =upper_limit * 10
		upper_limit =upper_limit + 9
	  
	lower_limit = 1 + upper_limit//10
   
	max_product = 0 # Initialize result 
	for i in range(upper_limit,lower_limit-1, -1): 
	  
		for j in range(i,lower_limit-1,-1): 

			product = i * j 
			if (product < max_product): 
				break
			number = product 
			reverse = 0

			while (number != 0): 
			  
				reverse = reverse * 10 + number % 10
				number =number // 10
			  
			if (product == reverse and product > max_product):
				i1 = str(i)
				j1 = str(j)
				max_product = product

	print(i1,'*', j1)
	return max_product 
  
n = int(input("Please Input Integer : "))
if n <= 4:
	print(larrgestPalindrome(n)) 
