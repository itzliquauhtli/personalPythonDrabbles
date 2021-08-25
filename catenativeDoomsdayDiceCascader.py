## I found this method of rolling dice while browsing some forums
## I immediately asked "What is the average result of such a roll?"
## I couldn't work it out properly with math, so I dusted off my
## python and wrote this Monte Carlo simulation.

from random import random
from math import floor

## I think I forgot randrange and randint exist. This function just 
## returns a pseudorandom number i where 1 <= i <= x
def rollDie( x ):
    return floor(( random() * x ) + 1 )

## Ah, the meat of the program, the weird die. Basically, you start with
## the "prime die" (a d6) and roll it. The result tells you how many more
## dice you roll, and how big those dice are to start with. You now take
## one of those dice, and roll it. Multiply the number of sides of the
## remaining dice by the result. Continue this process until there are
## no dice left. The last number rolled is your result. In the original
## context, this was damage, but if anyone were insane enough to use this
## process in an actual game, it could theoretically be linked to anything.
##
## What follows is an example of one possible roll of the Catenative
## Doomsday Dice Cascader. Note, I will be using the D&D names for dice, i.e.
## a d6 for a six sided die, or a d20 for a twenty sided die:
##    Roll 0: d6
##        Result = 5
##        There are two results from this prime role:
##            1. You have 5 dice, and
##            2. They are all d5s
##    Roll 1: d5 
##        Result = 4
##            This die has been expended and all 
##            remaining d5s turn into d20s (5x4)
##    Roll 2: d20
##        Result = 13
##            This die has been expended and all 
##            remaining d20s turninto d260s (20x13)
##    Roll 3: d260
##        Result = 136
##            This die has been expended and all 
##            remaining d260s turninto d35,360s (260x136)
##    Roll 4: d35,360
##        Result = 13,856
##            This die has been expended and the last
##            die becomes ~d489 million
##    Roll 5: d489,948,160
##        Result = 83,094,565
##    In this instance, the die function returns 83,094,565.
## 
## Frankly this is the dumbest die roll I've ever seen and it's great.
def cascadeDie():
    n = rollDie( 6 )
    die_size = n
##    print( n ) # Debug print
    for i in range( n - 1 ): # This loop runs one less time than the total number of dice because the last rollDie call is inside the return line.
        die_size = die_size * rollDie( die_size )
##        print( " " + str( die_size ) ) # Debug print
    return rollDie( die_size )

## Form an array and fill it with a bunch of values from the cascadeDie() function
## This is a bad name, but I can't think of a better one so it's staying
def fullCascade( i ):
    arr = [] # Yes i know that Python uses linked lists, not arrays, shut up I learned to code with Java and I will keep using arr as my dummy variable name until i die
    for i in range( i ):
       arr.append( cascadeDie() )
    return arr

## Take the mean of a list of numbers
def averageList( arr ):
    total = 0
    for i in arr:
        total += i
    return ( total / len( arr ) )

## Now that we have our functions we roll the cascade die 100 times, printing
## each result to console. Then, we use our fullCascade and averageList
## functions to print the average of 10 lots of 100,000 rolls each.
print( "100 Example rolls:" )
for i in range( 100 ):
    print( "  " + str( cascadeDie() ) )

print( "" )
print( "10 average values of 100,000 rolls each" )
for i in range( 10 ):
    print( "  " + str( averageList( fullCascade( 100000 ) ) ) )
