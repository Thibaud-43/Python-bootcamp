import string
import sys

def main():
   punctuation = string.punctuation
   if len(sys.argv) != 3:
       return
   sys.argv[1].replace(punctuation, "")
   phrase = sys.argv[1].split(" ")
   for word in phrase[:]:
       if len(word) < int(sys.argv[2]):
           phrase.remove(word)
   print(phrase)

if __name__ == '__main__':
    main();
