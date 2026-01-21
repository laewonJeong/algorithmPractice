import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    weight = float(input())
    height = float(input())

    BMI = weight / (height * height)

    if BMI > 25.0:
        print('Overweight')
    elif BMI < 18.5:
        print('Underweight')
    else:
        print('Normal weight')

if __name__ == "__main__":
    main()