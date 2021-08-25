##Battleship by itzliquauhtli
##
##version 1.0.0 finished 04/13/2019
##
##The classic pen-and-paper game implemented in the python console because I got bored in class.
##Single Player, with a dumb ai opponent.
##Designed with flexibility in mind, with ocean size and ships configurable.

from random import randrange, randint
from copy import copy

##Functions;
##
##printList( arr arr ):
##    Prints all elements of a list, used for debuging
##emptyBoard( str tile , int x , int y ):
##    Returns a 2d array of dimmensions x by y.
##    All elements are the tile string, which is usually the "sea" variable
##    Used to generate the initial board, before filling it with ships.
##print2dArray( arr board ):
##    Prints a 2d array to the console.
##displaySingle( arr board ):
##    Makes a board with axis labels above and to the right, then prints it to the screen.
##displayDual( arr boardP , arr boardO ):
##    Calls displaySingle twice, makes the main program a bit neater
##getCoord():
##    Prompts the user for a coordinate on the board. Expects standard battleship names
##    (i.e. E5, F8, a1, etc.) Can be lowercase or uppercase.
##    Returns an array [ y , x ] for use in targeting
##getCoordRand( int y , int x ):
##    Returns a random coordinate of form [ y , x ]
##binaryPrompt( str prompt , str pos , str neg )
##    Asks the user a binary question.
##    Return true if answer equals pos, false if neg, and loops if anything else.
##placeValidate( board , ship , tile , aim , ort )
##    Makes sure the ship fits where the user has placed it. Returns an int based on the result of the check;
##        Returns 0 if the check found no issues with the placement
##        Returns 1 if the ship overlaps with another
##        Returns 2 if the ship runs off the edge of the board.
##placeVtc( arr board , arr ship , arr aim ):
##    Run through the board array and change each tile in the ship's path to the appropriate tile. For vertical use only.
##    Returns the modified board array.
##placeHrz( arr board , arr ship , arr aim ):
##    Run through the board array and change each tile in the ship's path to the appropriate tile. For horizontal use only.
##    Returns the modified board array.
##placeCombined( board , ship , aim , ort )
##    One function that runs either placeVtc or placeHrz depending on ort value.
##    Literally just lets manPlaceShip and randPlaceShip look a lot neater.
##    Returns the modified board array.
##manPlaceShip( arr board , arr ship , str tile ):
##    Allows the player to manually place one ship on their board by specifying the closest square to the origin, and wether it is horizontal 
##    or vertical.
##    Returns the board array, modified with the ship's tiles in the proper place.
##manFullPlace( arr board , arr ships , str tile ):
##    One function to run through the list of ships and prompt the user to place all of them.
##    Returns the board array, modified with all of the ships' tiles.
##randPlaceShip( arr board , arr ship , str tile ):
##    Same as manPlaceShip, but done with random values for the coordinates and orientation.
##    Returns the board array, modified with the ship's tiles.
##randFullPlace( arr board , arr ships , str tile ):
##    Same as manualFullPlace, but calling randPlaceShip rather than manPlaceShip. Works entirely in the background.
##    Returns the board array, modified with all of the ships' tiles.
##pBoardSetup( str tile , int y , int x ):
##    Fully sets up the player's initial board using the above functions. 
##    First, asks if the player would like to manually place ships, or randomize their setup, then calls the appropriate ___FullPlace function.
##    Once the called function resolves, displays the board and prompts the user to confirm their starting positions.
##    Loops until this confirmation is given.
##    Returns the complete board, ready to start the game.
##getShips( arr board , arr ships )
##    Gets an array of ships with locations from a board with displayed ships. 
##    Returns an array of ships. See the ship_list comment for information on the structure.
##oFullSetup( arr board , arr ships , str tile ):
##    Randomly sets a board up for the opponent, records the ship positions, then clears the board for gameplay
##hitDetect( arr ship , arr shot , bool isPlayer ):
##    Checks if a given shot intersects with one ship. Returns true if a hit is detected, false if it's a miss
##pSingleFire( arr board , arr ships , str h , str m ):
##    Ask the player for a coordinate, and run through a list of ships to check if it's a hit.
##    Replaces the coordinate with a hit or miss tile, depending on the result.
##oSingleFire( arr board , arr ships , str h , str m ):
##    This is literally the worst possible AI immaginable, I'm not even sure this counts as AI, i made no attempt
##    to make it smart, it just picks random coordinates, checks if its fired there before, then if it hasnt, hits fire.
##getShotNum( arr ships , bool isPlayer ):
##    For Barrage mode, tells the two following function how many shots to allow each combatant
##pBarrage( arr board , arr ships , str h , str m ):
##    Player Barrage, prompts the player for a number of coordinates equal to the number of ships they still control.
##oBarrage( arr board , arr ships , str h , str m ):
##    Same as pBarrage, but picks coordinates randomly and fires for the opponent AI
##checkGameOver( arr ships , bool isPlayer ):
##    Function to check whether either combatant has sunk the last of their opponent's ships. 
##    Ends the game in the main loop


