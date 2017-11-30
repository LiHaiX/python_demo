#!/usr/bin/env python
#coding=utf-8

#python get and set
class Retangle:
    def __init__(self):
        self.width=0
        self.height=0

    def setSize(self,size):
        self.width,self.height=size

    def getSize(self):
        return self.width,self.height


    size=property(getSize,setSize)

r=Retangle()
r.width=10
r.height=20

print r.size
r.size=1,2
print r.size





