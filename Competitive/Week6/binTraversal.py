import sys

def test_traversal(path) :
    if len(path) <= 2 :
        return True
    if len(path) == 3 :
        if path[1] < path[0] :
            return path[2] > path[0]
        elif path[1] > path[0] :
            return path[2] > path[0]
    index = 1
    while(index < len(path) and path[index] < path[0]) :
        index += 1
    left = path[1:index]
    for item in left :
        if item > path[0] :
            return False
    right = path[index:len(path)]
    for item in right :
        if item < path[0] :
            return False
    return test_traversal(left) and test_traversal(right)

def main() :
    listy = []
    count = 1
    for line in sys.stdin:
        listy.extend(map(int, line.strip().split(" ")))
        if listy[len(listy)-1] < 0 :
            listy.pop()
            print("Case {}: {}".format(count,"yes" if test_traversal(listy) else "no"))
            count += 1
            listy = []

if __name__ == "__main__" :
    main()
