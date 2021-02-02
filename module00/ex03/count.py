import sys
import string

def analyze(text):
    if not text:
        print("String is empty")
        return
    ponctuations_characters = string.punctuation
    space = text.count(" ")
    lower = 0
    upper = 0
    ponctuation = 0
    for i in range(len(text)):
        if text[i].islower():
           lower += 1
        if text[i].isupper():
            upper += 1
        if text[i] in ponctuations_characters:
            ponctuation += 1
    print('The text contains', i + 1, 'characters:\n- ', upper,' upper letters\n- ', lower ,' lower letters\n- ', ponctuation,' punctuation marks\n- ', space,' spaces')
    

def text_analyzer(*args):
    if len(args) == 0:
        text = input("What is the text to analyze ? \n")
        analyze(str(text))
    elif len(args) == 1:
        text = args[0]
        analyze(str(text))
    else :
        print("Error")

if __name__ == "__main__":
    main()
