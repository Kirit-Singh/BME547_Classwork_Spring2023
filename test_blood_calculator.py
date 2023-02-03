import pytest

# 3A's - Arrange, Act, Assert
@pytest.mark.parametrize("HDL_input, expected")
def test_HDL_analysis(HDL_input, expected):
	from blood_calculator import test_HDL_analysis
	# Arrange
    HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Normal"

def test_HDL_analysis_Borderline_Low():
	from blood_calculator import test_HDL_analysis
	# Arrange
    HDL_input = 45
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Borderline Low"

def test_HDL_analysis_Low():
	from blood_calculator import test_HDL_analysis
	# Arrange
    HDL_input = 45
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Low"