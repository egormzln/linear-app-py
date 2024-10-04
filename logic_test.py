from fractions import Fraction

from symplex_logic import SymplexLogic
from task_config import ExtremumType, SolutionType

symplex_logic_instance = SymplexLogic()

task_matrix = [
    [-1,-1,-1,-1],
    [1,0,3,4,5],
    [0,1,4,3,'9/2'],
    [0, 0, 0, 0]
]
task_extremum_type = ExtremumType.MIN
task_solution_type = SolutionType.MANUAL

task_matrix = [[Fraction(element) for element in row] for row in task_matrix]

symplex_result = symplex_logic_instance.solve_task(task_matrix, task_extremum_type, task_solution_type)

if symplex_result is not None:
    basis_output = [str(i) for i in symplex_result[1]]
    print(f'Ответ: \n*x = {basis_output} *f = {symplex_result[0]} ')


