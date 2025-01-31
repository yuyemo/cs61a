def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    # 使用sorted()排序，并选择前两个最小值
    smallest_two = sorted([i, j, k])[:2]
    return smallest_two[0]**2 + smallest_two[1]**2

# 获取用户输入
x = int(input())
y = int(input())
z = int(input())

# 调用函数并输出结果
num = two_of_three(x, y, z)
print(f"{num}")
