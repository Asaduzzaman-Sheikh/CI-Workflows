import pytest 



# Funtion to check the power of a number
def power_calculator( number, power ):
    return number ** power

# Test cases for the power_calculator function
def test_power_calculator():
    assert power_calculator( 2, 3 ) == 8, " Test case 1 failed: 2 raised to the power of 3 should be 8 "
    assert power_calculator( 5, 0 ) == 1, " Test casse 2 failed: Any number raised to the power of 0 should be 1 "
    assert power_calculator( 10, 2 ) == 100, " Test case 3 failed: 10 raised to the power of 2 should be 100 "


# Checking for invalid inputs
def test_power_calculator_invalid_inputs():
    with pytest.raises( TypeError ):
        power_calculator( "a", 2 )
    with pytest.raises( TypeError ):
        power_calculator( 2, "b" )
    with pytest.raises( TypeError ):
        power_calculator( None, 2 )
    with pytest.raises( TypeError ):
        power_calculator( 2, None )
        
        
        
        
        
