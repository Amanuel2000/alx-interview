#!/usr/bin/python3

def pascal_triangle(m):
    """
    returns a list of lists of integers representing the Pascal’s triangle of m
    """
    triangle = []

    # return (trianlgle if m <= 0)
    if m <= 0:
        return triangle
    for j in range(m):
        temp_list = []

        for k in range(j+1):
            if k == 0 or k == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[j-1][k-1] + triangle[j-1][k])
        triangle.append(temp_list)
    # print(triangle)
    return 