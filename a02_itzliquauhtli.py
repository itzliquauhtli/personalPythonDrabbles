import turtle
from random import randrange

# Returns the Tue-Morse sequence as an array. Array length is 2^n, and each element is a bool(True or False)
# Trust me, this'll make sense in a bit.
def thueMorse( n ):
    n = 2 * n + 1
    out = [ True ]
    for i in range( n ):
        step = []
        for j in out:
            step.append( not j )
        for j in step:
            out.append( j )
    return out

def teleport( tt , pos ):
    tt.up()
    tt.goto( pos[ 0 ] , pos[ 1 ] )
    tt.down()
    return True

def koch( tt , order , pos , ort , step ):
    fractal = thueMorse( order )
    teleport( tt , pos )
    tt.seth( ort )
    tt.begin_fill()
    for i in range( 3 ):
        for j in fractal:
            if ( j ):
                tt.forward( step )
                tt.right( 60 )
            else:
                tt.right( 180 )
    tt.end_fill()
    return True

def colorString( n ):
    string = "#"
    if ( n > 3 ):
        string += "FF"
        n -= 4
    else:
        string += "00"
    if ( n > 1 ):
        string += "FF"
        n -= 2
    else:
        string += "00"
    if ( n > 0 ):
        string += "FF"
        n -= 1
    else:
        string += "00"
    return string

Adam = turtle.Turtle()
Adam.speed( 0 )
Adam.shape( "turtle" )
Adam.color( colorString( 0 ) )
Adam.fillcolor( colorString( 1 ) )

Brian = turtle.Turtle()
Brian.speed( 0 )
Brian.shape( "turtle" )
Brian.color( colorString( 1 ) )
Brian.fillcolor( colorString( 2 ) )

Charlie = turtle.Turtle()
Charlie.speed( 0 )
Charlie.shape( "turtle" )
Charlie.color( colorString( 2 ) )
Charlie.fillcolor( colorString( 3 ) )

David = turtle.Turtle()
David.speed( 0 )
David.shape( "turtle" )
David.color( colorString( 3 ) )
David.fillcolor( colorString( 4 ) )

Evan = turtle.Turtle()
Evan.speed( 0 )
Evan.shape( "turtle" )
Evan.color( colorString( 4 ) )
Evan.fillcolor( colorString( 5 ) )

Fred = turtle.Turtle()
Fred.speed( 0 )
Fred.shape( "turtle" )
Fred.color( colorString( 5 ) )
Fred.fillcolor( colorString( 6 ) )

Gilbert = turtle.Turtle()
Gilbert.speed( 0 )
Gilbert.shape( "turtle" )
Gilbert.color( colorString( 6 ) )
Gilbert.fillcolor( colorString( 7 ) )

Harry = turtle.Turtle()
Harry.speed( 0 )
Harry.shape( "turtle" )
Harry.color( colorString( 7 ) )
Harry.fillcolor( colorString( 0 ) )


turtle.ht()
turtle.bgcolor( "#888888" )
thruple = [ Adam , Brian , Charlie , David , Evan , Fred , Gilbert , Harry ]
width = int( turtle.window_width() / 2 )
height = int( turtle.window_height() / 2 )

while True:
    for tt in thruple:
        pos = [ randrange( - width , width ) , randrange( - height , height ) ]
        ort = randrange( 360 )
        order = randrange( 4 )
        step = randrange( 10 , 100 )
        if ( order != 0 ):
            step /= 2 ** order
        koch( tt , order , pos , ort , step )
