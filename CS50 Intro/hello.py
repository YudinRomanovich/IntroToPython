
def main():
	# Ask user for their name
	# Remove witespace from str and capitalize user name
	name = input("What's your name? ").strip().title()
	print(hello(name))

	
def hello(to="World"):
	return f"hello, {to}"


if __name__ == "__main__":
	main()
