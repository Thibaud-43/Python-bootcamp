import sys

morse_dic = {
        'a' : '.-',
        'b' : '-...',
        'c' : '-.-.',
        'd' : ' -..',
        'e' : '.',
        'f' : '..-.' ,
        'g' : '--.' ,
        'h' : '....' ,
        'i' : '..' ,
        'j' : '.---' ,
        'k' :  '-.-' ,
        'l' : '.-..' ,
        'm' :  '--' ,
        'n' :  '-.' ,
        'o' : '---' ,
        'p' :  '.--.' ,
        'q' : '--.-' ,
        'r' :  '.-.' ,
        's' :  '...' ,
        't' :  '-' ,
        'u' :  '..-' ,
        'v' :  '...-' ,
        'w' :  '.--' ,
        'x' :  '-..-' ,
        'y' :  '-.--' ,
        'z' :  '--..' ,
        '0' :  '-----' ,
        '1' :  '.----' ,
        '2' :  '..---' ,
        '3' : '...--' ,
        '4' : '....-' ,
        '5' : '.....' ,
        '6' :  '-....' ,
        '7' : '--...' ,
        '8' : '---..' ,
        '9' : '----.',
                }

def morse(string):
    for character in string:
        print(morse_dic[character], end =" ")

def main():
    list = []
    for i in range(len(sys.argv)):
         list.append(sys.argv[i].lower())
    list.remove("sos.py")
    for string in list:
        if not string.isalnum():
            print("ERROR")
            return
    for i in range(len(list)):
        morse(list[i])
        if not i == len(list) - 1:
            print("  /  ", end = "")
        else :
            print()

if __name__ == '__main__':
    main()
