def check(l):

    for i in l:
        if not i:
            return False
    return True

def main():
    n = int(raw_input())
    for i in range(n) :
        l = map(int, raw_input().split())
        print("Set #{}: {}".format(i+1, "Yes" if check(l) else "No"))

if __name__ =="__main__":
    main()
