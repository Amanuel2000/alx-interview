#!/usr/bin/python3
"""determining pascal's triangle"""


def pascal_triangle(m):
    """
    returns list of Pascal’s triangle of m
    """
    triangle = []

    # return (trianlgle if m <= 0)
    if m <= 0:
        return triangle
    for h in range(m):
        temp_list = []

        for i in range(h+1):
            if i == 0 or i == h:
                temp_list.append(1)
            else:
                temp_list.append(triangle[h-1][i-1] + triangle[h-1][i])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
