# I only do tests here

a = [1, 2, 3, 4, 5, 6]
b = [2, 2, 3, 4, 5, 7]

print([x - y for x, y in zip(a, b)])