def printList( arr ):
    for i in arr:
        print( i )

def emptyBoard( tile , y , x ):
    board = [ ]
    for i in range( y ):
        board.append( [ ] )
        for j in range( x ):
            board[ i ].append( tile )
    return board

def print2dArray( board ):
    for i in board:
        print( " ".join( i ) )
    return True

def displaySingle( board ):
    prtBoard = emptyBoard( "~" , len( board ) + 1 , len( board[ 0 ] ) + 1 )
    for i in range( len( prtBoard ) ):
        for j in range( len( prtBoard[ i ] ) ):
            if ( i == 0 ):
                if ( j == 0 ):
                    prtBoard[ i ][ j ] = " `"
                else:
                    prtBoard[ i ][ j ] = chr( j + 96 ).upper()
            elif ( j == 0 ):
                temp = ""
                if ( i < 10 ):
                    temp += " "
                temp += str( i )
                prtBoard[ i ][ j ] = temp
            else:
                prtBoard[ i ][ j ] = board[ i - 1 ][ j - 1 ]
    print2dArray( prtBoard )
    return True

def displayDual( boardP , boardO ):
    displaySingle( boardO )
    print( "" )
    displaySingle( boardP )
    print( "" )

def getCoord():
    while True:
        aim = input( "Please enter coordinates: " )
        try:
            x = int( aim[ 0 ] )
            print("I didn't understand that. Enter your coordinates in the form A1, B2, etc.")
        except ValueError:
            x = ord( aim[ 0 ].lower() ) - 97
            y = int( aim[ 1: ] ) - 1
            return [ y , x ]

def getCoordRand( y , x ):
    return [ randrange( y ) , randrange( x ) ]

def binaryPrompt( prompt , pos , neg ):
    while True:
        check = input( prompt ).lower()
        if ( check == pos ):
            return True
        elif ( check == neg ):
            return False
        else:
            print( "Please only type " + pos.upper() + " or " + neg.upper() + ". Try again." )

def placeValidate( board , ship , tile , aim , ort ):
    check = 0
    try:
        if ( ort ):
            for i in range( aim[ 0 ] , aim[ 0 ] + ship[ 2 ] ):
                if ( board[ i ][ aim[ 1 ] ] == tile ):
                    check += 1
        else:
            for i in range( aim[ 1 ] , aim[ 1 ] + ship[ 2 ] ):
                if ( board[ aim[ 0 ] ][ i ] == tile ):
                    check += 1
        if ( check == ship[ 2 ] ):
            return 0
        else:
            return 1
    except IndexError:
        return 2

def placeVtc( board , ship , aim ):
    for i in range( aim[ 0 ] , aim[ 0 ] + ship[ 2 ] ):
        board[ i ][ aim[ 1 ] ] = ship[ 1 ]
    return board

