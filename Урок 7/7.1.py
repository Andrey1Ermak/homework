class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(*x)] for x in zip(self.matrix, other.matrix)])

        # def sum_of_matrix():
        #     for el in zip(self.matrix, other.matrix):
        #         yield ''.join(f'{int(el[0][0]) + int(el[1][0])}\t'
        #                       f'{int(el[0][1]) + int(el[1][1])}')
        #
        # for i in sum_of_matrix():
        #     print(i)

    def __str__(self):
        return '\n'.join([''.join([f'{i}\t' for i in row]) for row in self.matrix])


matrix_1 = Matrix([[2, 4, 3], [3, 6], [4, 5], [9, 9]])
matrix_2 = Matrix([[1, 5, 1], [1, 4], [5, 3], [10, 12]])

print(matrix_1)
print()
print(matrix_1 + matrix_2)
