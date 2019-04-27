def eval(ss) :
    stack  = []
    for t in ss :
        if t == "(" or t == "[":
            stack.insert(0,t)
        else:
            if stack == [] :
                return False
            elif t == ")" :
                pre = stack.pop(0)
                if pre != "(" :
                    return False
            elif t == "]" :
                pre = stack.pop(0)
                if pre != "[" :
                    return False
    return stack == []

def main() :
    n = int(raw_input())
    for i in range(n):
        print("Yes" if eval(raw_input()) else "No")

if __name__ == "__main__" :
    main()
