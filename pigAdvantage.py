from random import randrange

def averageList( arr ):
    total = 0
    for i in arr:
        total += bool( i )
    return ( total / len( arr ))

outcomes = [ 1 , 2 , 3 , 4 , 5 , 6 , 2 , 2 , 3 , 4 , 5 , 6 , 3 , 3 , 3 , 4 , 5 , 6 , 4 , 4 , 4 , 4 , 5 , 6 , 5 , 5 , 5 , 5 , 5 , 6 , 6 , 6 , 6 , 6 , 6 , 6 ]

results = []

for i in range( 1000000 ):
    rolling = 0
    while True:
        roll = outcomes[ randrange( 36 ) ]
        if roll == 1:
            results.append( 0 )
            print( 0 )
            break
        else:
            rolling += roll
            if rolling > 40:
                results.append( rolling )
                print( rolling )
                break

print( averageList( results ) )