def find_phone_plan() :
    raw_input("")
    calls =  map(int, raw_input("").split(" "))
    mp = 0
    jp = 0
    for c in calls:
        mp += (c/30) * 10 + 10
        jp += (c/60) *15 + 15
    if mp == jp :
        return "Mile Juice {}".format(mp)
    elif mp < jp :
        return "Mile {}".format(mp)
    else :
        return "Juice {}".format(jp)

def main() :
    tests = int(raw_input(""))
    for i in range(tests) :
        print("Case {}: {}".format(i+1,find_phone_plan()))

if __name__ == "__main__" :
    main()
