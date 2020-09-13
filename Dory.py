import random
import pygame
import sys
import copy
import math

from pygame.locals import *

pygame.init()

shark = pygame.image.load('Bruce-FNsmall.png')
jelly = pygame.image.load('glowing_jellyfish.png')
purplejelly = pygame.image.load('purple_jellyfish1.png')
prettyJ = pygame.image.load('prettyyJelly3.png')

red = (255, 0, 0)
green = (83, 178, 10)
blue = (0, 0, 255)
lblue = (48, 179, 255)
dblue = (99, 197, 255)
white = (255,255,255)
black = (0,0,0)
yellow =(244, 205, 9)
screen = pygame.display.set_mode((1000, 700), 0, 32)
jtot = 40
stot = 6
ptot = 2
pjtot = 10
startGame = False

block_list = pygame.sprite.Group()


all_sprites_list = pygame.sprite.Group()

class pretty(pygame.sprite.Sprite):
   xxx = random.randint(100, 680)
   prettyJ = pygame.image.load('prettyyJelly3.png')
   hit = False
   goingL = True
   goingR = False

   def __init__(self, nuxx, nuyy):
       super().__init__()
       self.x = nuxx
       nuyy = random.randint(700, 900)
       self.y = nuyy
       self.tree = pygame.rect.Rect(self.x, self.y, 200, 98)

   def isisHit(self):
       return self.hit

   def draw(self):
       possit = [self.x, self.y]
       screen.blit(self.prettyJ, possit)

   def move(self, block, speed):
       speed = random.randint(4, 15)
       xxxe = block.getX() + 16
       yyye = block.getY() + 16

       if self.goingR:
           if self.x < 940:
               self.x += speed

       if self.x >= 940:
           self.goingL = True
           self.goingR = False

       if self.goingL:
           if self.x >= 940 or self.x > 0:
               self.x -= speed

       if self.x <= 0:
           self.goingL = False
           self.goingR = True

       if self.y <= -200:
           self.y = self.y + 700
       if self.y > -200:
           self.y = self.y - 2

       if (block.getX() >= self.x and block.getX() <= self.x + 20) or (xxxe >= self.x and xxxe <= self.x + 20):
           if block.getY() >= self.y and block.getY() <= self.y + 80 or (yyye >= self.y and yyye <= self.y + 80):
               self.hit = True


class purpur(pygame.sprite.Sprite):
   xx = random.randint(100, 680)
   purplejelly = pygame.image.load('purple_jellyfish1.png')
   hit = False
   goingL = False
   goingR = True

   def __init__(self, nux, nuy):
       super().__init__()
       self.x = nux
       nuy = random.randint(710, 900)
       self.y = nuy
       self.tree = pygame.rect.Rect(self.x, self.y, 200, 98)

   def isisHit(self):
       return self.hit

   def draw(self):
       posit = [self.x, self.y]
       screen.blit(self.purplejelly, posit)

   def move(self, speed, block):
       speed = random.randint(1, 6)
       xxe = block.getX() + 16
       yye = block.getY() + 16

       if self.goingR:
           if self.x < 940:
               self.x += speed

       if self.x >= 940:
           self.goingL = True
           self.goingR = False

       if self.goingL:
           if self.x >= 940 or self.x > 0:
               self.x -= speed

       if self.x <= 0:
           self.goingL = False
           self.goingR = True

       if self.y <= -200:
           self.y = self.y + 700
       if self.y > -200:
           self.y = self.y - 2

       if (block.getX() >= self.x and block.getX() <= self.x + 20) or (xxe >= self.x and xxe <= self.x + 20):
           if block.getY() >= self.y and block.getY() <= self.y + 80 or (yye >= self.y and yye <= self.y + 80):
               self.hit = True


class jellies(pygame.sprite.Sprite):
   locX = random.randint(100, 680)
   jelly = pygame.image.load('glowing_jellyfish.png')
   hit = False
   goingL = True
   goingR = False

   def __init__(self, numerx, numer):
       super().__init__()
       self.x = numerx
       numer = random.randint(710, 1000)
       self.y = numer
       self.tree = pygame.rect.Rect((self.x, self.y, 100, 20))


   def isHit(self):
       return self.hit

   def draw(self):
       pos = [self.x, self.y]
       screen.blit(self.jelly, pos)

   def move(self, block, speed):
       speed = random.randint(1, 5)
       xe = block.getX() + 16
       ye = block.getY() + 16

       if self.goingR:
           if self.x < 940:
               self.x += speed

       if self.x >= 940:
           self.goingL = True
           self.goingR = False

       if self.goingL:
           if self.x >= 940 or self.x > 0:
               self.x -= speed

       if self.x <= 0:
           self.goingL = False
           self.goingR = True

       if self.y <= -10:
           self.y = self.y + 700
       if self.y > -10:
           self.y = self.y - 2

       if (block.getX() >= self.x and block.getX() <= self.x + 20) or (xe >= self.x and xe <= self.x + 20):
           if block.getY() >= self.y and block.getY() <= self.y + 80 or (ye >= self.y and ye <= self.y + 80):
               self.hit = True


