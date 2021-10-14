from collections import deque

ENQUEUE = 'ISSUE'
DEQUEUE = 'SOLVED'

queue = deque()

for _ in range(int(input().strip())):
    operands = input().strip().split()

    if operands[0] == DEQUEUE:
        queue.pop()
        continue

    if operands[0] == ENQUEUE:
        queue.appendleft(operands[1])

while queue:
    print(queue.pop())
