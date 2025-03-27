from copy import deepcopy, copy
CHOICES = []

for i, val in enumerate('ABCD'):
    remain = ['A', 'B', 'C', 'D']
    remain.remove(val)
    for _ in range(6): CHOICES.append([val])
    for j, v in enumerate(remain): 
        for k in range(2): 
            CHOICES[i * 6 + j * 2 + k].append(v)
        r = ''.join(remain)
        r = list(r)
        r.remove(v)
        CHOICES[i * 6 + j * 2].append(r[0])
        CHOICES[i * 6 + j * 2].append(r[1])
        CHOICES[i * 6 + j * 2 + 1].append(r[1])
        CHOICES[i * 6 + j * 2 + 1].append(r[0])


# OR just type them all out
ALT_CHOICES = [
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'D', 'C'],
    ['A', 'C', 'B', 'D'],
    ['A', 'C', 'D', 'B'],
    ['A', 'D', 'B', 'C'],
    ['A', 'D', 'C', 'B'],
    ['B', 'A', 'C', 'D'],
    ['B', 'A', 'D', 'C'],
    ['B', 'C', 'A', 'D'],
    ['B', 'C', 'D', 'A'],
    ['B', 'D', 'A', 'C'],
    ['B', 'D', 'C', 'A'],
    ['C', 'A', 'B', 'D'],
    ['C', 'A', 'D', 'B'],
    ['C', 'B', 'A', 'D'],
    ['C', 'B', 'D', 'A'],
    ['C', 'D', 'A', 'B'],
    ['C', 'D', 'B', 'A'],
    ['D', 'A', 'B', 'C'],
    ['D', 'A', 'C', 'B'],
    ['D', 'B', 'A', 'C'],
    ['D', 'B', 'C', 'A'],
    ['D', 'C', 'A', 'B'],
    ['D', 'C', 'B', 'A']
]

# TEST CASE
# VAL = '0   0   0   7   3   0   0   9   0   0   0   0   6   0   0   0   0   5   0   3   0   0   0   0'

CANDIADATES = ['A', 'B', 'C', 'D']
enter = input().split('   ')
votes = []

for i, v in enumerate(enter):
        if int(v) != 0:
            for _ in range(int(v)): votes.append(copy(CHOICES[i]))

while len(CANDIADATES) > 1: 
    vote_count = {c : 0 for c in CANDIADATES}
    for vote in votes:
        vote_count[vote[0]] += 1

    min_vote = [4324235234324324324, 'X']
    for count in vote_count.items():
        if count[1] < min_vote[0]:
            min_vote = [count[1], count[0]]
    
    CANDIADATES.remove(min_vote[1])
    vote_count.pop(min_vote[1])
    for vote_i in range(len(votes)):
        votes[vote_i].remove(min_vote[1])

print(CANDIADATES[0])
print(vote_count[CANDIADATES[0]])