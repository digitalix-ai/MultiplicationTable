def create_multiplication_table(width, height):
	output = ""
	num_chars = len(str(width*height)) + 1
	
	for a in range(1, height+1):
		for b in range(1, width+1):
			product = a * b
			
			product_str = str(product)
			product_str = product_str.rjust(num_chars, ' ')
			output += product_str
		output += "\n\n"
	return output
def process_input(raw_input):
	if int(raw_input) > 0:
		value = int(raw_input)
	
	return value
	
def get_user_input():
	values = []
	for prompt in ('Width', 'Height'):
		raw_input = input(prompt + ": ")
		processed_input = process_input(raw_input)
		values.append(processed_input)
	
	return values
	
def main():
	success = False
	try:
		width, height = get_user_input()
		success = True
	except:
		print("\nUser input must be a positive integer.")
	
	if success:
		output = create_multiplication_table(width, height)
		print("\n\n" + output)

if __name__ == "__main__":
	main()