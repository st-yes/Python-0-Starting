import sys

if (len(sys.argv) > 2):
    print("AssertionError: more than one argument is provided")
elif (len(sys.argv) == 2):
    if sys.argv[1].isdigit() == True or sys.argv[1][1:].isdigit() == True and sys.argv[1][0] == '-':
        num = int(sys.argv[1])
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")