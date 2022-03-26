import random
from PIL import Image

# Importing World Image...
im = Image.open("World Map.png")
width, height = im.size
impix = im.load()

# Understanding Ratio Between Pixel Width and Height, and Lat and Long
x = round(width / 360)
y = round(height / 180)

# These variables could be a more accurate way to center the graph
x3 = round(width / 2)
y3 = round(height / 2)

# Centering For My For Loop / Did some fine tuning with -8 and +7


# Variables...
deg_s = u'\N{DEGREE SIGN}'

# Main
run = True
while run:
   
    ans1 = input("Enter a coordinate or request a random coordinate? (a/b)\n")

    # You Can Type In Your Own Coordinate Or Request A Random Coordinate
    if ans1 == 'a':
        lat = float(input("Enter a lattitude coordinate(lat=-90/90)\n"))
        long = float(input("Enter a longitude coordinate(long=-180/180)\n"))
    elif ans1 == 'b':
        lat = random.uniform(-90,90)
        long = random.uniform(-180,180)

        lat = round(lat, 2)
        long = round(long, 2)

    # Lat / Long Coordinate Asthetics
    if long > 0:
        dir1 = 'E'
    else:
        dir1 = 'W'

    if lat > 0:
        dir2 = 'N'
    else:
        dir2 = 'S'

    
    # Finding the interpretable coordinate
    coordinatex = round(long * x + x3)
    coordinatey = round(-lat * y + y3)

    # Opposite side of the globe coordinates
    if coordinatex > 0:
        _coordinatex = coordinatex - x3
    else:
        _coordinatex = coordinatex + x3

    if coordinatey > 0:
        _coordinatey = -coordinatey
    else:
        _coordinatey = -coordinatey

    # Placing Pin on Map
    for i in range(coordinatex, coordinatex + 8):
        for p in range(coordinatey, coordinatey + 8):
            try:
                impix[i,p] = (150,0,0)
            except Exception:
                pass
    
    # Opposite Pin
    for i in range(_coordinatex, _coordinatex + 8):
        for p in range(_coordinatey, _coordinatey + 8):
            try:
                impix[i,p] = (0,150,0)
            except Exception:
                pass
    
        # Placing Pin on Map
    for i in range(coordinatex, coordinatex + 8):
        for p in range(coordinatey, coordinatey + 8):
            try:
                impix[i,p] = (150,0,0)
            except Exception:
                pass
    
    # pixel ==> coordinate variables
    c = ''
    v = ''

    def lat_long_conv(a,b):
        """
        Turning a pixel coordinate into a lat/long coordinate
        """
        global c,v
        c = (a / x) - x3
        v = (b / y) - y3


    def opposite(a,b):
        """
        This is the function of finding the opposite lat/long coordinate
        """
        global c,v
        if a > x3:
            c = a - x3
        else:
            c = a + x3

        if b > y3:
            v = -b
        else:
            v = -b

    ans2 = input("would you like to find Earth sandwiches? (y/n)\n")

    if ans2 == 'y':
        # Finding Earth Sandwich Locations
        for i in range(0, width):
            for p in range(0, height):
                opposite(a=i,b=p)
                # I have to use try because the c, v variables get out of index
                # I need to completely flip the values in the opposite function
                try:
                    if 220 > impix[i,p][2]:
                        if 220 > impix[c,v][2]:
                            impix[i,p] = (255,0,0)
                            impix[c,v] = (255,0,0)
                    else:
                        pass
                except Exception:
                    pass
    


    location = f"{lat}{deg_s}{dir2},{long}{deg_s}{dir1}"
    print(location)
    
    im.show()