def placeHrz( board , ship , aim ):
    for i in range( aim[ 1 ] , aim[ 1 ] + ship[ 2 ] ):
        board[ aim[ 0 ] ][ i ] = ship[ 1 ]
    return board

def placeCombined( board , ship , aim , ort ):
    if ( ort ):
        board = placeVtc( board , ship , aim )
    else:
        board = placeHrz( board , ship , aim )
    return board

def manPlaceShip( board , ship , tile ):
    while True:
        print( "Top/Left of our " + ship[ 0 ] + ". (Length = " + str( ship[ 2 ] ) + ")" )
        aim = getCoord()
        ort = binaryPrompt( "Will the ship be (V)ertical or (H)orizontal? " , "v" , "h" )
        check = placeValidate( board , ship , tile , aim , ort )
        if ( check == 0 ):
            print( "Deployment successfull." )
            print( "" )
            return placeCombined( board , ship , aim , ort )
        elif ( check == 1 ):
            print( "Ships cannot overlap. Try again." )
            print( "" )
        else:
            print( "Ships must remain inside the board. Try again." )
            print( "" )

def manFullPlace( board , ships , tile ):
    for ship in ships:
        displaySingle( board )
        board = manPlaceShip( board , ship , tile )
    return board

def randPlaceShip( board , ship , tile ):
    while True:
        ort = bool( randrange( 2 ) )
        aim = [ randrange( len( board ) ) , randrange( len( board[ 0 ] ) ) ]
        check = placeValidate( board , ship , tile , aim , ort )
        if ( check == 0 ):
            return placeCombined( board , ship , aim , ort )

def randFullPlace( board , ships , tile ):
    for ship in ships:
        board = randPlaceShip( board , ship , tile )
    return board

def findCoord( board , tile ):
    loc = []
    for i in range( len( board ) ):
        for j in range( len( board[ 0 ] ) ):
            if ( loc == [] and board[ i ][ j ] == tile ):
                loc = [ i , j ]
    try:
        loc.append( board[ loc[ 0 ] + 1 ][ loc[ 1 ] ] == tile )
    except IndexError:
        loc.append( False )
    return loc

def pBoardSetup( tile , y , x , ships ):
    while True:
        board = emptyBoard( tile , y , x )
        mode = binaryPrompt( "Deploy ships (M)anually or (A)utomatically? " , "m" , "a" )
        if ( mode ):
            board = manFullPlace( board , ships , tile )
        else:
            board = randFullPlace( board , ships , tile )
        displaySingle( board )
        confirm = binaryPrompt( "Is this board OK? (Y/N) " , "y" , "n" )
        if ( confirm ):
            return board

def getShips( board , ships ):
    working = ships
    for ship in working:
        ship.append( findCoord( board , ship[ 1 ] ) )
        ship.append( ship[ 2 ] )
    return working

def oFullSetup( board , ships , tile):
    board = randFullPlace( board , ships , tile )
    aiShips = getShips( board , ships )
    board = emptyBoard( tile , len( board ) , len( board[ 0 ] ) )
    return aiShips

def hitDetect( ship , shot , isPlayer ):
    for i in range( ship[ 2 ] ):
        if ( isPlayer ):
            origin = copy( ship[ 5 ] )
        else:
            origin = copy( ship[ 3 ] )
##        print( origin ) # Debug Prints
##        print( ship[ 3 ] , ship[ 5 ])
        if ( origin[ 2 ] ):
            origin[ 0 ] += i
        else:
            origin[ 1 ] += i
##        print( origin ) # Debug Prints
##        print( ship[ 3 ] , ship[ 5 ])
        if ( shot[ 0 ] == origin[ 0 ] and shot[ 1 ] == origin[ 1 ] ):
            return True
    return False

