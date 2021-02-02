def main():
    t = ( 0, 4, 132.42222, 10000, 12345.67)
    print("day_%.2d"%t[0], ", ex_%.2d"%t[1], " : %.2f"%t[2], ", ", "{:.2e}".format(t[3]), ", ", "{:.2e}".format(t[4]),sep="")
if __name__ == '__main__':
    main()
