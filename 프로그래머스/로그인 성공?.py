def solution(id_pw, db):
    answer = ''
    dc = {}
    for a, b in db:
        dc[a] = b
    if id_pw[0] in dc:
        if dc[id_pw[0]] == id_pw[1]:
            answer = "login"
        else:
            answer = "wrong pw"
    else:
        answer = "fail"

    return answer