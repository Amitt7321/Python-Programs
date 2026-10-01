input("Binary exponantiation uses bit of the exponent. Press ENTER")
print("2^8= exponent 8 = binary",bin(8)[2:])
print("2^8= exponent 5 = binary",bin(5)[2:])

exp = int(input("Enter exponent(try 3 or 6):"))
print("exponent", exp,"=binary",bin(exp)[2:])
guess=input("What is 2^"+ str(exp)+"?")
input("Binary exponatiation reads bit s of exponent. Prss ENTER")
print("2^",exp,"=",2**exp,"your guess:",guess)