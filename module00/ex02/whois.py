import sys

def check(str):
    if int(str) == 0:
        return "I'm Zero"
    if int(str)%2 == 0:
        return "I'm Even"
    if int(str)%2 != 0:
        return "I'm Odd"

def main():
    if len(sys.argv) != 2:
        print("ERROR")
        return
    str = sys.argv[1].replace('-', '')
    if str.isdigit():
        print(check(str))
    else :
        print("ERROR")

if __name__ == '__main__':
    main()
