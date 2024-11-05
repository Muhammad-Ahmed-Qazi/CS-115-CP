def countdown(n):
    if n == 0:
        return f'Blast off!'
    else:
        return f'{n}\n' + countdown(n - 1)

if __name__ == '__main__':
    time = int(input("Enter timer for countdown: "))
    print(countdown(time))