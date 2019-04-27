def main():
    n = int(raw_input())
    while n:
        rows = [0]*n
        cols = map(int, raw_input().split())
        rows[0] = sum(cols)
        for i in range(1,n):
            line = map(int, raw_input().split())
            rows[i] = sum(line)
            for j,x in enumerate(line):
                cols[j] += x
        oddCols = [i+1 for i in range(len(cols)) if cols[i]%2 != 0]
        oddRows = [i+1 for i in range(len(rows)) if rows[i]%2 != 0]
        # print("{} , {}".format(oddCols, oddRows))
        if not oddCols and not oddRows:
            print("OK")
        elif len(oddCols) == 1 and len(oddRows) == 1:
            print("Change bit ({},{})".format(oddRows[0], oddCols[0] ))
        else:
            print("Corrupt")
        n = int(raw_input())

if __name__ == "__main__":
    main()
