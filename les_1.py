a = input()
b = len(a) // 2


c = a[:b]
d = ''.join(reversed(a[b:]))

if c == d:
    print('True')
else:
    print('False')