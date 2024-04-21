import sys



NESTED_MORSE = {
    ' ': '/ ',
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

def convertMorseCode(text):
    morse_text = ""
    for char in text:
        if char != ' ' and char.isalnum() == False:
            return False
        morse_text += NESTED_MORSE[char.upper()]
    return morse_text

if __name__ == '__main__':
    args = sys.argv
    if (len(args) != 2):
        print("AssertionError: the arguments are bad")
    else:
        morse = convertMorseCode(args[1])
        if (morse == False):
            print("AssertionError: the arguments are bad")
        else:
            print(morse)
    