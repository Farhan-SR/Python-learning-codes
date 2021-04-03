subjects = ["C","C++" , "Java" , "Pyhton", "Basic"]
print(subjects)
print(len(subjects)) #len = lenght of list

subjects.append("Toc")
print(subjects) #append = add to the list permanetly

subjects.insert(2, "OS")
print(subjects) #insert = index num+ sub num , other will be shift right side

subjects.remove("Basic")
print(subjects)  #remove = to remove any data of list

subjects.sort()
print(subjects)  #sort = organige the serial by dictionary and for number 0-1-2 incresing

nx2 = [20 ,10,75,85, 20,30,40,50,80]
nx2.sort()
print(nx2)

"""subjects.reverse()
nx2.reverse()  #reverse = ordering from right to left & for number big to small
print(subjects)
print(nx2)"""


subjects.pop()  #to remove last data of list / can use multi time
nx2.pop()
print(subjects)
print(nx2)


"""
subjects.clear()
nx2.clear()  #cler- will cler all the deta of the list 
print(subjects)
print(nx2)"""

subjects2 = subjects.copy()
print(subjects2)  #copy - to copy all the list data to another veriable

nx23 = nx2.copy()
print(nx23)



pos =  nx2.index(40)
print(pos)  # to see the position of a data on list

test = [20 , 40 , 20 , 20 ,20 , 30 ]
print(test)
cont = test.count(20)  # to count how many same number there
print(cont)







