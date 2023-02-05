def test_xy_analysis():
    from xy_calculator import xy_analysis
    first_coordinates = (1,1)
    second_coordinates = (2,2)
    answer = slope_calculator(first_coordinates,second_coordinates)
    expected = 1
    assert answer == expected
