import math

def NULL_not_found(object: any) -> int:
    if (object in (None, '', False)):
        print(f"{object} {type(object)}")
    elif isinstance(object, (float, int)) and math.isnan(object):
        print(f"{object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0