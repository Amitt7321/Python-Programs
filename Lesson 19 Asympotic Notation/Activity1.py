n=10
guess=input("Double Loop at n=10 chack n x n pairs.How many? ")
input("Formula: on calculation, done. Press ENTER to run")
steps=1
print("steps=",steps," -> 0(1) constant time -> steps never change")

input("Loop:one step per item. Press ENTER to run")
steps=0
for i in range(n):
    steps+=1
    print("steps=",steps," -> 0(1) linear  time -> steps grow with n")
    input("Double Loop: chacks every pair. Press ENTER to run")
    steps=0
    for i in range(n):
        for j in range(n):
            steps+=1
print(" steps=",steps, "your guess:",guess," ->0(n^2) quadratic time")

input("Two more notations. Press ENTER")
print(" Big Omega Ω -> best case lower bound")
print(" Big Theta Θ -> exact bound (worst = best)")