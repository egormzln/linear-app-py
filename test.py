from fractions import Fraction

from symplex_logic import SymplexLogic
from task_config import ExtremumType

symplex_logic_instance = SymplexLogic()

# № 3.10
#     [1, 3, 2, 4, -2],
#     [-1, 0,  1, -2, -2, -2],
#     [0,  1, -1,  1, -2,  0],
#     [2,  1,  0,  5,  1,  7],
#     [1, 1, 1, 0, 0]



# # № 3.7
# [-1, -1, -1, -1],
# [1, 3, 1, 2, 5],
# [2, 0, -1, 1, 1],
# [0, 0, 1, 1]

# # Задача из объясения симплекс-метода
# [-2, -1, -3, -1],
# [1,  2,  5,-1, 4],
# [1, -1, -1, 2, 1],
# [0,0,1,1]

task_matrix = [
# № 3.12 у Ратушина
    [3, -2, 1, 3, 3],
    [2, -1, 1, 1, 1, 2],
    [-4, 3, -1, -1, -3, -4],
    [3, 2, 3, 5, 0, 3],
    [0, 1, 1, 1, 0]
]

task_extremum_type = ExtremumType.MIN

task_matrix = [[Fraction(element) for element in row] for row in task_matrix]

input_matrix = []
input_target_columns = []

for i in range(len(task_matrix[-1])):
    if task_matrix[-1][i] == Fraction(1):
        input_target_columns.append(i)

for task_row in range(1, len(task_matrix)-1):
    new_row = []
    for item in task_matrix[task_row]:
        new_row.append(item)
    input_matrix.append(new_row)

print('Задача:')
for i in input_matrix:
    for j in i:
        print(str(j), end=' ')
    print()

print()
print('Индексы базисных переменных:')
print(*input_target_columns)

print()
print('Ответ:')
gauss_result = symplex_logic_instance.gauss_method(input_matrix, input_target_columns)
for i in gauss_result:
    for j in i:
        print(str(j), end=' ')
    print()
print()

reduced_function = symplex_logic_instance.reduced_function(task_matrix[0], gauss_result, task_matrix[-1], task_extremum_type)
print('Упрощённая функция:')
print(*[str(i) for i in reduced_function])
print()

initial_symplex_table = symplex_logic_instance.get_initial_symplex_table(reduced_function, gauss_result, task_matrix[-1], task_extremum_type)
print('Начальная симплекс-таблица:')
for _ in initial_symplex_table:
    for __ in _:
        print(__, end=' ')
    print()
print()

symplex_result = symplex_logic_instance.solve_task(initial_symplex_table, task_extremum_type)





