n = int(input())
list1 = {}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def getValue(name):
    v = list1.get(name)
    return v


result = ""
for i in range(n):
    s_current = input().replace(" ", "")
    left, right = s_current.split("=")[0], s_current.split("=")[1]
    rightValues = right.split("+")
    if getValue(left) is None:
        list1[left] = 0
    for rightValue in rightValues:
        if is_number(rightValue) is False:
            if getValue(rightValue) is None:
                print("NA")
                exit(0)
    rightsum = 0
    for rightValue in rightValues:
        if is_number(rightValue) is False:
            rightsum += getValue(rightValue)
            # print(rightsum)
        else:
            rightsum += int(rightValue)
    list1[left] = rightsum
    if i == n - 1:
        result = rightsum

print(result)
