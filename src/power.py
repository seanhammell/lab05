"""
Author: Sean Hammell
Filename: power.py
Date: 02/24/2023
Purpose: Recursively compute the value of a base raised to a power.
"""
def power(base, exp):
	if exp == 0:
		return 1;
	
	return base * power(base, exp - 1)

def main():
	while True:
		try:
			base = int(input("Enter a base: "))
			exp = int(input("Enter a power: "))
			if exp < 0:
				print("Sorry, your exponent must be zero or larger")
				continue
			print(f"Answer: {power(base, exp)}")
			break
		except ValueError:
			print("Please enter an integer for base and power")

if __name__ == "__main__":
	main()