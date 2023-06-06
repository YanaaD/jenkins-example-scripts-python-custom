import random

def min_sum() -> int:
    """
    Finds the minimum value in each list
    and returns their sum.
    """
    randomlist1 = random.sample(range(10, 300), 5)
    print(randomlist1)
    randomlist2 = random.sample(range(10,300), 5)
    print(randomlist2)

    return min(randomlist1) + min(randomlist2)

if __name__ == "__main__":   
   print(min_sum())

