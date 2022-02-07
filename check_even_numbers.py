#check for even numbers
#function definition


enterNum=input('Enter a number:')
def check_even_numbers(number):	

	if number % 2==0:
		print (f'{number} is an even number')			# returns true if nuber is even
	else:
		print (f'{number} is an odd number')		#returns true if nuber is not even



while not isinstance(enterNum, int):
	enterNum=int(input('Enter a valid number:'))
else:
	check_even_numbers(enterNum)



