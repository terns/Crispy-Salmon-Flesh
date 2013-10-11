# -*- coding: utf-8 -*-
# Name: Amber
# Evergreen Login: hartra06
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###
import math
# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

x = 0 
a = 1 
import hw2_test
b = hw2_test.n
while a <= b: 
    x += a 
    a += 1    
print  x

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"



for c in range (2,11): 
    print c ** -1        


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

g = 10
triangular = 0
for j in range (1,(g+1)):
    triangular += j
print "Triangular number", g, "via loop:", triangular
print "Triangular number", g, "via formula:", g*(g+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

h = 10
m = 1
for k in range (1,(h+1)):
    m *= k
print m
###could also have used math.factorial here


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"
for q in range (10,0,-1): 
    print math.factorial (q) 

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"


y = 0 
r = 1 
s = 10
while r <= s: 
    y += (math.factorial (r)) ** -1 
    r += 1    
print  y+1

###
### (◡ ‿ ◡ ✿) ♡no collaboratorz♡ (✿◡ ‿ ◡ )
###

# ... Looked up a few operators, which is how i learned about the +=, *=, etc. operators and looked at math commands
# ... as a comment (on a line starting with "#").

###
### Assignment took me a few hours, reading took about 1.5 hours with note taking...
### Used Resources online to help with finding easier, more elegant solutions

