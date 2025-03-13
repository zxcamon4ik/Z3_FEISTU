import random
import numpy as np

def generate_random_array(size=10, min_val=40, max_val=60, decimals=2):
    """
    Generate an array of random double values within a specified range and decimal precision.
    
    Args:
        size: Number of elements in the array
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)
        decimals: Number of decimal places
        
    Returns:
        List of random values
    """
    result = []
    for _ in range(size):
        # Generate random value and round to specified decimal places
        value = round(random.uniform(min_val, max_val), decimals)
        result.append(value)
    
    return result

ra = generate_random_array()
for i in range(len(ra)):
    print(ra[i], end=" ")


print("\n")
