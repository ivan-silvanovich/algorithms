def gcd(*args):
    args = list(set(args))
    allowed_types = (int, )

    for arg in args:
        if type(arg) not in allowed_types:
            raise TypeError(f'only {allowed_types} objects are allowed')
        elif arg == 0:
            raise ValueError('zero elements are not allowed')

    a = args[0]
    for num in args[1:]:
        b, a = sorted((num, a))

        while b:
            b, a = a % b, b

    return a


def get_optimal_set(capacity, things):
    step = gcd(*(thing['weight'] for thing in things))
    table = []
    empty_cell = {
        'cost': 0,
        'things_list': []
    }

    for _ in range(len(things)):
        line = []

        for __ in range(0, capacity, step):
            line.append(empty_cell.copy())

        table.append(line)

    max_cell = table[0][0]
    for i in range(len(table)):
        for j in range(len(table[i])):
            column_weight = step * (j + 1)
            current_thing = things[i]
            current_cell = table[i][j]
            max_cost_column_cell = table[i - 1][j] if i else empty_cell

            if current_thing['weight'] > column_weight:
                current_cell['cost'] = max_cost_column_cell['cost']
                current_cell['things_list'] = max_cost_column_cell['things_list']
            else:
                left_weight = column_weight - current_thing['weight']
                adding_cell = table[i - 1][left_weight // step - 1] if i and left_weight else empty_cell
                possible_cost = current_thing['cost'] + adding_cell['cost']

                if possible_cost > max_cost_column_cell['cost']:
                    current_cell['cost'] = possible_cost
                    current_cell['things_list'] = [current_thing['name']] + adding_cell['things_list']

                    if current_cell['cost'] > max_cell['cost']:
                        max_cell = current_cell

                else:
                    current_cell['cost'] = max_cost_column_cell['cost']
                    current_cell['things_list'] = max_cost_column_cell['things_list']

    return max_cell['cost'], max_cell['things_list']


capacity = 6
data = (
    ('water', 10, 3),
    ('book', 3, 1),
    ('food', 9, 2),
    ('jacket', 5, 2),
    ('camera', 6, 1),
)

# capacity = 4
# data = (
#     ('recorder', 3000, 4),
#     ('laptop', 2000, 3),
#     ('guitar', 1500, 1),
# )

things = []
for thing in data:
    things.append(
        {
            'name': thing[0],
            'cost': thing[1],
            'weight': thing[2]
        }
    )

print(get_optimal_set(capacity, things))
