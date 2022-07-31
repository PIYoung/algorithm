while True:
    A = input()

    if A == "0":
        break

    A = float(A)
    answer = "{:.2f}".format(1 + A + A**2 + A**3 + A**4)
    print(answer)