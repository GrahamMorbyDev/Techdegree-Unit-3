breed_data = {
    'name': 'Javier Hernandez',
    'pets': [
        {
            'name': 'Kitty',
            'breed': 'American Shorthair'
        },
        {
            'name': 'Buzz',
            'breed': 'Pitbull'
        }
    ],
    'classes': ('Math', 'Science', 'Art')
}


def breeds(data):
    breeds_list = []
    for i in data['pets']:
        breeds_list.append(i['breed'])
    return breeds_list


print(breeds(breed_data))
