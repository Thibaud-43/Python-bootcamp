import time
from sys import stdout

def ft_progress(listy):
    i = 0
    start = time.time()
    while i < len(listy):
        yield i
        i += 1
        egual = int(i/len(listy) * 23) * "="
        space = (23 - (int(i/len(listy) * 23))) * " "
        stdout.write("\rETA: {:6.2f}s [{:4.0%}][{}>{}] {:3} / {} | elapsed time {:.2f}s".format(((time.time() - start) / i) * (len(listy) - i),i / len(listy), egual, space, i, len(listy), time.time() - start))
        stdout.flush()

def main():
    listy = range(100)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.1)

if __name__ =='__main__':
    main()
