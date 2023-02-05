def xy_input():
    x1 = float(input("Enter the value of x1: "))
    y1 = float(input("Enter the value of y1: "))
    x2 = float(input("Enter the value of x2: "))
    y2 = float(input("Enter the value of y2: "))
    first_coordinates = x1, y1
    second_coordinates = x2, y2
    return first_coordinates, second_coordinates

def slope_calculator(first_coordinates, second_coordinates):
    x1, y1 = first_coordinates
    x2, y2 = second_coordinates
    slope = (y2-y1)/(x2-x1)
    return x1, y1, slope

def xy_analysis(x1, y1, slope, x3):
	y3 = (slope * (x3 - x1)) + y1
	return y3

first_coordinates, second_coordinates = xy_input()
x1, y1, slope = slope_calculator(first_coordinates, second_coordinates)
x3 = float(input("Enter the value of x3: "))
result = xy_analysis(x1, y1, slope, x3)
print("The value of y3 is:", result)
