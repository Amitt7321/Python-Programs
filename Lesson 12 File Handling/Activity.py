file = open("bucket-list.txt","w")
file.write("1. Visit Statue of Liberty/n")
file.write("2. Paraglyding/n")
file.write("3. Develop a new electronic device/n")
file.close
print("Bucket list saved to bucket-list.txt!/n")

file = open("bucket-list.txt", "r")
content = file.read()
print("/n=== My Bucket List===")
print(content)
file.close

file = open("bucket-list.txt", "r")
lines=file.readlines()
print(f"You have{len(lines)}items on your bucket list.")
file.close()

file = open("bucket-list.txt", "a")
file.write("4. Travel Japan/n")
file.write("5. Meat with Mr. Beast/n")
file.close()
print("/n2 more items added!")

file = open("bucket-list.txt", "r")
print("/n=== Updated Bucket List===")
print(file.read())
file.close()