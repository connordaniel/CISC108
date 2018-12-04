# Lab 10: Welcome to Python
NAMES = ["Connor Daniel", "Olivia Rorke"]

##### Part 1

## Question 1.1) 2pts
age = 69
## Question 1.2) 2pts
title = "But Beautiful"
## Question 1.3) 2pts
price = 15.39
## Question 1.4) 2pts
recently_read = True
## Question 1.5) 2pts
current_year = 2018 * 0 + 8072 - 2018 / 3
## Question 1.6) 2pts
can_drink = 21 >= age
## Question 1.7) 2pts
message = title + " is my favorite book."
##### Part 2

## Question 2.1) 5pts
def average_three(first, second, third):
	'''
	Consumes three integers and produces
	their average.

	Args:
		first (int): First number
		second (int): second number
		third (int): third number
	Returns:
		float: average of the three numbers
	'''
	total = first + second + third
	return total / 3
assert average_three(1,2,3) == 2.0
assert average_three(4,5,6) == 5.0
## Question 2.2) 5pts
def string_join(str1, str2):
	'''
	Consumes two strings and produces
	them joined with a _ inbetween

	Args:
		str1 (string): first string
		str2 (string): second string
	Returns:
		String: joined string
	'''
	return str1 + "_" + str2
assert string_join("hello","world") == "hello_world"
assert string_join("corgi","butts") == "corgi_butts"
## Question 2.3) 5pts
def square(num):
	'''
	Consumes a number and produces the 
	same number squared

	Args:
		num (int): number to be squared
	Returns:
		int: the squared number
	'''
	return num ** 2
assert square(2) == 4
assert square(4) == 16
## Question 2.4) 5pts
def print_square(num):
	'''
	Consumes a number and 
	prints out the number 
	squared.

	Args:
		num (int): the number to be squared
	Returns: nothing
	'''
	print(square(num))
## Question 2.5) 6pts
def print_and_return_square(num):
	'''
	Consumes a number and produces
	the squared number and also prints it

	Args:
		num (int): the number to be squared
	Returns: number squared
	'''
	print(square(num))
	return(square(num))
assert print_and_return_square(4) == 16
assert print_and_return_square(6) == 36
## Question 2.6) 5pts
def sqrt(num):
	'''
	Consumes a number and produces
	the square root of the number
	Args:
		num (int): the number to be rooted
	Returns:
		float: the square root of the number
	'''
	return num ** .5
assert sqrt(25) == 5
assert sqrt(100) == 10
## Question 2.7) 5pts
def calculate_distance(x1,y1,x2,y2):
	'''
	Consumes two points and produces the 
	distance between them
	Args:
		x1,y1: the first point of the graph
		x2,y2: the second point on the graph
	Returns:
		float: distance between the two points
	'''
	distance = sqrt( square(y2-y1) + square(x2-x1) )
	return distance
##### Part 3

## Question 3.1) 10pts
def is_rainy(str):
	'''
	Consumes a string representing the current weather 
	state and produces whether it is raining
	Args:
		str (str): the string, either "rainy", "sunny," or "cloudy"
	Returns:
		bool: true if the string equals rainy
	'''
	if str == "rainy":
		return True
	else:
		return False
assert is_rainy("rainy") == True
assert is_rainy("sunny") == False
## Question 3.2) 10pts
def get_grade(grade):
	'''
	Consumes a number representing a grade
	frome 0 to 100 and produces a string representing
	the grade
	'''
	if grade >= 90:
		return "A"
	elif grade >= 80:
		return "B"
	elif grade >= 70:
		return "C"
	elif grade >= 60:
		return "D"
	else:
		return "F"
assert get_grade(95) == "A"
assert get_grade(88) == "B"
assert get_grade(76) == "C"
assert get_grade(69) == "D"
## Question 3.3) 10pts
def count_down(count):
	'''
	Consumes a number. If the number is greater than zero, it prints the
	 number and recursively calls the function again with the decremented
	 number. If the number is less than zero, 
	it returns -1. Otherwise, it prints the string "The end!"
	'''
	if count > 0:
		print(count)
		return count_down(count - 1)
	elif count < 0:
		return -1
	else:
		print("The end!")
## Question 3.4) 10pts