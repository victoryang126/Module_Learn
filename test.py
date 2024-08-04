def check_in_range_detailed(list_a, list_b):
    n = len(list_a)

    # 确保列表A和B有相同的长度
    if n != len(list_b):
        return False,"length is not equal"

    # 结果字典
    result = []
    ranges_checked = []
    for i in range(n):
        a_val = list_a[i]

        in_range = False

        # 检查当前元素是否在
        if i < len(list_b):
            current_low, current_high = list_b[i]
            in_current_range = current_low <= a_val <= current_high
            ranges_checked.append(f'check actual {a_val } at index {i} in current low and current high ({current_low}:{current_high})->Result:{in_current_range}')
            if in_current_range:
                in_range = True
                result.append(in_range)
                continue

        # 检查前一个元素的范围（如果存在）
        if i > 0:
            previous_low, previous_high = list_b[i - 1]
            in_prev_range = previous_low <= a_val <= current_high
            ranges_checked.append(f'check actual {a_val } at index {i} in previous low and current high ({previous_low}:{current_high})->Result:{in_prev_range}')
            if in_prev_range:
                in_range = True
                result.append(in_range)
                continue

        # 检查下一个元素的范围（如果存在）
        if i < n - 1:
            next_low, next_high = list_b[i + 1]
            in_next_range = current_low <= a_val <= next_high
            ranges_checked.append(f'check actual {a_val } at index {i} in previous low and current high ({current_low}:{next_high})->Result: {in_next_range}')
            if in_next_range:
                in_range = True
        result.append(in_range)



    return all(result),ranges_checked

# 示例数据
list_a = [ 1, 11, 23, 36]
list_b = [(0.9, 1.4), (11.1, 12.3), (22, 24), (35, 37)]

# 调用函数并输出结果
result,ranges_checked = check_in_range_detailed(list_a, list_b)
for range_check in ranges_checked:
    print(range_check)
