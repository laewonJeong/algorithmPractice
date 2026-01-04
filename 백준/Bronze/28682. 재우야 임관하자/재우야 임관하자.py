import sys

input = sys.stdin.readline

lectures = ["swimming", "bowling", "soccer"]

n = int(input().strip())

print(" ".join(["swimming"] * n))
sys.stdout.flush()

fails = input().split()

result = []
for f in fails:
    for lec in lectures:
        if lec != "swimming" and lec != f:
            result.append(lec)
            break

print(" ".join(result))
sys.stdout.flush()