def pSingleFire( board , ships , h , m ):
    miss = True
    while True:
        shot = getCoord()
        try:
            if ( board[ shot[ 0 ] ][ shot[ 1 ] ] != h and board[ shot[ 0 ] ][ shot[ 1 ] ] != m ):
                break
            else:
                print( "You've already shot there." )
        except IndexError:
            print( "That's outside of our range." )
    for ship in ships:
        if ( hitDetect( ship , shot , False ) ):
            miss = False
            board[ shot[ 0 ] ][ shot[ 1 ] ] = h
            ship[ 4 ] -= 1
            print( "Hit!" )
            if ( ship[ 4 ] == 0 ):
                placeCombined( board , ship , ship[ 3 ] , ship[ 3 ][ 2 ] )
                print( "You've sunk their " + ship[ 0 ] + "!" )
            break
    if ( miss ):
        board[ shot[ 0 ] ][ shot[ 1 ] ] = m
        print( "Miss!" )

def oSingleFire( board , ships , h , m ):
    miss = True
    while True:
        shot = getCoordRand( len( board ) , len( board[ 0 ] ) )
        if ( board[ shot[ 0 ] ][ shot[ 1 ] ] != h and board[ shot[ 0 ] ][ shot[ 1 ] ] != m ):
            break
    for ship in ships:
        if ( hitDetect( ship , shot , True ) ):
            miss = False
            board[ shot[ 0 ] ][ shot[ 1 ] ] = h
            ship[ 6 ] -= 1
            print( "Hit!" )
            if ( ship[ 6 ] == 0 ):
                print( "They've sunk our " + ship[ 0 ] + "!" )
            break
    if ( miss ):
        board[ shot[ 0 ] ][ shot[ 1 ] ] = m
        print( "Miss!" )

def getShotNum( ships , isPlayer ):
    shots = 0
    if ( isPlayer ):
        for ship in ships:
            if ( ship[ 6 ] > 0 ):
                shots += 1
    else:
        for ship in ships:
            if ( ship[ 4 ] > 0 ):
                shots += 1
    return shots

def pBarrage( board , ships , h , m ):
    shotNum = getShotNum( ships , True )
    shots = []
    for i in range( shotNum ):
        while True:
            print( str( shotNum - i ) + " shots remaining." )
            shot = getCoord()
            overlap = False
            for j in shots:
                if ( shot == j ):
                    overlap = True
            if ( overlap ):
                print( "We're already targeting this location for this battery." )
                continue
            try:
                if ( board[ shot[ 0 ] ][ shot[ 1 ] ] == h or board[ shot[ 0 ] ][ shot[ 1 ] ] == m ):
                    print( "You've already shot there." )
                else:
                    shots.append( shot )
                    print( "Locked in." )
                    break
            except IndexError:
                print( "That's outside of our range." )
    for shot in shots:
        miss = True
        for ship in ships:
            if ( hitDetect( ship , shot , False ) ):
                miss = False
                board[ shot[ 0 ] ][ shot[ 1 ] ] = h
                ship[ 4 ] -= 1
                print( "Hit!" )
                if ( ship[ 4 ] == 0 ):
                    placeCombined( board , ship , ship[ 3 ] , ship[ 3 ][ 2 ] )
                    print( "You've sunk their " + ship[ 0 ] + "!" )
                break
        if ( not hit ):
            board[ shot[ 0 ] ][ shot[ 1 ] ] = m
            print( "Miss!" )

def oBarrage( board , ships , h , m ):
    shotNum = getShotNum( ships , False )
    shots = []
    for i in range( shotNum ):
        while True:
            shot = getCoordRand( len( board ) , len( board[ 0 ] ) )
            overlap = False
            for j in shots:
                if ( shot == j ):
                    overlap = True
            if ( overlap ):
                continue
            elif ( board[ shot[ 0 ] ][ shot[ 1 ] ] != h and board[ shot[ 0 ] ][ shot[ 1 ] ] != m ):
                shots.append( shot )
                break
    for shot in shots:
        miss = True
        for ship in ships:
            if ( hitDetect( ship , shot , True ) ):
                miss = False
                board[ shot[ 0 ] ][ shot[ 1 ] ] = h
                ship[ 6 ] -= 1
                print( "Hit!" )
                if ( ship[ 6 ] == 0 ):
                    print( "They've sunk our " + ship[ 0 ] + "!" )
                break
        if ( miss ):
            board[ shot[ 0 ] ][ shot[ 1 ] ] = m
            print( "Miss!" )

