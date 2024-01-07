def unique(arr):
    numbers = []
    for num in arr:
        if num not in numbers:
            numbers.append(num)
    return numbers


n = input("Enter input:")
arr = list(map(int, n.split()))

numbers = unique(arr)

print(' '.join(map(str, numbers)))