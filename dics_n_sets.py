#dictionary is collection of key value pair in python
dics = {
    "key": "value",
    "number": 42,
    "bolean": False,
    "list": [1,"pppppppz",25.00,True]
}
print(dics)
print(dics["key"]) #output: value
print(dics["list"]) #output[1, 'pppppppz', 25.0, True]

'''
properties of dicsnary
1:dictionary are unordable
2:dictionary are mutable
3:dictionary are indexed
4:dictionary can't containes duplicate keys
'''
#dictionary method
print(dics.items()) # print all key value in the form of tuple
print(dics.keys()) #returnsd all the key of  dictionary
print(dics.get("number"))# return the value of key output:42


#set in python
#set is  a collection of non-repetative elements
set1 = set() # to create a empty set set1=() is nat a empty set it's a tuple
set1.add(1)
set1.add(2) # or set = {1,2}
print(set1)
#properties of set
'''
set are unordered
set are unindexed
there is no way to change set 
set element are unrepetable
'''
#method of set
s = {1,5,8,9,0, "what",6}
print(len(s))# output:6
print(s.remove(8)) # remove v8 from set
print(s.pop())#remove smallest number from the set
print(s.pop())
print(s)
print(s.pop())
print(s.union({5,10,"what","parvez"})) #return the combine value of both but if value already exist in set 
#then no combine because sets are unrepetable
print(s.intersection({4,8,0,"what"}))#return the value that both sets contain
print(s)