def checkGameOver( ships , isPlayer ):
    afloat = getShotNum( ships , isPlayer )
    if ( afloat <= 0 ):
        return True
    else:
        return False

##Some effectively global variables used to set up the boards and play the game. Not *technically* globals, I'm just 
##setting them all up here and calling them in all of the functions when necessary.
##    sea  (default = "~"): The empty tile displayed wherever there isn't a hit, miss, or player ship
##    hit  (default = "X"): The tile placed wherever a hit is registered
##    miss (default = "X"): The tile placed whenever a miss is registered
##    lat  (default = 10): The height of the boards
##    lon  (default = 10): The width of the boards
##    score (default = 0): Starting score, don't change unles you just really want to see a high score
##    barrageMode (default = False): If set to true, the game will play in "Barrage Mode"
##        On a player's turn, they choose as many shots as they have floating ships. Then all shots are fired at the same time.

sea  = "~"
hit  = "X"
miss = "O"
lat = 10
lon = 10
score = 0
barrageMode = False

##Ships are written as lists within this list.
##    Element 0 is the name of the ship
##    Element 1 is the tile displayed on the player's board, as well as the opponent's board once the ship is sunk.
##    Element 2 is the ship's len.
##At the beginning of a game, the following values will be added to the list.
##    Element 3 is the location of the ship on the AI's board, written as a list [ y , x , orientation ].
##    Element 4 is the number of unshot locations of the opponent's ship, used to trigger the "You've sunk their ___!" dialogue and barrage mode.
##    Element 5 is the location of the ship on the player's board, written as a list [ y , x , orientation ].
##    Element 6 is the number of unshot locations of the player's ship, used to trigger the "They've sunk our ___!" dialogue and barrage mode.

ship_list = [ [ "Carrier"     , "C" , 5 ] ,
              [ "Battleship"  , "B" , 4 ] ,
              [ "Destroyer"   , "D" , 3 ] ,
              [ "Submarine"   , "S" , 3 ] ,
              [ "Patrol Boat" , "P" , 2 ] ]

print( "Welcome to Battleship!" )
barrageMode = binaryPrompt( "Turn on Barrage Mode? Y/N " , "y" , "n" )

while True:
    oBoard = emptyBoard( sea , lat , lon )
    oFullSetup( oBoard , ship_list , sea )
    oBoard = emptyBoard( sea , lat , lon )

    pBoard = pBoardSetup( sea , lat , lon , ship_list )
    ship_list = getShips( pBoard , ship_list )
    
    while True:
##        print( "--ship_list--" ) #Prints the array w/ ship information for debugging
##        printList( ship_list )   #Or for cheating, I'm not a cop
        displayDual( pBoard , oBoard )
        if ( barrageMode ):
            pBarrage( oBoard , ship_list , hit , miss )
            if checkGameOver( ship_list , False ):
                print( "That's the last of them! We've won!" )
                score += 1
                break
            input( "Press Enter to sontinue." )
            oBarrage( pBoard , ship_list , hit , miss )
            if checkGameOver( ship_list , True ):
                print( "That's the last of our ships! We've lost!" )
                break
            input( "Press Enter to continue." )
        else:
            pSingleFire( oBoard , ship_list , hit , miss )
            if checkGameOver( ship_list , False ):
                print( "That's the last of them! We've won!" )
                score += 1
                break
            input( "Press Enter to sontinue." )
            oSingleFire( pBoard , ship_list , hit , miss )
            if checkGameOver( ship_list , True ):
                print( "That's the last of our ships! We've lost!" )
                break
            input( "Press Enter to continue." )
    
    confirm = binaryPrompt( "Would you like to play again? Y/N " , "y" , "n" )

print( "Your final score is " + score + ". Thank you for playing!" )
