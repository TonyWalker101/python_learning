# practicing math operator usage on strings 

def repeat (s, exclaim):
	result = s*3

	if exclaim:
		result = result+'!!!'
	return result

def main():
	print(repeat('Yay', False))
	print(repeat('Woo Hoo', True))

if __name__ == '__main__':
	main()
