"""
Author: Sean Hammell
Filename: power.py
Date: 02/24/2023
Purpose: Compute the value of a user-provided base and power.
"""
def power(base, exp):
	"""
	Recursively computes the value of a base raised to a power.
	"""
	if exp == 0:
		return 1;
	
	return base * power(base, exp - 1)

def main():
	"""
	Launching point of the program.
	"""
	while True:
		try:
			base = int(input("Enter a base: "))
			exp = int(input("Enter a power: "))
			while exp < 0:
				print("Sorry, your exponent must be zero or larger")
				exp = int(input("Enter a power: "))
			print(f"Answer: {power(base, exp)}")
			break
		except ValueError:
			print("Please enter an integer for base and power")

if __name__ == "__main__":
	main()