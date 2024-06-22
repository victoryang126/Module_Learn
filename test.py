def compare_lists(actual, expect):
    detailed_info = []
    all_true = True

    for i in range(len(actual)):
        # 当前元素的索引
        actual_elem = actual[i]

        # 获取expect中前一个、当前、后一个元素
        expect_prev = expect[i - 1] if i > 0 else None
        expect_curr = expect[i]
        expect_next = expect[i + 1] if i < len(expect) - 1 else None

        # 比较逻辑
        if actual_elem == expect_prev or actual_elem == expect_curr or actual_elem == expect_next:
            result = True
        else:
            result = False
            all_true = False

        # 添加详细信息
        detailed_info.append({
            "index": i,
            "actual": actual_elem,
            "expect_prev": expect_prev,
            "expect_curr": expect_curr,
            "expect_next": expect_next,
            "result": result
        })

    if all_true:
        return True,None
    else:
        return False, detailed_info

# 示例
actual = [1, 2, 3, 4, 5]
expect = [0, 2, 3, 1, 5]
result = compare_lists(actual, expect)

if result is True:
    print("All comparisons are True.")
else:
    print("Not all comparisons are True.")
    for info in result[1]:
        print(f"Index {info['index']}: actual = {info['actual']}, "
              f"expect_prev = {info['expect_prev']}, expect_curr = {info['expect_curr']}, "
              f"expect_next = {info['expect_next']}, result = {info['result']}")
