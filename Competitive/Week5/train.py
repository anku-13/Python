def bubble_trains() :
    swaps = 0
    l = int(raw_input(""))
    if l :
        trains = map(int, raw_input("").split(" "))
        changed = True
        while changed :
            changed = False
            for i in range(l-1) :
                if (trains[i] > trains[i+1]) :
                    temp = trains[i]
                    trains[i] = trains[i+1]
                    trains[i+1] = temp
                    swaps += 1
                    changed = True
    else :
        raw_input("")
    print("Optimal train swapping takes {} swaps.".format(swaps))

def main() :
    n = int(raw_input(""))
    for i in range(n) :
        bubble_trains()

if __name__ == "__main__" :
    main()
