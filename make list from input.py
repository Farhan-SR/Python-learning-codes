#10 20 30 40 50


n =input("enter some numbers : ")
list = n.split()  #10,20,30,40
sum = 0
for num in list :
    sum = sum + int(num)

print(sum)