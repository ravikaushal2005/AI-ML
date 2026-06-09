#set 
''' set is a collection which is unordered, unchangeable*, and unindexed. 
    *Note: Set items are unchangeable, but you can remove items and add new items.'''

#creating a set
myset = {"apple", "banana", "cherry"}
print(myset)
#accessing set items
''' you cannot access items in a set by referring to an index, since sets are unordered. but you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword. '''
for x in myset:
    print(x)
print("banana" in myset)
#adding items to a set
''' you can add items to a set using the add() method. '''
myset.add("orange")
print(myset)
#removing items from a set
''' you can remove items from a set using the remove() method, or the discard() method. the difference between remove() and discard() is that remove() will raise an error if the specified
item is not present in the set, while discard() will not raise an error. '''
myset.remove("banana")
print(myset)
myset.discard("grape")
print(myset)    
