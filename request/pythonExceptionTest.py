#!/usr/bin/env python
#coding=utf-8

#python Exception Demo

class pythonExceptionTest:

    while True:
        x = input('enter the first ')
        y = input('enter the second ')
        try:
            value=x/y
            print 'x/y is ',value
        except Exception,e:
            print 'Invalid input' ,e
            print 'try again'
        else :
            break
        finally:
            print 'clean up ....'