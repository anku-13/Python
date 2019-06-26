def hungry_hippos():
    x = map(int, raw_input().split())
    num_hippos = x[0]
    height = x[1]
    ta = x[2]
    td = x[3]
    min_time = num_hippos * ta
    hippos = map(int, raw_input().split())
    hippos.sort(reverse=True)
    pair = []
    for i, h in enumerate(hippos):
        # print("{} - {}".format(h, hippos[-1]))
        if h < height and hippos[-1] + h < height and i != num_hippos-1:
            pair.append((h, hippos[-1]))
            hippos.pop()
            hippos.pop(0)
    # print hippos
    # print pair
    return len(hippos) * ta + len(pair) * td if (len(hippos) * ta + len(pair) * td) < min_time else min_time


def main() :
    tests = int(raw_input())
    for i in range(tests):
        print("Case {}: {}".format(i+1, hungry_hippos()))

if __name__ == "__main__" :
    main()
