iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    if iris.get(id_n) is None:
        iris[id_n] = {}

    iris[id_n].update({'species': species, 'petal_length': petal_length, 'petal_width': petal_width})
    iris[id_n].update(kwargs)
