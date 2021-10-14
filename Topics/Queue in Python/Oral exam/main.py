from collections import deque

ENQUEUE = 'READY'
DEQUEUE = 'PASSED'
EXTRA = 'EXTRA'

queue = deque()
students = []

for _ in range(int(input().strip())):
    operands = input().strip().split()

    if operands[0] == DEQUEUE:
        students.append(queue.pop())
        continue

    if operands[0] == ENQUEUE:
        queue.appendleft(operands[1])
        continue

    if operands[0] == EXTRA:
        queue.appendleft(queue.pop())

for person in students:
    print(person)
