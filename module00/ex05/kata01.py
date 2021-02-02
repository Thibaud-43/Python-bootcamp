def main():
    languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
    for k in languages.keys():
        print(k, "was created by", languages[k])

if __name__ == '__main__':
    main()
