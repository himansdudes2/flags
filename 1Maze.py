import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800, 800))

done = False
x = 30
y = 30
x1 = 720
y1 = 30
clock = pygame.time.Clock()
ts1 = time.time()
ts2 = time.time()
tol1 =0
tol2 =0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True




    pressed = pygame.key.get_pressed()
    pressed2 = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y +=3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    if pressed2[pygame.K_w]: y1 -=3
    if pressed2[pygame.K_s]: y1 += 3
    if pressed2[pygame.K_a]: x1 -= 3
    if pressed2[pygame.K_d]: x1 += 3

    screen.fill((0, 0, 0))
    Font = pygame.font.SysFont("comicsansms", 70, True, True)
    Title = Font.render("Maze Finder", True, (255, 255, 255))
    screen.blit(Title, (190, 350))

    rec1 = pygame.draw.rect(screen, (0, 0, 200), pygame.Rect(x, y, 50, 50))  #Φτιάχνει τετράγωνο στο screen με χρώμα 0,128,55 που βρίσκεται σε θέσεις x,y και έχει μήκος πλάτος 60



    rec2 = pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(x1, y1, 50, 50))
    wu = pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(0, 0, 800, 20))
    wr = pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(780, 0, 20, 800))
    wd = pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(0, 780, 800, 20))
    wl = pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(0, 0, 20, 800))

    wm1 = pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(200, 50, 50, 300))
    wm2 = pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(380, 450, 50, 300))
    wm3 = pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(550, 50, 50, 300))
    psq = pygame.draw.rect(screen, (200, 0, 150), pygame.Rect(370, 50, 70, 70))

    if rec1.colliderect(wu): y += 3
    if rec1.colliderect(wd): y -= 3
    if rec1.colliderect(wr): x -= 3
    if rec1.colliderect(wl): x += 3

    if rec2.colliderect(wu): y1 +=3
    if rec2.colliderect(wd): y1 -=3
    if rec2.colliderect(wr): x1 -= 3
    if rec2.colliderect(wl): x1 += 3

    if rec1.colliderect(wm1) or rec1.colliderect(wm3):
        if pressed[pygame.K_UP]: y += 3
        if pressed[pygame.K_LEFT]: x += 3
        if pressed[pygame.K_RIGHT]: x -= 3

    if rec2.colliderect(wm1) or rec2.colliderect(wm3):
        if pressed[pygame.K_w]: y1 += 3
        if pressed[pygame.K_a]: x1 += 3
        if pressed[pygame.K_d]: x1 -= 3

    if rec1.colliderect(wm2) or rec2.colliderect(wm2):
        if pressed[pygame.K_DOWN]: y -= 3
        if pressed[pygame.K_LEFT]: x += 3
        if pressed[pygame.K_RIGHT]: x -= 3

        if pressed[pygame.K_s]: y1 -= 3
        if pressed[pygame.K_a]: x1 += 3
        if pressed[pygame.K_d]: x1 -= 3

    if rec1.colliderect(rec2):
        x = 30
        y = 30
        x1 = 720
        y1 = 30

    if rec1.colliderect(psq):
        x =30
        y =30
        te1 = time.time()
        tol1 = round(te1 - ts1, 2)
        ts1 = time.time()

    if rec2.colliderect(psq):
        x1 =720
        y1 =30
        te2 = time.time()
        tol2 = round(te2 - ts2, 2)
        ts2 = time.time()

    Font1 = pygame.font.SysFont("comicsansms", 20, True, True)
    Time1 = Font1.render("Time for blue:" + str(tol1), True, (0, 0, 255))
    screen.blit(Time1, (50, 650))

    Font2 = pygame.font.SysFont("comicsansms", 20, True, True)
    Time2 = Font2.render("Time for green:"+ str(tol2), True, (0, 255, 0))
    screen.blit(Time2, (560, 650))


    pygame.display.flip()
    clock.tick(60)