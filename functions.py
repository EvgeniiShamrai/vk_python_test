def get_area(x, y):
    if any([not (isinstance(i, int) or isinstance(i, float)) for i in (x, y)]):
        raise TypeError("The input data must be of type int or float")
    if not (x >= 0 and y >= 0):
        raise TypeError("The input data must be greater then zero")
    return x * y
