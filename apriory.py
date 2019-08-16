import itertools

stuff = [1, 2, 3]


def get_array(stuff, l):
    ans = []
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            if len(subset) == l:
                ans.append(list(subset))
    return ans


def get_score(test, all_data):
    score = 0
    for data in all_data:
        t = 0
        for el in test:
            if el in data:
                t += 1
        if t == len(test):
        # if test in data:
           score += 1

    return score


data = [
    [0, 1, 2, 5, 7, 9],
    [1, 2, 7, 8],
    [0, 5, 6, 8, 9],
    [1,2,4,5,7],
    [0,1,2,5,9],
    [0,1,2,9],
    [0,3,4,5,8,9],
    [1,2,3,4,7,8],
    [5,6,7],
    [0,5,6,8,9],
]

minsup = 3


for k in range(1, 6):
    print 'K = ', k
    print '*' * 30
    combinations = get_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k)
    for c in combinations:
        score = get_score(c, data)
        if score >= minsup:
            print c, '   ', get_score(c, data)
