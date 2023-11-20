def d(n):
    arr = list(range(1, n + 1))
    arr2 = []
    for x in arr:
        k = x
        b = list(str(x))
        for i in b:
            k += int(i)
        if k in arr:
            arr2.append(k)
    set_arr2 = set(arr2)
    y = [_ for _ in arr if _ not in set_arr2]
    for _ in y:
        print(_)


d(10000)