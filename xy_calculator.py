def xy_input():
    x1 = 1
    y1 = 1
    x2 = 2
    y2 = 2
    x3 = 5
    y3 = 4
    first_coordinates = (x1, y1)
    second_coordinates = (x2, y2)
    third_coordinates = (x3, y3)
    return first_coordinates, second_coordinates, third_coordinates


def slope_calculator(first_coordinates, second_coordinates):
    (x1, y1) = first_coordinates
    (x2, y2) = second_coordinates
    slope = (y2-y1)/(x2-x1)
    return x1, y1, slope


def xy_analysis(x1, y1, slope, x3):
    calc_y3 = (slope * (x3 - x1)) + y1
    return calc_y3


def line_checker(first_coordinates, second_coordinates, third_coordinates):
    (x1, y1) = first_coordinates
    (x2, y2) = second_coordinates   
    (x3, y3) = third_coordinates
    slope = (y2-y1)/(x2-x1)
    if y3 == (slope * (x3 - x1)) + y1:
        return True
    else:
        return False


def test_line_checker():
    from xy_calculator import line_checker
    first_coordinates = (4, 4) 
    second_coordinates = (8, 8) 
    third_coordinates = (10, 10)
    answer = line_checker(first_coordinates, second_coordinates, third_coordinates)
    expected = True
    assert answer == expected


def line_checker_output():
    result = line_checker(first_coordinates, second_coordinates, third_coordinates)
    return result

   
if __name__ == "__main__":
    first_coordinates, second_coordinates, third_coordinates = xy_input()
    x1, y1, slope = slope_calculator(first_coordinates, second_coordinates)
    x3, calc_y3 = third_coordinates
    print("x1, y1, slope:", slope_calculator(first_coordinates, second_coordinates))
    print("Calculated y3 based on x3:", xy_analysis(x1, y1, slope, x3))
    print("Is hard-coded y3 on line:", line_checker_output())