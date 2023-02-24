"""
Author: Sean Hammell
Filename: fibonacci.py
Date: 02/24/2023
Purpose: Find the ith fibonacci value or verify a number is in the sequence.
"""
def ith_fibonacci(i):
    """
    Recursively computes the ith fibonacci number.
    """
    if i < 2:
        return i

    return ith_fibonacci(i - 1) + ith_fibonacci(i - 2)

def verify_fibonacci(num):
    """
    Determines if the given number is a part of the fibonacci sequence.
    """
    i = 0
    while True:
        fib_val = ith_fibonacci(i)
        if fib_val == num:
            print(f"{num} is in the sequence")
            return
        elif fib_val > num:
            print(f"{num} is not in the sequence")
            return
        i += 1

def main():
    """
    Launching point of the program.
    """
    try:
        commands = input("Enter mode and value: ").strip().split(" ")
        mode = commands[0]
        value = int(commands[1])

        if value < 0:
            print("Negative values not allowed")
            return

        if mode == "-i":
            print(f"{ith_fibonacci(value)}")
        elif mode == "-v":
            verify_fibonacci(value)
    except:
        print("Valid modes: -i and -v\nValid values: non-negative integers")

if __name__ == "__main__":
	main()