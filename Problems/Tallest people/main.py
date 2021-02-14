def tallest_people(**kwargs) -> None:
    maximum = 0
    persons = {}

    for person, tall in sorted(kwargs.items(), key=lambda x: x[1], reverse=True):
        if tall >= maximum:
            persons[person] = tall
            maximum = tall

    for person in sorted(persons):
        print(f'{person} : {persons.get(person)}')
