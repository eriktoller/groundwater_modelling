from module import convert_to_complex

if __name__ == "__main__":
    print('Executing main.py')
    print("This is the main module.")

    x = 10.0
    y = 20.0
    complex_number = convert_to_complex(x, y)
    print(f"The complex representation of ({x}, {y}) is {complex_number}")