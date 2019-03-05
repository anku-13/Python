def main() :
    con = map(int, raw_input("").split(" "))
    while con[0] != 0 and con[1] != 0 and con[2] != 0 :
        grid = []
        for i in range(con[0]) :
            grid.append(list(raw_input("")))
        rx, ry = 0, con[2]-1
        count = 0
        loop = False
        while(rx >= 0 and ry >= 0 and rx < con[0] and ry < con[1] and not loop) :
            # print("x {} y {}".format(rx,ry))
            action = grid[rx][ry]
            grid[rx][ry] = str(count)
            if action == "N" :
                rx -= 1
            elif action == "S" :
                rx += 1
            elif action == "W" :
                ry -= 1
            elif action =="E" :
                ry += 1
            else :
                loop = True
                print("{} step(s) before a loop of {} step(s)".format(action, count-int(action)))
            count += 1

        if not loop :
            print("{} step(s) to exit".format(count))
        con = map(int, raw_input("").split(" "))

if __name__ == "__main__" :
    main()
