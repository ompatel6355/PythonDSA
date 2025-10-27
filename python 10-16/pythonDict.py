thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#from key function
x = ('key1', 'key2', 'key3')
y = (1, 2, 3)
# i = 0
# while i < len(y):
#     thisdict = dict.fromkeys(x, y[i])
#     print(thisdict)
#     i+=1
thisdict = dict.fromkeys(x, y)

print(thisdict)


#nested dict

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child1"]["name"])





# print(thisdict["brand"])
# print(len(thisdict))
# print(type(thisdict))

# thisdict["model"] = "Honda"
# print(thisdict.get("model"))

# print(thisdict.keys())
# thisdict.update({"color" : "white"})

# print(thisdict)



#One of the method to loop through dict to print out key and value
# for x in thisdict:
#     print(x, thisdict[x])
#2
# for x,y  in thisdict.items():
#     print(x, y)

#find the difference between two dict
# x = thisdict.copy()
# x.update({"color" : "white"})

# dif = x.keys() - thisdict.keys()
# print(dif)


