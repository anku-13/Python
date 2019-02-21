def main() :
    run_count = 1
    shelf_width = int(raw_input(""))
    while shelf_width > 0 :
        shelf = []
        filled = 0
        line = raw_input("")
        while "E" not in line :
            line = line.split()
            if line[0] == "A" :
                shelf.append([line[1],line[2]])
                filled += int(line[2])
                while filled > shelf_width :
                    book = shelf.pop(0)
                    filled -= int(book[1])
            elif line[0] == "R" :
                for book in shelf :
                    if book[0] == line[1] :
                        filled -= int(book[1])
                        shelf.remove(book)
            line = raw_input("")
        shelf.reverse()
        print("Problem {}: {}".format(run_count, " ".join([book[0] for book in shelf])))
        run_count += 1
        shelf_width = int(raw_input(""))

if __name__ == "__main__" :
    main()
