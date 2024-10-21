"""a simple testing example"""



def add_three(x:int)-> int:
    return x + 3


def main():
    # tetsing teh fducntion add_three
    assert add_three(1) == 4
    assert add_three(2) == 5
    assert add_three(6) == 9
    print("All test pass!")


if __name__ =="__main__":
    main()