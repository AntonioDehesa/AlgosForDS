# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table
class MyHashtable(object):
    def __init__ (self, size): # Creates an empty hashtable
        self.size = size
        # Create the list of size n
        self.table = [None] * size
        self.status = [0] * size # I will use 0 for empty, 1 for removed, and 2 for filled
    def __str__ (self): # for print
        return str(self.table)
    def insert(self, elem): # Adds an element into the hashtable 
        hash = ord(elem[0]) % self.size 
        if hash > self.size:
            raise Exception("The hash is greater than the table size")
        else:
            i = hash
            while i < self.size:
                if self.status[i] == 0 or self.status[i] == 1:
                    self.table[i] = elem
                    self.status[i] = 2
                    break
                else:
                    i+=1
                    if i >= self.size:
                        i = 0
                    if i == hash: # If it gets to the hash again, it means that it tried every slot in the list, and none are empty
                        raise Exception("The table is full!")
                        
    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size 
        if hash > self.size:
            raise Exception("The hash is greater than the table size")
        else:
            i = hash
            while i < self.size:
                if self.status[i] == 0:
                    return False # The element was not there
                elif self.table[i] != elem:
                    i+=1
                    if i >= self.size:
                        i = 0
                    if i == hash: # if it gets to the hash again, it means that it has looped and still not found the element
                        return False
                else:
                    return True
    def delete(self, elem): # Removes an element from the hashtable 
        hash = ord(elem[0]) % self.size
        if hash > self.size:
            raise Exception("The hash is greater than the table size")
        else:
            i = hash
            while i < self.size:
                if self.status[i] == 0:
                    break # The element does not exist
                if self.table[i] != elem:
                    i+=1
                    if i >= self.size:
                        i = 0
                    if i == hash: # if it gets to the hash again, it means that it has looped and still not found the element
                        raise Exception("The element does not exist in the table")
                else:
                    self.table[i] = None
                    self.status[i] = 1
                    break

class MyHashtable2(object):
    def __init__ (self, size): # Creates an empty hashtable
        self.size = size
    # Create the list (of size) of empty lists (chaining)
        self.table = []
        for i in range(self.size): 
            self.table.append([])
    def __str__ (self): # for print
        return str(self.table)
    def insert(self, elem): # Adds an element into the hashtable 
        hash = ord(elem[0]) % self.size 
        self.table[hash].append(elem)
    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size 
        return elem in self.table[hash]
    def delete(self, elem): # Removes an element from the hashtable 
        hash = ord(elem[0]) % self.size 
        self.table[hash].remove(elem)
s = MyHashtable(10) 
s.insert("amy") #97
s.insert("chase") #99
s.insert("chris") #99 
print(s.member("amy")) 
print(s.member("chris")) 
print(s.member("alyssa")) 
s.delete("chase") 
print(s.member("chris"))
# You can use print(s) at any time to see the contents
# of the table for debugging
print(s)