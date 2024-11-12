def recursive_sum(my_list):
    if not my_list:
        return 0;
    else:
        return my_list[0] + recursive_sum(my_list[1:])


if __name__ == '__main__':
    num = [1, 2, 3, 4]
    result = recursive_sum(num)

    print("Sum of list =", result)