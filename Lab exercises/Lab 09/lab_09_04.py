def reversal(string):
    if string == '':
        return ''
    else:
        return string[-1] + reversal(string[:-1])

if __name__ == '__main__':
    string = input("Enter a string you want to reverse: ")

    print("Reversed string:", reversal(string))