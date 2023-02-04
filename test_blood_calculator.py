def test_HDL_analysis():
    from Blood_Calculator import HDL_analysis
    # Arrange
    HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Normal"

def test_HDL_analysis_Borderline_Low():
    from Blood_Calculator import HDL_analysis
    # Arrange
    HDL_input = 50
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Borderline Low"

def test_HDL_analysis_Low():
    from Blood_Calculator import HDL_analysis
    # Arrange
    HDL_input = 30
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Low"