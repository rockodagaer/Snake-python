import pygame # pip install pygame (recogment python version 3.10.5)
import random
import tkinter as tk
from tkinter import messagebox

rows2 = int(input('Enter number of rows: ')) # this will be the size of the grid its rows*rows for the x and y ( for best experience set to 20 )

screenX, screenY = 800, 600 # screen size can only be this. 1080p or any other sizes will keep the same screen size
screen = pygame.display.set_mode((screenX, screenY)) # makes the screen will be set to W*W for default.
class Cube(object): # the function that does the drawing
    global rows2
    rows = rows2 # set the row size
    w = 500 # width can stay the same but you could experience with some other sizes

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny): # move the players snake
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False): # draw the player ( recogment setting eyes to False if you use a smaller size than recogmended )
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes: # recogment setting to false if grid size other than 20
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class Snake(object): # all the player components
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos) # this will be where the player head is located
        self.body.append(self.head) # all the positions of the cubes are located in here (incl head)
        self.dirnx = 0 # head direction X
        self.dirny = 1 # head direction Y

    def move(self): # get the controlls and move later ( snake goes to fast if moved inside component )
        keys = pygame.key.get_pressed() # get key pressed

        for key in keys:
            if keys[pygame.K_LEFT]:
                if not self.dirnx == 1: self.dirnx = -1 # it checks if its not going in the reverse direction because you will die without reason without
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] # turn

            elif keys[pygame.K_RIGHT]:
                if not self.dirnx == -1: self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                if not self.dirny == 1: self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                if not self.dirny == -1: self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def reset(self, pos): # used if you die
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self): # used if you eat a fruit
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface): # draw the snake
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface): # draw grid (w = 5 for invisible grid, usefull for smaller or bigger snake size)
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface): # update screen
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(5, rows, surface)
    pygame.display.update()


def randomSnack(rows, item): # move the snack
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(subject, content): # used to draw the lose message
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main(): # main game
    global width, rows2, s, snack
    width = 500 # change this for bigger screen
    rows = rows2
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    snack = Cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    frame = 0

    while flag: # main loop
        frame += 1
        s.move()

        if frame % 8 == 0: # move the player
            for i, c in enumerate(s.body):
                p = c.pos[:]
                if p in s.turns:
                    turn = s.turns[p]
                    c.move(turn[0], turn[1])
                    if i == len(s.body) - 1:
                        s.turns.pop(p)
                else:
                    if c.dirnx == -1 and c.pos[0] <= 0:
                        c.pos = (c.rows - 1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                        c.pos = (0, c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                        c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0:
                        c.pos = (c.pos[0], c.rows - 1)
                    else:
                        c.move(c.dirnx, c.dirny)
        clock.tick(60)
        if s.body[0].pos == snack.pos: # check if touching fruit
            s.addCube()
            snack = Cube(randomSnack(rows, s), color=(0, 255, 0))
            if s.body[0].pos[0] < 0 or s.body[0].pos[0] > rows - 1 or s.body[0].pos[1] < 0 or s.body[0].pos[1] > rows - 1:
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play again...')
                s.reset((10, 10))

        for x in range(len(s.body)): # check if touching body
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play again...')
                s.reset((10, 10))
                break

        redrawWindow(win) # redraw
        for event in pygame.event.get(): # get the quit command
            if event.type == pygame.QUIT:
                flag = False # quit the main loop
                pygame.quit()


main() # run the game
