def is_armstrong_number(number):
	length = len(str(number))
	return number == sum(int(digit) ** length for digit in str(number))