class log(pygame.sprite.Sprite):
 x = random.randint(100,680)
 tree = pygame.rect.Rect((0, x, 100,20))
 shark = pygame.image.load('Bruce-FNsmall.png')
 hit = False
 goingL = False
 goingR = True
 y =0

 def __init__(self, numx,num):
     super().__init__()
     self.y = num
     self.x = numx
     self.tree = pygame.rect.Rect((self.x, self.y, 100,20))

 def isHit(self):
         return self.hit

 def draw(self, surface):
     keys = [False, False, False, False]
     playerpos = [self.x, self.y]

     if self.goingL:
         Lshark = pygame.transform.flip(shark, True, False)
         screen.blit(Lshark, (self.x, self.y))

     if self.goingR:
         screen.blit(shark, playerpos)

 def move(self, speed, block):
     bxb = block.getX()
     bxe = block.getX() + 16
     byb = block.getY()
     bye = block.getY() + 16

     self.y -= 1
     if self.y < 0:
         self.y += 1400

     if self.goingR:

         self.x+=speed
         if (bxb >= self.x and bxb <= self.x + 100) or (bxe >= self.x and bxe <= self.x + 100):
             if byb >= self.y and byb <= self.y + 20 or (bye >= self.y and bye <= self.y + 20):
                 self.hit = True

         self.tree.move_ip(self.x, self.y)

         if self.x >= 920:
             self.goingR = False
             self.goingL = True

     if self.goingL:
        self.x-=speed
        if (bxb >= self.x and bxb <= self.x + 100) or (bxe >= self.x and bxe <= self.x + 100):
            if byb >= self.y and byb <= self.y + 20 or (bye >= self.y and bye <= self.y + 20):
                self.hit = True
        Lshark = pygame.transform.flip(shark, True, False)
        screen.blit(Lshark, (self.x, self.y))
        self.tree.move_ip(self.x, 0)
        if self.x <= 0:
             self.goingL = False
             self.goingR = True



class  block(pygame.sprite.Sprite):
 image = pygame.image.load("BabyDory2.png").convert_alpha()
 x = random.randint(0, 800)
 y = random.randint(0,150)
 rect = pygame.rect.Rect((x, y, 16,16))

 def setX(self, newx):
     self.rect.move_ip(abs(newx),0)
     self.x = newx

 def __init__(self):
     super().__init__()
     self.rect = pygame.rect.Rect((self.x, self.y, 16, 16))

 def getX(self):
     return self.x
 def getY(self):
     return self.y

 def movewLog(self,speed):
     print(speed)

     self.rect.move_ip(speed,0)
     self.x+=speed


 def handle_keys(self):


     if self.x < 0 or self.x > 1000:
         self.offScreen = True

     if self.y < 0 or self.y > 700:
         self.offScreen = True

     key = pygame.key.get_pressed()
     if key[pygame.K_LEFT]:
         if self.x > 0:
             self.rect.move_ip(-10, 0)
             self.x-=10
     if key[pygame.K_RIGHT]:
         if self.x < 970:
             self.rect.move_ip(10, 0)
             self.x+=10
     if key[pygame.K_UP]:
         if self.y > 0:
             self.rect.move_ip(0, -10)
             self.y-=10
     if key[pygame.K_DOWN]:
         if self.y < 670:
             self.rect.move_ip(0, 10)
             self.y+=10

 def draw(self, surface):
     playerpos = [self.x, self.y]
     screen.blit(self.image, playerpos)

class Button():
   def __init__(self, x, y):
       self.rect = pygame.rect.Rect((x, y, 100, 50))
       pygame.draw.rect(screen, red, [x, y, 100, 50])

   def draw(self, x, y):
         pygame.draw.rect(screen, red, [x, y, 100, 50])

   def pressed(self, mouse):
       if mouse[0] > self.rect.topleft[0]:
           if mouse[1] > self.rect.topleft[1]:
               if mouse[0] < self.rect.bottomright[0]:
                   if mouse[1] < self.rect.bottomright[1]:
                      return True
                   else: return False
               else: return False
           else: return False
       else: return False

levelOne = Button(500, 300)

square = block()
square.draw(screen)

randodo = random.randint(500, 800)
purp_list = []

for p in range(ptot):
   randodox = random.randint(0, 800)
   randodoy = random.randint(500, 800)
   purp_list.append(purpur(randodox, randodoy))

pretJ_list = []
for pj in range(pjtot):
   randododox = random.randint(0, 800)
   randododoy = random.randint(500, 800)
   pretJ_list.append(pretty(randododox, randododoy))

rand = random.randint(200,280)
tree_list = []

for x in range(stot):
 randx = random.randint(0, 800)
 randy = random.randint(200,700)
 tree_list.append(log(randx,randy))

