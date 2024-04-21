import sys

def ft_filter(func, items):
    '''
    filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    for item in items:
        if func(item) == True:
            yield item

def ft_filter_v2(func, items):
    return [item for item in items if func(item) == True]


def isEven(x):
    return x % 2 == 0


