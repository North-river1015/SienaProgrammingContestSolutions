from copy import deepcopy


def find_val(b, n, target):

    pvals = []
    for sum in range(1, n+1):
        for x in range(sum + 1):
            pvals.append((x, sum-x))
    
    for combo in pvals:
        if combo[0] + combo[1] * b == target:
            return True
    return False



def find_best(SEARCH_SPACE):
    search = deepcopy(SEARCH_SPACE)
    target = 0
    while len(search) > 1:
        target += 1
        found = []
        for b in search:
            if (find_val(b, N, target)):
                found.append(b)
        if len(found) >= 1:
            search = found
        else:
            return search[0], target-1
    return search[0], target


if __name__ == '__main__':
    N = int(input('N: '))
    MAX_VAL = N ** 2 + 1

    best = find_best([i for i in range(1, MAX_VAL + 1)])
    print(f'MAX: {best[1]}')
    print(f'A: {1}, B: {best[0]}')

