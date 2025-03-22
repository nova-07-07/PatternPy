n = 15

# Upper part of the butterfly
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower part of the butterfly
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
