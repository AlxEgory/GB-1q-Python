# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        mat_str = ['-'.join(str(el) for el in row) for row in self.matrix]
        mat_str = '|\n|'.join(mat_str)
        mat_str = f'|{mat_str}|'
        return mat_str

    def __add__(self, other):
        matrix_sum = [
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.matrix, other.matrix)
        ]
        return Matrix(matrix_sum)


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[31, 22], [37, 43], [51, 86]])

print(matrix1+matrix2)

