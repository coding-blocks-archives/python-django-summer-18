import sys

ans = 0

for arg in sys.argv[1:]:
	ans += int(arg)

print("Sum is:", ans)