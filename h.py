for i in range(2,0,-1) :
    x = "".join([" "]*i + ["X"]*(5-(i+i)) + [" "]*i)
    print(x+x)
for i in range(3) :
    print("".join(["X"]*10))
for i in range(1,5) :
    x = "".join([" "]*i + ["X"]*(5-i))
    print (x + x[::-1])