#documentos = [10, "10", "yotas", [4,5,6,7]]
nombre = "Juan Carlos"
docu = [10248185, "10", nombre, 1300000]
print(docu)
print(f"El numero de la cedula es: {docu[0]}")

docu.append("orange")
print(docu)

docu[1] = "A45"
print(docu)

# docu.clear()
# print(docu)

docu.copy()
print(docu)


x = docu.index("Juan Carlos")
print(x) 
docu[x] = "Maria"
print(docu)



"""
append()	Adds an element at the end of the list
clear()     Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()    Removes the item with the specified value
reverse()	Reverses the order of the list
sort()      Sorts the list
"""


