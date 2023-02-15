def my_function():
    # creates an error
    a = 50
    b = 0
    while True:
        try:
            if b == 0:
                raise ValueError("You cannot enter 0 for b")
            c = a/b
        except ValueError as ve:
            print(ve)
            b = float(input("Enter b: "))
        except ZeroDivisionError:
            print("Attempting to divide by zero, please enter non-zero value")
            b = float(input("Enter b: "))
        else:
            return c


def main():
    c = my_function()
    d = 100
    e = d/c
    return e


if __name__ == "__main__":
    print(main())