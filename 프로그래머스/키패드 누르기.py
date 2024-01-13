def solution(numbers, hand):
    answer = ''
    l = '*'
    r = '#'
    d = {1: (0, 0), 2: (0, 1), 3: (0, 2),
         4: (1, 0), 5: (1, 1), 6: (1, 2),
         7: (2, 0), 8: (2, 1), 9: (2, 2),
         '*': (3, 0), 0: (3, 1), '#': (3, 2),
         }

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l = i
        elif i in [3, 6, 9]:
            answer += 'R'
            r = i
        elif i in [2, 5, 8, 0]:
            left = abs(d[i][0] - d[l][0]) + abs(d[i][1] - d[l][1])
            right = abs(d[i][0] - d[r][0]) + abs(d[i][1] - d[r][1])
            if left == right:
                if hand == 'right':
                    r = i
                    answer += 'R'
                elif hand == 'left':
                    l = i
                    answer += 'L'
            elif left > right:
                r = i
                answer += 'R'
            elif left < right:
                l = i
                answer += 'L'
    return answer