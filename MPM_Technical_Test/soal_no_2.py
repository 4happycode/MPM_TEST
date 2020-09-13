# python_3

def wordBreak(dict, str, out=''):

    if not str:
        print(out)
        return

    for i in range(1, len(str) + 1):
        prefix = str[:i]
        if prefix in dict:
            wordBreak(dict, str[i:], out + " " + prefix)


if __name__ == '__main__':

    # List dictionary
    dict = [
        "pro", "gram", "merit", "program", "it", "programmer"
    ]

    # input String
    n = input("Your String: ")

    wordBreak(dict, n)