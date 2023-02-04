def test_HDL_analysis():
    from Blood_Calculator import HDL_analysis
    # Arrange
    HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Normal"