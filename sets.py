def check_name(str1, str2):
    str1_set = set(str1)
    str2_set = set(str2)
    str_in_set = str2_set.issubset(str1_set)
    return str_in_set


print(check_name('treehouse', 'bob'))


