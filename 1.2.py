from functools import reduce

def avg(numbers):
    return reduce(sum(),numbers)/len(numbers)
    # return sum(numbers)/len(numbers)
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

print(drop_first_last([1,2,3,4,5]))