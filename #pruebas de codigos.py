while True:
    keys = ('a', 'b', 'c')
    new_dict = dict.fromkeys(keys.get('a'), 'initial')
    print(new_dict)
    input()
# Resultado: {'a': 'initial', 'b': 'initial', 'c': 'initial'}
