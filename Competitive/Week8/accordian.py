def cmprCard(c1, c2) :
    return c1[0] == c2[0] or c1[1] == c2[1]

def play(cards) :
    stacks = []
    while cards :
        stacks.append([cards.pop(0)])
        # print("\n stacks:")
        # for p in stacks :
        #     print p
        changed = True
        while changed :
            changed = False
            for i, sth in enumerate(stacks) :
                if i-3 >= 0 and cmprCard(sth[0],stacks[i-3][0]) :
                    stacks[i-3].insert(0, sth.pop(0))
                    changed = True
                elif i-1 >= 0 and cmprCard(sth[0],stacks[i-1][0]) :
                    # print("moved {} to pile {}".format(sth[0], ))
                    stacks[i-1].insert(0, sth.pop(0))
                    changed = True

                if sth == [] :
                    stacks.pop(i)
                if changed :
                    break
    return stacks

def main() :
    cards = []
    line = raw_input()
    while(line != "#") :
        cards.extend(line.strip().split())
        if len(cards) == 52 :
            stacks = play(cards)
            print("{} pile{} remaining: {}".format(len(stacks), "" if len(stacks) == 1 else "s", " ".join(map(str, map(len, stacks)))))
            cards = []
        line = raw_input()

if __name__ == "__main__" :
    main()
