import pygame
import requests
import json
from PIL import Image

pygame.init()

# misc
deg_s = u'\N{DEGREE SIGN}'

# Creating pygame font
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 15)
textsurface3 = myfont.render(f"Portland, 45.5{deg_s}N,122.6{deg_s}W", False, (0,0,0))
textsurface4 = myfont.render(f"Copenhagen, 55.7{deg_s}N,12.7{deg_s}E", False, (0,0,0))
textsurface5 = myfont.render(f"Rio de Janeiro, 22.9{deg_s}S,43.2{deg_s}W", False, (0,0,0))
textsurface6 = myfont.render(f"Sydney, 33.9{deg_s}S,151.2{deg_s}W", False, (0,0,0))
textsurface7 = myfont.render(f"Johannesburg, 26.2{deg_s}S,28{deg_s}W", False, (0,0,0))

# The screen surface
screen = pygame.display.set_mode([1430,735])

# Loading the png image file to understand pixel width and height
im = pygame.image.load("World Map.png")

# Importing World Image...
image = Image.open("World Map.png")
width, height = image.size


# Understanding Ratio Between Pixel Width and Height, and Lat and Long
x = round(width / 360)
y = round(height / 180)

# Centering
cntrx = round(width / 2)
cntry = round(height / 2) -10

# FPS / Can't pull from the API more than once every 5 seconds
clock = pygame.time.Clock()

def find_coord(a,b):
    global coordinatex, coordinatey
    coordinatex = round(a * x + cntrx)
    coordinatey = round(-b * y + cntry + 8)

# Main loop()
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Frame Rate
    clock.tick(1)

    # Pulling info and converting it to JSON
    response = requests.get("http://api.open-notify.org/iss-now.json")
    inf_ = response.json()

    # Setting lat and long coordinates after pulling info from the API
    lat = float(inf_['iss_position']['latitude'])
    long = float(inf_['iss_position']['longitude'])

    # Creating long / lat coordinates to hover over ISS pin
    textsurface = myfont.render(f"ISS, Lat: {lat}{deg_s}, Long: {long}{deg_s}", False, (0,0,0))

    # Refreshing the screen
    screen.blit(im, [0,0])

    # Hover your mouse over an area to see long / lat coordinates
    mx, my = pygame.mouse.get_pos()
    if  0 < mx < 1430 and 0 < my < 735:
        c = (mx / x) - 179
        v = -((my / y) - 91.5)
        textsurface2 = myfont.render(f"Lat: {v}{deg_s}, Long: {c}{deg_s}", False, (0, 0, 0))
        screen.blit(textsurface2, (80, 700))

    # Placing pins for Major Cities
    find_coord(a=-122.6, b=45.5)
    pygame.draw.rect(screen, color=(0,0,0), rect=(coordinatex, coordinatey, 5, 5))
    screen.blit(textsurface3, (coordinatex -30, coordinatey -20))

    find_coord(a=12.6, b=55.7)
    pygame.draw.rect(screen, color=(0,0,0), rect=(coordinatex, coordinatey, 5, 5))
    screen.blit(textsurface4, (coordinatex -30, coordinatey -20))

    find_coord(a=-43.2, b=-22.9)
    pygame.draw.rect(screen, color=(0,0,0), rect=(coordinatex, coordinatey, 5, 5))
    screen.blit(textsurface5, (coordinatex -30, coordinatey -20))

    find_coord(a=151.2, b=-33.9)
    pygame.draw.rect(screen, color=(0,0,0), rect=(coordinatex, coordinatey, 5, 5))
    screen.blit(textsurface6, (coordinatex -30, coordinatey -20))

    find_coord(a=28, b=-26.2)
    pygame.draw.rect(screen, color=(0,0,0), rect=(coordinatex, coordinatey, 5, 5))
    screen.blit(textsurface7, (coordinatex -30, coordinatey -20))

    # Finding the interpretable coordinate
    find_coord(a=long,b=lat)

    # Spawn real-time coordinates over ISS pin
    screen.blit(textsurface, (coordinatex -50, coordinatey -25))

    # Creating the Pin
    square = pygame.Rect(coordinatex, coordinatey, 5, 5)

    # Placing Pin on Map
    pygame.draw.rect(screen, color=(255,0,0), rect=square)

    pygame.display.flip()