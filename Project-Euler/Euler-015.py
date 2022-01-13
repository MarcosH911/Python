from math import factorial


def lattice_paths(grid_number):
    return (factorial(grid_number * 2)) / ((factorial(grid_number)) ** 2)


print(lattice_paths(20))
