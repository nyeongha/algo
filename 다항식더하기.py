def solution(polynomial):
    arr = [0, 0]
    res = []
    for x in polynomial.split(" + "):
        if x.endswith("x"):
            arr[0] += int(x[:-1] or "1")
        else:
            arr[1] += int(x)


    if arr[0] == 1:
      res.append(f"x")
    elif arr[0] != 0:
      res.append(f"{arr[0]}x")
    if arr[1] != 0:
      res.append(f"{arr[1]}")

    return " + ".join(res)