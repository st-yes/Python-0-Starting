from NULL_not_found import NULL_not_found
import sys

std = sys.stdout

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

std.write('Nothing: ')
NULL_not_found(Nothing)
std.write('Garlic: ')
NULL_not_found(Garlic)
std.write('Zero: ')
NULL_not_found(Zero)
std.write('Empty: ')
NULL_not_found(Empty)
std.write('Fake: ')
NULL_not_found(Fake)
print(NULL_not_found("Brian"))