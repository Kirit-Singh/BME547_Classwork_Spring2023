# 3A's - Arrange, Act, Assert

def test_HDL_analysis():
	from blood_calculator import test_HDL_analysis
	# Arrange
    HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Normal"