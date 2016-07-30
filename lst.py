lst = [1,2,[3,4,5],6,[7,[8,9]]]
def print_list(lst):
    for item in lst:
        if isinstance(item,list):
            print_list(item)
        else:
            print item
print_list(lst)
