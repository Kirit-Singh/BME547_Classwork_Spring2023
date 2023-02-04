import pytest

@pytest.mark.parametrize("HDL_input, expected",
    [(65, "Normal"),
    (45, "Borderline Low"),
    (20, "Low")
    ])
def test_HDL_analysis(HDL_input, expected):
    from Blood_Calculator import HDL_analysis
    # Arrange
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected

