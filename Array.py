import array as arr
a=arr.array("i",[1,3,4,5,9,3,0,2,3,5])
print("This is the original array",a)
print(a.count(3))
a.reverse()
print("The reverse order of the original array is",a)