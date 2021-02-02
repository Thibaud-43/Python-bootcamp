def main():
    phrase = "the right format"
    str = (42 - len(phrase) - 1) * "-" + phrase
    print(str)
if __name__ == '__main__':
    main()
