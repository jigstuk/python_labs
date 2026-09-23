n = int(input())
truee = 0
falsee = 0
for i in range(n):
    line = input(f'in_{i+1}: ').strip()
    parts = line.split()
    if parts[-1] == 'True':
        truee += 1
    else:
        falsee += 1
print(truee, falsee)