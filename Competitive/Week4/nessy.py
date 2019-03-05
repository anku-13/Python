def main() :
    n = int(raw_input(""))
    for i in range(n) :
        nm = map(int, raw_input("").split(" "))
        n, m = nm[0], nm[1]
        # print("n m     = {} {}".format(n,m))
        # print("n/3 m/3 = {} {}".format(n/3, m/3))
        # print("n%3 m%3 = {} {}".format(n%3, m%3))
        print((n/3) * (m/3))

if __name__ == "__main__" :
    main()
