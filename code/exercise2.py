def move_to_bottom(d, key):
    if key not in d:
        return "The key is not in the dictionary"
    
    value = d[key]
    
    del d[key]
    
    d[key] = value
    
    return d

if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    print(move_to_bottom(example_dict, 1))

    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    print(move_to_bottom(example_dict, 2))

    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    print(move_to_bottom(example_dict, 4))


