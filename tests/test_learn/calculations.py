
"""Simple funtion to practice TDD """
def add(a:int, b:int):
    """Add funtion

    Args:
        a (int): 
        b (int): 

    Returns:
        a+b
    """
    return a + b

def substract(a:int, b:int):
    """Substract funtion

    Args:
        a (int): 
        b (int): 

    Returns:
        a - b
    """
    return a - b


def divide(a:int, b:int):
    """Divide function
    returns: a/b """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b