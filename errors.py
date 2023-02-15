def my_function():
    # creates an error
    a = 50
    b = 0
    c = a/b
    return c


def main():
    c = my_function()
    d = 100
    e = d/c
    return e


if __name__ == "__main__":
    print(main())
