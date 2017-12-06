def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

grades=[3,5,2,1,5,7,7,8,3,1,60]

drop_first_last(grades)