def test_slope_calculator():
    from xy_calculator import slope_calculator
    first_coordinates = (4, 4)
    second_coordinates = (8, 8)  
    answer = slope_calculator(first_coordinates, second_coordinates)
    expected = (4, 4, 1)
    assert answer == expected

def test_xy_analysis():
    from xy_calculator import xy_analysis
    x1 = 2
    y1 = 2
    slope = 1
    x3 = 6
    answer = xy_analysis(x1, y1, slope, x3)
    expected = 6
    assert answer == expected

def test_line_checker():
    from xy_calculator import line_checker
    first_coordinates = (4, 4) 
    second_coordinates = (8, 8) 
    third_coordinates = (10, 10)
    answer = line_checker(first_coordinates, second_coordinates, third_coordinates)
    expected = True
    assert answer == expected

def test_line_checker():
    from xy_calculator import line_checker
    first_coordinates = (4, 4) 
    second_coordinates = (8, 8) 
    third_coordinates = (10, 20)
    answer = line_checker(first_coordinates, second_coordinates, third_coordinates)
    expected = False
    assert answer == expected
