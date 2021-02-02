import sys

def main():
    if len(sys.argv) == 1:
        return
    sys.argv.reverse()
    for i in range(len(sys.argv) - 1):
        sys.argv[i] = sys.argv[i].swapcase()
        sys.argv[i] = sys.argv[i][::-1]
    print(*sys.argv[:-1], sep=" ")
if __name__ == '__main__':
    main()
