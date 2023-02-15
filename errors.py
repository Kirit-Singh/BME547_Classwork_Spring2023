def my_function():
    # creates an error
    a = 50
    b = 0
    try: 
    	c = a/b
    except ZeroDivisionError:
        print("Attempting to divide by zero, please enter non-zero value")
        b = float(input("Enter b: "))
        c = a/b  
    return c
    

def main():
    c = my_function()
    d = 100
    e = d/c
    return e


if __name__ == "__main__":
    print(main())
