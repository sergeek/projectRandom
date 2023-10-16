"""
Can you make any predictions about random numbers, or find patterns?
Apparently you can, let me explain. 

You can find out how many times in a row you can hit the same number after specified number of rolling random numbers.

The formula goes like this: x^y=r
Where x is the number of sides, y is how many times in a row you want to hit the same side, and r is how many rolls needed to achieve it. 
So if I roll a 10 sided dice 1 trillion times, I should be able to get same number 12 times in a row at some point. 


And interesting that in first 2.7 trillion digits of pi, each number appears 12 times in a row, but number 8 appears 13 times in a row (and more will when approaching 10 trillion)

Here is the link where 2.7 trillion numbers of pi have been scanned and recorded any sequance: https://bellard.org/pi/pi2700e9/pidigits.html 
Longest Repetitions: (table from that site from scanned 2.7 trillion digits of pi)
Digit	Length	Position
0	    12	    1755524129973
1	    12	    1041032609981
2	    12	    1479132847647
3	    12	    1379574176590
4	    12	    1379889220413
5	    12	    1618922020656
6	    12	    1221587715177
7	    12	    368299898266
8	    13	    2164164669332
9	    12	    897831316556



So I can predict, if I roll 10 sided dice 9 times, most likely I will not hit the same number in a row 9 times. But if I roll it 1 billion times, at some point I will most likely hit the same number 9 times in a row. 

I wrote a program in Python to test the random number generator if it follows the same rules.

Result from 1 billion itteratoin, catching repetition of 9 or more:
number 2 appeared 9 times in a row on position 173,579,056
number 6 appeared 9 times in a row on position 390,750,973
number 8 appeared 9 times in a row on position 398,574,639
number 2 appeared 9 times in a row on position 485,156,781
number 9 appeared 9 times in a row on position 559,416,460
number 2 appeared 9 times in a row on position 573,300,293
number 7 appeared 9 times in a row on position 688,488,945
number 2 appeared 9 times in a row on position 856,549,591
Process finished in --- 638.715 seconds ---


"""



from random import randint
import time

#record how long it takes to run the programm
start_time = time.time()

# how many numbers to iterate
x = 1000000000
# ammount of repeats to catch and print on the line
r = 9

repeats = 1
previousN = None
# get random number from 0 to 9 x number of times
for i in range(1, x+1):
    n = randint(0, 9)

    if n == previousN:
        repeats += 1
    else:
        # catch and write how many times number appears in a row when >=r
        if repeats >= r:
            print(f'number {previousN} appeared {repeats} times in a row on position {i-repeats:,}')
        #reset repeats after there were no more repeated numbers
        repeats = 1
        # store previous random number to compare to the next one
        previousN = n


#print how long it took to run
print("Process finished in --- %s seconds ---" % round((time.time() - start_time), 3))

        
