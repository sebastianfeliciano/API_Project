def swap(d):
  keys = d.keys()
  values = d.values()
  swapped_tuples = zip(values, keys)
  value_types = [type(elem) for elem in values]
  
  if type({}) in value_types or type([]) in value_types:
    return 'Cannot swap the keys and values for this dictionary'
  else:
    new_dict = dict(swapped_tuples)
    return new_dict
    
if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    swapped = swap(example_dict)
    print(swapped)

    example_dict = {
        1: [2, 3],
        4: 'four',
        5: 'five'
    }

    swapped = swap(example_dict)
    print(swapped)

    example_dict = {
        1: 'one',
        2: {3: 4},
        5: 'five'
    }

    swapped = swap(example_dict)
    print(swapped)

    example_dict = {
        1: 'one',
        2: 'two',
        3: (4, 5)
    }

    swapped = swap(example_dict)
    print(swapped)
