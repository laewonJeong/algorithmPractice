import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    sum_miles = 0

    while True:
        line = input().rstrip().split()
        if line[0] == '#':
            break
        elif line[0] == '0':
            print(sum_miles)
            sum_miles = 0
            continue
        else:
            c_codes = line[3]
            a_miles = int(line[2])

            if c_codes == 'Y':
                a_miles = max(500, a_miles)
            elif c_codes == 'B':
                a_miles += (a_miles + 1) // 2
            else:
                a_miles *= 2

            sum_miles += a_miles

if __name__ == "__main__":
    main()