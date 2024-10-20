def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(42, 'тест', False)
values_list = [3.14, 'текст', False]
values_dict = {'a': 100, 'b': 'слово', 'c': None}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    return list_my
