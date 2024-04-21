import sys
from ft_filter import ft_filter_v2

#this return a lambda function
#
def longer_than(length):
    return lambda a : len(a) >= length


if (__name__ == '__main__'):
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
    else:
        if (sys.argv[2].isdigit() == False):
            print("AssertionError: the arguments are bad")
            exit()
        num = int(sys.argv[2])
        theList = sys.argv[1].split(' ')
        myfunc = longer_than(num) # will return a function where length == num
        print(ft_filter_v2(myfunc, theList))
