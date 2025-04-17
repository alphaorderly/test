import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from fib import fibonacci

def main():

    print("Hello, World! And welcome to the Python world.")
    print("This is an additional message for the user.")
    print("sonTest")
    print("sonTest")
    print("sonTest")
    print("sonTest")
    print("Goodbye!")
    print("sonTest")
    print("sonTest")
    n = 10
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    print("Goodbye!")
    print("Thank you for using the Fibonacci calculator!")


if __name__ == "__main__":
    main()