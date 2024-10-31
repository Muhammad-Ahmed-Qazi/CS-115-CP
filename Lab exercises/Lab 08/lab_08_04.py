def power(base, exponent = 2):
    return base ** exponent

if __name__ == "__main__":
    base = int(input("Enter the base: "))
    print(f"{base}^2 =", power(base))
    exponent = int(input("Enter the exponent: "))
    print(f"{base}^{exponent} =", power(base, exponent))