for t in tree_list:
 t.draw(screen)
 speed = 3
 t.move(speed,square)
 clock = pygame.time.Clock()

clock = pygame.time.Clock()

rando = random.randint(100, 600)
jellyfish = jellies(rando, rando)

jellos_list = []

for i in range(jtot):
   randox = random.randint(0, 830)
   randoy = random.randint(100, 700)
   jellos_list.append(jellies(randox, randoy))

for j in jellos_list:
   speed = random.randint(10, 12)
   j.move(square, speed)
   clock2 = pygame.time.Clock()

clock2 = pygame.time.Clock()

bgStart = pygame.image.load('underwater1.png')
bgOne = pygame.image.load('BetterTHREE.png')
bgTwo = pygame.image.load('ONE.png')
bgThree = pygame.image.load('BetterONE.png')
bgFour = pygame.image.load('FindingNemoReef.png')
bgFive = pygame.image.load('FindingNemoReef2.png')
bgSix = pygame.image.load('DarkerReef1.png')
bgSeven = pygame.image.load('DarkerReef2.png')
bgEight = pygame.image.load('DarkerReef3.png')
bgNine = pygame.image.load('trenchbg.png')
bgTen = pygame.image.load('trenchbg2.png')

bgOne_y = 0
bgTwo_y = bgOne_y + 700
bgThree_y = bgTwo_y + 700
bgFour_y = bgThree_y + 700
bgFour_x = 0
bgFive_x = bgFour_x + 1242
bgSix_x = bgFive_x + 1242
bgSeven_x = bgSix_x + 1242
bgEight_x = bgSeven_x + 1242
bgNine_x = bgEight_x + 1187
bgTen_x = bgNine_x + 1187
bgNine_y = 0
bgTen_y = 0


on = False

running = True
while running:
 for event in pygame.event.get():
     event = pygame.event.poll()
     if event.type == pygame.QUIT:
         break
         running = False
     mouse = pygame.mouse.get_pos()
     if levelOne.pressed(mouse):
             startGame = True
     elif event.type == pygame.MOUSEMOTION:
             x, y = pygame.mouse.get_pos()
             pygame.display.set_caption("( " + str(x) + ", " + str(y) + " )")

 if startGame is False:
         screen.blit(bgStart, (0, 0))
         levelOne.draw(500, 300)
         pygame.display.update()


 else:

         bgOne_y -= 15
         bgTwo_y -= 15
         bgThree_y -= 15

         if bgFour_y > 0:
             bgFour_y -= 15

         if bgOne_y <= -1 * 700:
             bgOne_y = bgFour_y + 700
         if bgTwo_y <= -1 * 700:
             bgTwo_y = bgOne_y + 700
         if bgThree_y <= -1 * 700:
             bgThree_y = bgTwo_y + 700

         screen.blit(bgOne, (0, bgOne_y))
         screen.blit(bgTwo, (0, bgTwo_y))
         screen.blit(bgThree, (0, bgThree_y))
         screen.blit(bgFour, (bgFour_x, bgFour_y))
         screen.blit(bgFive, (bgFive_x, bgFour_y))
         screen.blit(bgSix, (bgSix_x, bgFour_y))
         screen.blit(bgSeven, (bgSeven_x, bgFour_y))
         screen.blit(bgEight, (bgEight_x, bgFour_y))
         screen.blit(bgNine, (bgNine_x, bgFour_y))
         screen.blit(bgTen, (bgTen_x, bgFour_y))

         pygame.display.update()

         square.draw(screen)
         square.handle_keys()

         if bgFour_y == 0:
             bgFour_x -= 7
             bgFive_x -= 7
             bgSix_x -= 7
             bgSeven_x -= 7
             bgEight_x -= 7
             bgNine_x -= 7
             bgTen_x -= 7

             for j in jellos_list:
                 j.draw()
                 speed = random.randint(10, 12)
                 j.move(square, speed)

                 if j.isHit():
                     pygame.quit()
                     sys.exit()

         if bgNine_x < -100 or bgTen_x < 0:

             for p in purp_list:
                 p.draw()
                 speed = random.randint(2, 6)
                 p.move(speed, square)

                 if p.isisHit():
                     pygame.quit()
                     sys.exit()

             for pj in pretJ_list:
                 pj.draw()
                 speed = random.randint(4, 15)
                 pj.move(square, speed)

                 if pj.isisHit():
                     pygame.quit()
                     sys.exit()


         else:
             for t in tree_list:
                 t.draw(screen)
                 speed = random.randint(1, 20)
                 t.move(speed, square)
                 if t.isHit():
                     pygame.quit()
                     sys.exit()

         if bgNine_x < -1187:
                 bgNine_x += 2374

         if bgTen_x < -1187:
                 bgTen_x = bgNine_x + 1187

 pygame.display.update()

 clock.tick(40)
pygame.quit()
sys.exit()

