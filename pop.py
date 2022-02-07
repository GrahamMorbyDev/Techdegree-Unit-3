def pop(org_list, index):
    try:
        del org_list[int(index)]
        return org_list
    except IndexError:
        return 'Invalid Index'


new_list = ['1', '2', '3', '4']
print(pop(new_list, 8))
