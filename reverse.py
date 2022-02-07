def reverse(string):
    new_str = ''
    for i in string:
        new_str = i + new_str
    return new_str


print(reverse('graham'))
