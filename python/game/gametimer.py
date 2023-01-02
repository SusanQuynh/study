from sys import pycache_prefix
import pygame
import time
pygame.init()
screen=pygame.display.set_mode((1280,790))
pygame.display.set_caption("Game")
running=True
clock=pygame.time.Clock()
lemonchiffon=(255,250,205)
BROWN=(255,248,220)
YELLOW=(0,0,0)
font=pygame.font.SysFont('sans',30)
mins=1
secs=1
l1=font.render('*******************************************************************************', True, YELLOW)
l2=font.render(' |                   |                  |                     |',True,YELLOW)
l3=font.render(' _________|________________.=""_;=.______________|_____________________|_______',True,YELLOW)
l4=font.render('|                   |  ,-"_,=""     `"=.|                  |',True,YELLOW)
l5=font.render('''|___________________|__"=._o`"-._        `"=.______________|___________________
''',True,YELLOW)
l6=font.render('''          |                `"=._o`"=._      _`"=._                     |
''',True,YELLOW)
l7=font.render(''' _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
''',True,YELLOW)
l8=font.render('''|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
''',True,YELLOW)
l9=font.render('''|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
''',True,YELLOW)
l10=font.render('''          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 ''',True,YELLOW)
l11=font.render('''_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
''',True,YELLOW)
l12=font.render('''|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
''',True,YELLOW)
l13=font.render('''|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
''',True,YELLOW)
l14=font.render('''____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
''',True,YELLOW)
l15=font.render('''/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
''',True,YELLOW)
l16=font.render('''____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
''',True,YELLOW)
l17=font.render('''/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
''',True,YELLOW)
l18=font.render('''____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
''',True,YELLOW)
l19=font.render('''/______/______/______/______/______/______/______/______/______/______/[TomekK]
''',True,YELLOW)
while running:
    clock.tick(60)
    screen.fill(lemonchiffon)
    screen.blit(l1,(10,5))
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip()
pygame.quit()