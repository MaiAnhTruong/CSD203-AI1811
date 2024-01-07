def find_nearest_to_average(arr):
    average = sum(arr) / len(arr)

    nearest_value = arr[0]
    nearest_diff = abs(arr[0] - average)
    nearest_index = 0

    for i in range(1, len(arr)):
        diff = abs(arr[i] - average)
        if diff < nearest_diff:
            nearest_value = arr[i]
            nearest_diff = diff
            nearest_index = i

    return nearest_index


n = input("Enter input:")
arr = []
num = n.split(' ')
for i in num:
    arr.append(int(i))

nearest_index = find_nearest_to_average(arr)

print("The position of the element nearest to the average is:",nearest_index)