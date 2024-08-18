"""
#
# Part: Python Collections
#List, Tuple, Set and Dictionary
#
"""

"""
#
# Part: Python List
#
"""
This_list=["apple", "banana", "coconu", "apple", "banana"]
print(This_list)
print(type(This_list))
print(len(This_list))

print(This_list[2])

This_list. append("cerry")
print(This_list, len(This_list))
This_list. insert(1, "orange")
print(This_list, len(This_list))

This_list2=["apple", "banana", "coconu", "apple", "banana"]
This_list3=["mango", "pineapple", "grape"]
This_list2.extend(This_list3)
print(This_list2, len(This_list2))

This_list4=["apple", "banana", "coconu", "apple", "banana"]
This_list4.remove("banana")
print(This_list4, len(This_list4))

This_list5=["apple", "banana", "coconu", "apple", "banana"]
This_list5.pop(2)
print(This_list5, len(This_list5))

This_list6=["apple", "banana", "coconu", "apple", "banana"]
del This_list6[1]
print(This_list6, len(This_list6))

This_list6.clear()
print(This_list6, len(This_list6))

del This_list5
# print(This_list5, len(This_list5))

This_list7=["orange", "mango", "kiwi", "pineapple", "banana"]
This_list7.sort()
print(This_list7, len(This_list7))

This_list8=["orange", "mango", "kiwi", "pineapple", "banana"]
This_list8.reverse()
print(This_list, len(This_list8))

This_list1=["a","b", "c" ]
This_list2=[1, 2, 3]
This_list3=This_list1+This_list2
print(This_list3)

"""
#
# Part: Python Tuple
#
"""
this_tuple=("apple", "banana", "coconu")
print(this_tuple)
print(type(this_tuple))
print(len(this_tuple))

print(this_tuple[0])

this_tuple2=("apple", "banana", "coconu")
this_tuple3_list=list(this_tuple2)
print(this_tuple3_list, type(this_tuple3_list))
this_tuple4=tuple(this_tuple3_list)
print(this_tuple4, type(this_tuple4))

this_tuple5=("apple", "banana", "coconu")
this_tuple6_list=list(this_tuple5)
this_tuple6_list.append("durian")
this_tuple7=tuple(this_tuple6_list)
print(this_tuple7, type(this_tuple7))

this_tuple8=("apple", "banana", "coconu")
this_tuple9_list=list(this_tuple8)
this_tuple9_list.remove("coconu")
this_tuple8=tuple(this_tuple9_list)
print(this_tuple8, type(this_tuple8))

del this_tuple8
# print(this_tuple8, type(this_tuple8))

tuple1=("a","b", "c")
tuple2=(1, 2, 3)
tuple3=tuple1+tuple2
print(tuple3, type(tuple3))

"""
#
# Part: Python set
#
"""
this_set={"apple", "banana", "coconu"}
print(this_set)
print(type(this_set))
print(len(this_set))

for x in this_set:
    print(x)

print("banana" in this_set)

this_set2={"apple", "banana", "coconu"}
this_set2.add("durain")
print(this_set2, type(this_set2))
this_set2.remove("coconu")
print(this_set2, type(this_set2))

this_set3={"apple", "banana", "coconu"}
this_set4={"durain", "grape"}
this_set3.update(this_set4)
print(this_set3, type(this_set3))

# Union (Euler)
this_set5={"apple", "banana", "coconu"}
this_set6={"durain", "grape",}
this_set7={1, 2, 3}
this_set8=this_set5 |this_set6|this_set7
print(this_set8, type(this_set8))

this_set.clear()
print(this_set8, type(this_set8))
del this_set8
# print(this_set8, type(this_set8))

"""
#
# Part: Python Dictionry
#
"""
this_dict={
    "brand":"Ford",
    "model":"Rapter",
    "year":"2024"
}
print(this_dict)
print(type(this_dict))
print(len(this_dict))

print(this_dict["brand"])
print(this_dict.get("year"))
print(this_dict.keys())

this_dict["year"]="1987"
print(this_dict)
this_dict.update({
    "year": "1988",
    "model": "Mustang"
})
print(this_dict)

print(this_dict)
this_dict["color"]="Red"

del this_dict["year"]
print(this_dict)

this_dict.clear()
print(this_dict, type(this_dict))
del this_dict
#print(this_dict, type(this_dict))

this_dict2={
    "brand":"Toyota",
    "model":"Yaris",
    "year":"2016"
}

this_dict3={
    "brand":"Honda",
    "model":"Civic",
    "year":"2024"
}

this_dict4={
    "brand":"Lamborghini",
    "model":"Huracan",
    "year":"2019"
}


my_car={
    "car1":this_dict2,
    "car2":this_dict3,
    "car3":this_dict4
}
print(my_car, len(my_car))
print(my_car["car2"]["model"])