input("A set eith n elements 2^n subsets. Press ENTER")
print("   3 elements 2^3=",2**3,"subsets")
print(" mask 5 = binary",bin(5)[2:],"select positions 0 and 2")

n=int(input("Enter the number of elements (try 4 or 5):"))
guess=input("How many subsets does a set of " + str(n)+" elements have?")
input(" Each element is in or out - 2 choices per element. Press ENTER")
print("",n," elements subsets: ", 2**n,"your guess:",guess)