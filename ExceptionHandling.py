try:
    height = float(input("Enter your height: "))
except ValueError:
    print("Invalid input")
    height = 0
else:
    if height > 3:
        raise ValueError("Human height should not be over 3m.")
    else:
        print(f"Your height is {height}")