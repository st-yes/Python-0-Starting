import string
import sys


def char_analysis(input):

    """
    return a list of the following:
    - number of chars,
    - number of upper letters
    - number of lower letters
    - number of punctuation
    - number of spaces
    - number of digits
    """
    output = [len(input), 0, 0, 0, 0, 0]
    for char in input:
        if char.isupper():
            output[1] += 1
        elif char.islower():
            output[2] += 1
        elif char in string.punctuation:
            output[3] += 1
        elif char.isspace():
            output[4] += 1
        elif char.isdigit():
            output[5] += 1
    return output


if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        input_str = input("What is the text to count?\n")
    elif (len(sys.argv) > 2):
        print("AssertionError: AssertionError:"
              " more than one argument is provided")
        exit()
    else:
        input_str = sys.argv[1]
    count = char_analysis(input_str)
    print(f"The text contains {count[0]} characters:\n"
          f"{count[1]} upper letters\n{count[2]} lower letters\n"
          f"{count[3]} punctuation marks\n"
          f"{count[4]} spaces\n{count[5]} digits")
