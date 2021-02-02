import sys

def do_sum(nb1, nb2):
    print("Sum : \t\t", int(nb1) + int(nb2))

def do_difference(nb1, nb2):
    print("Difference : \t", int(nb1) - int(nb2))
    
def do_quotient(nb1, nb2):
    if nb2 == 0:
        str = "ERROR (div by zero)"
    else:
        str = int(nb1) / int(nb2)
    print("Quotient : \t", str)

def do_reminder(nb1, nb2):
    if nb2 == 0:
        str = "ERROR (modulo by zero)"
    else:
        str = int(nb1) % int(nb2)
    print("Reminder : \t", str, "\n")

def print_usage():
    print("\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")

def check_number(nb):
    try:
        int(nb)
    except ValueError:
        print("InputError : only numbers")
        print_usage()
        sys.exit()
    return nb

def operations():
    if len(sys.argv) > 3:
        print("InputError : too many arguments")
        print_usage()
        return

    if len(sys.argv) == 2:
        print("InputError : not enought arguments")
        print_usage()
        return

    if len(sys.argv) == 1:
        print_usage()
        return

    nb1 = check_number(sys.argv[1])
    nb2 = check_number(sys.argv[2])
    do_sum(nb1, nb2)
    do_difference(nb1, nb2)
    do_quotient(nb1, nb2)
    do_reminder(nb1, nb2)

if __name__ == '__main__':
    operations()
