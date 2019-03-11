def main() :
    n = map(int, raw_input("").split(" "))
    while n[0] != 0 and n[1] != 0 :
        prod = n[0] * n[1]
        if prod == n[0] or prod == n[1]:
            prod += 1
        print ("({} x {}): {}".format(n[0],n[1], prod - n[0] if n[0] > n[1] else prod - n[1]))
        n = map(int, raw_input("").split(" "))

if __name__ == "__main__" :
    main()
