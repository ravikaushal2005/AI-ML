
# how to run python 
""" code => byte code => python Virtual machine 
1.compile to bytecode (low level & palteform Independent )
-> bytecode runs faster 
.pyc -> compled python (frozen Binaries)

# __pycache__
Source change  & python version 
hello.py,cpython-312.pyc

->Works only for  imported files 
-> not for top level files """

# python virtual machine (PVM) """
-> code loop to itrate byte code 
->Run time engine 
->also known as python inter interpreter """

# Byte code
byte code is a not machine code 
-> pythoin specfic interpretaion 
-> cpython(standard impementation) ,jython ,ironpython, stackless,pypy

# linux basic command for python 
cd md 

# python in shell 
type in terminal : python3 

# print hello 
print("hello")

# modules 
import os 
os.getcwd()

import sys
sys.plateform 

from importlib import reload ( reload file )

reload(filename)
reload(hello)


# loop
for c in "chai":
... presstab print(c)
... presstab
c
h
a
i

# mutable and immutable 
In Python, objects are either mutable (can be changed after creation) or immutable (cannot be changed after creation).
# immutable 
int
float
bool
str
tuple
frozenset

# mutable
list
dict
set