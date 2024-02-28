#!/usr/bin/python3
"""matrix multiplication"""

def matrix_mul(m_a, m_b):
    """matrix multiplication"""
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both matrices must be lists of lists")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Both matrices must be lists of lists")

    if not m_a or not m_a[0] or not m_b or not m_b[0]:
        raise ValueError("Both matrices must be non-empty")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row) or \
       not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("Matrices must contain only numbers")

    if any(len(row) != len(m_a[0]) for row in m_a) or \
       any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("All rows in a matrix must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrices are not compatible for multiplication")

    # Matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(product)
        result.append(row)

    return result
