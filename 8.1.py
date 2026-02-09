def add_one(some_list):
    s = ""
    for d in some_list:
        s += str(d)

    num = int(s) + 1

    result = []
    for ch in str(num):
        result.append(int(ch))

    return result