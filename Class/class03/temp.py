# read in temperature f to c
# <= -20 print cold
# else print c

temp = raw_input("Enter temperature: ")
print( "brr cold" if float(temp) <= -20 else ((float(temp) - 32) * (5/9))) 
# temp = float(temp)
# if(temp <= -20) :
#     print("brr cold!")
# else :
#     print((temp - 32) * (5/9))
