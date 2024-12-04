def get_bounds(n):
    min_number = int("1" + "0" * (n - 1))
    return min_number


def get_list(n):
    num_list = []
    while n != 0:
        digit = n % 10
        num_list.append(digit)
        n //= 10
    return num_list


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def reverse_list(arr):
    return arr[::-1]


def get_number_from_list(arr):
    num = 0
    for digit in arr:
        num = num * 10 + digit
    return num


def kaprekar_Constant(digits):
    min_limit = get_bounds(digits)
    max_limit = min_limit * 10

    for i in range(min_limit, max_limit):
        num_list = get_list(i)
        count = 0
        while True:
            min_number = get_number_from_list(quicksort(num_list))
            max_number = get_number_from_list(reverse_list(quicksort(num_list)))

            diff = max_number - min_number
            if diff == 0:
                break  # If all digits are the same, stop the loop.

            count += 1
            num_list = get_list(diff)

            # If we reach 6174, stop the process
            if diff == 6174:
                break

        if count > 0:
            print(f"Number {i} reached 6174 in {count} steps")


def main():
    digits = int(input("Enter the number of digits: "))
    kaprekar_Constant(digits)


if __name__ == "__main__":
    main()
