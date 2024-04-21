def count_in_list(the_list, target):
    count = 0
    for item in the_list:
        if item == target:
            count += 1
    return count

# print(count_in_list(["toto", "tata", "toto"], "tutu"))