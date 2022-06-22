#!/usr/bin/python3

import time
### README ###


### This is a sample python file that contains several function call ###

def pre_decor(prefix):
	def decor_function(original_function):
		time.sleep(10)
		def wrapper(*args, **kwargs):
			print(prefix, 'Wrapper executed this before "{}"'.format(original_function.__name__))
			result = original_function(*args, **kwargs)
			print(prefix, 'Wrapper executed this after "{}"'.format(original_function.__name__))
			return result	
		return wrapper
	return decor_function


def create_array():
	time.sleep(5)
	return []

def my_sort(a = list):
	time.sleep(7)
	b = a.sort()
	return b

@pre_decor('Testing')
def my_array(n):
	a = create_array()
	for i in range(n):
		a.append(i)
	a = my_sort(a)
	return a

@pre_decor('Testing')
def my_print(a):
	print(a)

my_print(my_array(10))
