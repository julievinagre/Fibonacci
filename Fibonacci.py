n_terms = input("How many Fibonacci terms? ")

while not n_terms.isdecimal():
    print("Not a valid number, try again!")
    n_terms = input("How many terms? ")
else:
    n_terms = int(n_terms)

    n1, n2 = 0, 1
    count = 0

    if (n_terms <= 0):
        print("Enter a positive integer")
    elif (n_terms == 1):
        print(f"Fibonacci sequence up to {n_terms}:")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < n_terms:
            print(n1)
            n_th = n1 + n2

            n1 = n2
            n2 = n_th
            count += 1
