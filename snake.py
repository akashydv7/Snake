import pygame as py
import pygame.freetype
import time, random, sys

# screen 
py.init()
swidth = 600
sheight = 600
iseaten = True
dir = ""
fx = 0
fy = 0
win = py.display.set_mode((swidth, sheight))
py.display.set_caption("SNAKE")
light = {
"background":(255, 250, 237),
"text":(255, 250, 237),
"textback":(1, 23, 43),
"snake":(46, 51, 71),
"food":(255, 0, 100),
"head":(0, 0, 0)
}
dark = {
"background":(17, 17, 17),
"text":(17, 17, 17),
"textback":(255, 250, 237),
"snake":(255, 250, 237),
"food":(255, 0, 100),
"head":(255, 255, 255)
}
pallete = light
win.fill(pallete["background"])
# THEME(61, 61, 70)


# TEXT section :

font = py.font.SysFont('freesansbold.ttf', 30)

score = -10

class Snake:
    def __init__(self, x, y, xspeed, yspeed):
        self.x = x
        self.y = y
        self.xspeed = xspeed*15
        self.yspeed = yspeed*15
        self.total = 0
        self.tail = []

    # updates the position of snake
    def update(self):
        global score
        self.death()

        if self.x == fx and self.y == fy:
            score+=10
            self.total += 1
            self.tail.append((self.x, self.y))
            iseaten = True
            picklocation()

        if self.total == len(self.tail) and self.total != 0:
            for i in range(len(self.tail)-1):
                self.tail[i] = self.tail[i+1]
            self.tail[self.total-1] = (self.x, self.y)
        time.sleep(0.08)

        if self.xspeed < 0:
            if self.x > 0:
                self.x += self.xspeed
            else:
                self.reset()
        elif self.xspeed > 0:
            if self.x < 585:
                self.x += self.xspeed
            else:
                self.reset()
        if self.yspeed < 0:
            if self.y > 0:
                self.y += self.yspeed
            else:
                self.reset()
        elif self.yspeed > 0:
            if self.y < 585:
                self.y += self.yspeed
            else:
                self.reset()
    # draws snake on the screen
    def show(self):
        win.fill(pallete["background"])
        for new in self.tail:
            py.draw.rect(win, pallete["snake"], (new[0], new[1], 15, 15))
        py.draw.rect(win, pallete["head"], (self.x, self.y, 15, 15), 9, 3)
        food()
        py.display.update()

    def reset(self):
        self.tail = []
        self.total = 0
        self.x = self.y = 0
        run = False
        res_screen()

    def death(self):
        for t in self.tail:
            if t[0] == self.x and t[1] == self.y:
                self.reset()


def food():
    global iseaten
    global score
    if iseaten == True:
        picklocation()
        py.draw.rect(win, pallete["food"], (fx, fy, 15, 15))
        py.display.update()
        iseaten = False
    elif iseaten == False:
        py.draw.rect(win, pallete["food"], (fx, fy, 15, 15))
        py.display.update()

def picklocation():
    global fx, fy
    fx = random.randrange(0, 585, 15)
    fy = random.randrange(0, 585, 15)

run = True

def game():
    global run
    global dir
    s = Snake(0, 0, 1, 0)
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
        keys = py.key.get_pressed()
        if keys[py.K_DOWN] and dir != "U":
            s.xspeed = 0
            s.yspeed = 15
            dir = "D"
        elif keys[py.K_UP] and dir != "D":
            s.xspeed = 0
            s.yspeed = -15
            dir = "U"
        elif keys[py.K_LEFT] and dir != "R":
            s.xspeed = -15
            s.yspeed = 0
            dir = "L"
        elif keys[py.K_RIGHT] and dir != "L":
            s.xspeed = 15
            s.yspeed = 0
            dir = "R"
        s.update()
        s.show()
    return

def menu():
    snk = font.render("SNAKE", True, pallete["text"])
    py.draw.rect(win, pallete["textback"], (240, 180, 120, 40))
    py.draw.rect(win, pallete["textback"], (240, 380, 120, 40))

    snk_rect = snk.get_rect(center=(swidth/2, 200))
    play = font.render("PLAY", True, pallete["text"])
    play_rect = play.get_rect(center=(swidth/2, 400))

    win.blit(snk, (snk_rect))
    win.blit(play, play_rect)
    py.display.update()

def restart_menu():
    txt = font.render("NICE TRY !", True, pallete["text"])
    scr = font.render(f"SCORE : {score}", True, pallete["text"])
    play = font.render("PLAY AGAIN", True, pallete["text"])

    py.draw.rect(win, pallete["textback"], (220, 180, 160, 40))
    py.draw.rect(win, pallete["textback"], (220, 220, 160, 40))
    py.draw.rect(win, pallete["textback"], (220, 380, 160, 40))

    txt_rect = txt.get_rect(center=(swidth/2, 200))
    scr_rect = scr.get_rect(center=(swidth/2, 240))
    play_rect = play.get_rect(center=(swidth/2, 400))

    win.blit(txt, txt_rect)
    win.blit(scr, scr_rect)
    win.blit(play, play_rect)
    py.display.update()

def main_screen():
    global pallete
    r = True
    while r:
        change = False 
        mouse = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == py.QUIT:
                r = False
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                print("Clicked", mouse)
                if 240<=mouse[0]<=360 and 380<=mouse[1]<420:
                    r = False
                elif 552<=mouse[0]<=590 and 12<=mouse[1]<33:
                    if pallete==light:
                        pallete=dark
                        win.fill(pallete["background"])
                        change = True
                    else:
                        pallete=light
                        win.fill(pallete["background"])
                        change=True
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE or event.key==py.K_RETURN:
                    r = False
        theme(change)
        menu()
    game()

def res_screen():
    global pallete
    r = True
    while r:
        mouse = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == py.QUIT:
                r = False
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if 240<=mouse[0]<=360 and 380<=mouse[1]<420:
                    r = False
                elif 552<=mouse[0]<=590 and 12<=mouse[1]<33:
                    if pallete==light:
                        pallete=dark
                        win.fill(pallete["background"])

                    else:
                        pallete=light
                        win.fill(pallete["background"])

                    print("changed")

            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE or event.key==py.K_RETURN:
                    r = False
                    break
        # win.fill(pallete["background"])
        theme()
        restart_menu()
    game()
def theme(change=False):
    unsel = pallete["snake"]
    py.draw.rect(win, unsel, (552, 12, 36,21), 3, 3)
    py.draw.rect(win, unsel, (570, 15, 15, 15))
    # py.draw.rect(win, unsel, (555, 15, 15, 15))
    py.display.update()
main_screen()