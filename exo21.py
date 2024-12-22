import math
from typing import Union, List

def length(lst: list) -> int:
    """
    Calculate the number of elements in a list.
    
    Args:
        lst: Input list
        
    Returns:
        Number of elements in the list
        
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return len(lst)

def mean(lst: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.
    
    Args:
        lst: List of numbers
        
    Returns:
        Arithmetic mean of the list
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("Cannot calculate mean of empty list")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("All elements must be numeric")
        
    return sum(lst) / len(lst)

def range_of_list(lst: List[Union[int, float]]) -> float:
    """
    Calculate the range (max - min) of a list of numbers.
    
    Args:
        lst: List of numbers
        
    Returns:
        Difference between maximum and minimum values
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("Cannot calculate range of empty list")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("All elements must be numeric")
        
    return max(lst) - min(lst)

def median(lst: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.
    
    Args:
        lst: List of numbers
        
    Returns:
        Median value of the list
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("Cannot calculate median of empty list")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("All elements must be numeric")
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_lst[mid-1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

def standard_deviation(lst: List[Union[int, float]]) -> float:
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        lst: List of numbers
        
    Returns:
        Standard deviation of the list
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("Cannot calculate standard deviation of empty list")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("All elements must be numeric")
    
    list_mean = mean(lst)
    squared_diff_sum = sum((x - list_mean) ** 2 for x in lst)
    return math.sqrt(squared_diff_sum / len(lst))

def get_statistics(lst: List[Union[int, float]]) -> dict:
    """
    Calculate comprehensive statistics for a list of numbers.
    
    Args:
        lst: List of numbers
        
    Returns:
        Dictionary containing various statistical measures
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
    """
    try:
        return {
            "length": length(lst),
            "mean": mean(lst),
            "median": median(lst),
            "range": range_of_list(lst),
            "standard_deviation": standard_deviation(lst),
            "min": min(lst),
            "max": max(lst)
        }
    except (ValueError, TypeError) as e:
        return {"error": str(e)}

# Test the functions
def run_tests():
    test_cases = [
        [],                     # Empty list
        [5],                    # Single element
        [1, 2, 3, 4, 5],       # Positive integers
        [-2, -1, 0, 1, 2],     # Mixed positive and negative
        [1.5, 2.5, 3.5],       # Floating point numbers
        [100, -100, 50, -50]   # Large range
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_case}")
        try:
            stats = get_statistics(test_case)
            print("Statistics:", stats)
        except (ValueError, TypeError) as e:
            print("Error:", str(e))

if __name__ == "__main__":
    run_tests()