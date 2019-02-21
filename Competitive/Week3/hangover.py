def main() :
    n = float(raw_input(""))
    while(n != 0) :
        i = 0.0
        cards = 1
        while i + (1.0/(cards+1)) < n :
            i += 1.0/(cards+1)
            cards += 1
        print("{} card(s)".format(cards))
        n = float(raw_input(""))

if __name__ == "__main__" :
    main()
