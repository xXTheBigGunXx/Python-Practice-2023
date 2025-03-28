print ("CALCULATOR")
input_one = float(input())
input_sign = input()
if input_sign == "+":
    input_second = float(input())
    print (input_one + input_second)
elif input_sign == "-":
    input_second = float(input())
    print (input_one - input_second)
elif input_sign == "/":
    input_second = float(input())
    print (input_one / input_second)
elif input_sign == "*":
    input_second = float(input())
    print (input_one * input_second)
elif input_sign == "**2":
    print (input_one **2 )
elif input_sign == "**0.5":
    print (input_one **0.5 )
elif input_sign == "**":
    input_second = float(input())
    print (input_one ** input_second )
