def change_name(name):
    dic = {'i': 'e', 'e': 'i', 'I': 'E', 'E': 'I'}
    res = ''

    for c in name:
        if c in dic:
            res += dic[c]
        else:
            res += c

    return res

if __name__ == "__main__":
    while 1:
        try:
            name = input()
            print(change_name(name))
        except EOFError:
            break