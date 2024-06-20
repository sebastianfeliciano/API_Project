def find_key(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key
    return None

if __name__ == "__main__":
    example_dict = {
        1: ['red', 'blue', 'green'],
        'Josh Jung': (9, 10),
        3: {0: 0},
        9000: 'impale mat a'
    }

    key = find_key(example_dict, (9, 10))
    print(key)

    key = find_key(example_dict, {0: 0})
    print(key)

    key = find_key(example_dict, 'impale mat a')
    print(key)
