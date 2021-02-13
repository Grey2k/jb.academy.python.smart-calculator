def select_dates(potential_dates):
    persons = []

    for person in potential_dates:
        if (person.get('age') > 30
                and 'art' in person.get('hobbies')
                and person.get('city') == 'Berlin'):
            persons.append(person.get('name'))

    return ', '.join(persons)
