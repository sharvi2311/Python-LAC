#CREATE LIST
thislist = ["Banana","Cherry","Apple","Mango","Pineapple"]
print("List items are", thislist)

#LENGTH OF LIST
print("The length of the list is", len(thislist))

#TYPE OF THE LIST
print("The type of itmes in the list are", type(thislist))

#ACCESSING THE ELEMENTS OF THE LIST
print("The secomd element of the list is", thislist[1])

#NEGETIVE INDEXING
print("The last element of the list is", thislist[-1])

#RANGE OF INDEX
print("The 2nd, 3rd and 4th elements of the list are ",thislist[1:4])

#NOT INCLUDING AN ELEMENT
print("Fifth element with fourth index is not included",thislist[:4])

#PRINTS THE ELEMENTS FROM THE GIEN INDEX TILL THE END
print("Returns the items from Apple to the end", thislist[2:])

#CHECK IF ITEM IS IN THE LIST
if "Apple" in thislist:
    print("Yes, 'Apple' is in the list")
else :
    print("No, 'Apple' is not in the list")

#CHANGE ITEM VALUE
thislist[1] = "Blackcurrant"
print("List after changing an item value ",thislist)

#CHANGE A RANGE OF ITEM VALUES
thislist[1:3] = ["Blackcurrant", "Watermelon"]
print("List after changing a range of item values ", thislist)

#Change the second value by replacing it with two new values:
thislist[1:2] = ["blackcurrant", "watermelon"]
print("Change the second value by replacing it with two new values", thislist)

#INSERT VALUES
thislist.insert(2, "watermelon")
print("Inserting an item at a given index", thislist)

#APPEND ITEMS - ADDS ITEM AT THE END OF THE LIST
thislist.append("orange")
print("Add an item at the end of the list", thislist)

#INSERT ITEM AT A SPECIFIC INDEX
thislist.insert(1, "orange")
print("After inserting an item at specified index", thislist)

#EXTEND LIST - BY ADDING ITEMS OF ANOTHER LIST AT THE END
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(" LIST AFTER ADDING ITEMS OF ANOTHER LIST AT THE END", thislist)

#EXTEND - add any iterable object (tuples, sets, dictionaries etc.)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("New list after adding any iterable object", thislist)

#REMOVE SPECIFIED ITEMS (THEIR FIRST OCCURENCE)
thislist.remove("kiwi")
print("New List after removing banana", thislist)

#POP - REMOVE SPECIFIED INDEX
thislist.pop(1)
print("New list after removing item at index 1 ", thislist)

#POP - REMOVES THE LAST ITEM
thislist.pop()
print("New list after popping out the last item ", thislist)

#DEL - REMOVES THE FIRST ITEM
del thislist[0]
print("New list after removing the first item", thislist)

#CLEAR THE LIST - The list still remains, but it has no content
thislist.clear()
print("After clearing the list", thislist)

#DEL - Delete the entire list:
del thislist
print("List is deleted")



# ==================================== Tuple =====================================


#CREATE A TUPPLE
thistuple = ("apple", "banana", "cherry")
print("Tupple is created", thistuple)

#TUPPLE WITH DUPLICATE VALUES
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("Tupple can have duplicate values", thistuple)

#LENGTH OF THE TUPPLE
print("Length of the tupple is", len(thistuple))

#TUPPLE WITH ONLY ONE ITEM AND PRINTING IT'S TYPE - must put a comma or else python will not understand it
thistuple = ("apple",)
print(type(thistuple))

#EMPTY TUPLE & DATA TYPE OF THE TUPLE
thistuple = ()
print(type(thistuple))


#ACCESSING THE ELEMENTS OF TUPLE
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

courses = ("Python" , "Data Science" , "Cloud Computing" , "Cyber Security" , "AI")
print( courses[1])
print( courses[3:5])
if "Python" in courses:
    print("Yes, python is in courses")
else:
    print("No, python is not in courses")
print (courses.index("Cloud Computing"))
print (len(courses))
add = ("Machine Learning" , "Web Development")
updated_courses =courses + add
print(updated_courses)
list_course = list(updated_courses)
list_course.remove("Cyber Security")
updated_courses = tuple(list_course)
print(updated_courses)




# ============================================= Dictionary ========================================


#CREATE A DICTIONARY
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x) #before the change
thisdict["color"] = "white"
print(x) #after the change

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("No, the model is not one of the keys")

thisdict["year"] = 2018
print(thisdict)
