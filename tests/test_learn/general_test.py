"""a simple testing example"""
import unittest


def add_three(x:int) -> int:
    """Simple adds 3 to the input inetger

    Args:
        x (int): the user input amount 

    Returns
        int: The result of summary of User input please ineger 3
    """
    return x + 3


def main():
    # tetsing the funtionality add_three function
    assert add_three(1) == 4
    assert add_three(2) == 5
    assert add_three(6) == 9
    print("All test pass!")


if __name__ =="__main__":
   main()