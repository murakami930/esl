from sys import stdin
# Your code here!
A, B, C = [int(x) for x in stdin.readline().rstrip().split()]

for i in range( 6 ):
    i += 1
    if A*i >= C:
        break
    else:
        i = A*i+B

print(i)
