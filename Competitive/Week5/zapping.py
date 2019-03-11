def main() :
    n = map(int, raw_input("").split(" "))
    while n[0] != -1 and n[1] != -1 :
        if n[0] > n[1] :
            temp = n[0]
            n[0] = n[1]
            n[1] =  temp
        d1 = n[1] - n[0]
        d2 = n[0] + 100 - n[1]
        print (d1 if d1 < d2 else d2)
        n = map(int, raw_input("").split(" "))

if __name__ == "__main__" :
    main()
