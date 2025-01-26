test_case = int(input())
MAX = 1000000
for _ in range(test_case):
    sc = int(input())
    student_id = []
    for i in range(sc):
        s_id = int(input())
        student_id.append(s_id)
    for i in range(1,MAX):
        arr = []
        for j in student_id:
            a = j%i
            arr.append(a)
        arr = list(set(arr)) 
        if len(arr) == sc:
            result = i
            break
    print(result)