def add_viewer(name, fan_list=None):
    if isinstance(fan_list, list):
        fan_list.append(name)

        return fan_list

    return [name]
