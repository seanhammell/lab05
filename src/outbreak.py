"""
Author: Sean Hammell
Filename: outbreak.py
Date: 02/24/2023
Purpose: Recursively compute the number of people with the flu on a given day.
"""
def outbreak(day):
    """
    Recursively compute the number of people with the flu.
    """
    if day == 1:
        return 6
    elif day == 2:
        return 20
    elif day == 3:
        return 75
    
    return outbreak(day - 1) + outbreak(day - 2) + outbreak(day - 3)

def main():
	"""
	Launching point of the program.
	"""
    print("OUTBREAK!")
    day = int(input("What day do you want a sick count for?: "))
    if (day < 1):
        print("Invalid day")
    else:
        print(f"Total people with flu: {outbreak(day)}")

if __name__ == "__main__":
	main()