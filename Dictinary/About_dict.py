# unordered  pair, changed, and index:---
# hash table :--
# {"key":"value"} -- {"key":{[]-[]} } ---- collisions
# key : {[][]}

# create :--
dict_empty = dict()
dict_em = {}  # O (1), (1)

# print(dict_empty,dict_em )

dict_em = dict(one="onevalue",two = "twovalues" ) #--O (n), (N)
# print(dict_em)

dict_en = dict([('one', 'one_Value'), ('two', 'two_values')])
# print(dict_en)

# Memory :---

# [value] <<-- key  
#    ||
#    ||
#    \/
#    [hashkey] --- specfic values -- e44rafafdauj  [values] <<e44rafafdauj

# collision >>

dict_sim = {"one":"one_Value", "two":"two_values"}

# print(dict_sim)

# operations in dict

# update :--
dict_sim["one"]="new_values" #--- O(1) , O(1)
# print(dict_sim)

# addition :--
dict_sim["add"]="new_values_add" #--- O(1) , O(1) -- O(n)
# print(dict_sim)

# traverse:
def tra(dict_sim):
    for key in dict_sim:
        print(dict_sim[key])

# tra(dict_sim) # O(n) and O(1)

# search an element in dict:
def tra(dict_sim, value):
    # for key in dict_sim:
    #     if (dict_sim[key]) == value:
    #         print(key, value)
    for key, values in dict_sim.items():
        if values == value:
            print(key, values)

# tra(dict_sim, "new_values")    # O(n) and O(1)   
# print(dict_sim.items())



#delete and remove:---
# del dict_sim['one']
# print('del--')
# print(dict_sim)
# removed = dict_sim.pop('key_not_present', 'not')
# print('--removed')
# print(removed)
# print(dict_sim)
# print(dict_sim.popitem())
# dict_sim.clear()
# print(dict_sim) -- O(n), O(1)


# print(dict_sim.copy())
# print(dict_sim.fromkeys([1,2,3,4]))
# print(dict_sim.get("val", "2"))
# print(dict_sim.items())
# print(dict_sim.keys())
# print(dict_sim.values())
# print(dict_sim.popitem())
# dict_sim.setdefault('val', 'added')
# print(dict_sim)
# print(dict_sim.setdefault('val', 'added'))
# print(dict_sim.pop())
# val = {"new":"bbbb"}
# print(dict_sim)
# print(dict_sim.update(val))
# print(dict_sim)

# def fun():
#     return "1"
# print(fun())


# print(len(dict_sim))
# print("one" in dict_sim)
# print(all(dict_sim))
# print(any(dict_sim))
# print(sorted(dict_sim))

# print({key:val for key, val in dict_sim.items() if key =="one"})

# v={}
# for key, val in dict_sim.items():
#     if key =="one":
#         v[key]=val
# print(v)

