def both_ends(str):

    l=len(str)
    if l<2:
        return

    return str[0:2]+str[-2:]

print(both_ends('geeksforgeeks'))
print(both_ends('peopleinhury'))
print(both_ends('stringconcat'))