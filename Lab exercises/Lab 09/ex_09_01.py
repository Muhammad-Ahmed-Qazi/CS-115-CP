def fibonacci(prev, curr, lim):
    if (prev + curr) >= lim:
        return f'{curr}'
    else:
        if prev != 0:
            result = f'{curr}, {fibonacci(curr, (prev + curr), lim)}'
        else:
            result = f'0, {curr}, {fibonacci(curr, (prev + curr), lim)}'

        return result

if __name__ == '__main__':
    limit = int(input("Enter limit for the Fibonacci series: "))

    print("Fibonacci:", fibonacci(0, 1, limit))