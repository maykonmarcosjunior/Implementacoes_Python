from collections import deque

n = int(input())
stack = deque()
min_stack = deque()
output = []


def push(args):
    item = int(args[0])
    stack.append(item)
    if not min_stack or item <= min_stack[-1]:
        min_stack.append(item)


def pop(args):
    if stack:
        popped_item = stack.pop()
        if popped_item == min_stack[-1]:
            min_stack.pop()


def get_min(args):
    if min_stack:
        output.append(str(min_stack[-1]))
    else:
        output.append("EMPTY")


operations = {
    "PUSH": push,
    "POP": pop,
    "MIN": get_min,
}

for _ in range(n):
    operation, *args = input().split()
    operations[operation](args)

print("\n".join(output))
