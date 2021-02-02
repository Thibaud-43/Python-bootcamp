import string
import sys

def main():
   punctuation = string.punctuation
   if len(sys.argv) != 3:
       return
   sys.argv[1].replace(punctuation, "")
   phrase = sys.argv[1].split(" ")
   print()
   for item in phrase:
       if (len(item) < int(sys.argv[2])):
           phrase.remove(item)
   print(phrase)

if __name__ == '__main__':
    main();
