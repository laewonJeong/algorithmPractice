def java(var):
    if var[0] == '_' or var[-1] == '_' or '__' in var:
        return 'Error!'
    result = ''

    for i in range(len(var)):
        if ord(var[i]) >= 65 and ord(var[i]) < 95 and var[i] != '_':
            return 'Error!'
        if var[i] == '_':
            continue
        if var[i-1] == '_':
            result += var[i].upper()
        else:
            result += var[i]
    return result

def cpp(var):
    if ord(var[0]) >=65 and ord(var[0]) <=93:
        return 'Error!'
    result =''
    for i in var:
        if ord(i)>=65 and ord(i) <93:
            result += '_' + i.lower()
        else:
            result += i
    return result

var = input()
if '_' in var:
    print(java(var))
else:
    print(cpp(var))