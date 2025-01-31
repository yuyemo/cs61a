from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a + abs(b), but without calling abs."""
    if b < 0:
        f = add  # 对于负数b，实际做的是 a + (-b) = a + abs(b)
        b = -b   # 使 b 变为正数
    else:
        f = add  # 对于正数b，直接加上b
    return f(a, b)

# 获取用户输入
x = int(input("请输入a的值: "))
y = int(input("请输入b的值: "))

# 调用函数并输出结果
num = a_plus_abs_b(x, y)
print(f"结果是: {num}")
