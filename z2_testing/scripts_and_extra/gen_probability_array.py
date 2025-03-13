import random
import numpy as np

def generate_probability_array(size=10, decimals=2):
    """
    Generate an array of random values between 0 and 1 with specified decimal places,
    where all values sum to exactly 1.
    
    Args:
        size: Number of elements in the array
        decimals: Number of decimal places
        
    Returns:
        List of random values that sum to 1
    """
    # Generate initial random values
    values = [random.random() for _ in range(size)]
    
    # Normalize to sum to 1
    total = sum(values)
    normalized = [v/total for v in values]
    
    # Round to desired decimal places while preserving sum = 1
    rounded = [round(v, decimals) for v in normalized]
    
    # Adjust to ensure sum is exactly 1 after rounding
    rounded_sum = sum(rounded)
    difference = 1 - rounded_sum
    
    if difference != 0:
        # Find the element with the largest value to absorb the rounding difference
        max_index = rounded.index(max(rounded))
        rounded[max_index] = round(rounded[max_index] + difference, decimals)
    
    return rounded

pa = generate_probability_array()
for i in range(len(pa)):
    print(pa[i], end=" ")


print("\n")