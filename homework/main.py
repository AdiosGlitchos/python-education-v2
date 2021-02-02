#defining list
list=[20,25,30,35,40,45]

#swapping second half with first half
temp=list[0:3]
list[0:3]=list[3:6]
list[3:6]=temp

#printing list
print([list])
