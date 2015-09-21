# -----------------------------------------------------------------------------
# File name: main.py                                                          #
# Date created: 3/20/2014                                                     #
# Date last modified: 1/18/2015                                               #
#                                                                             #
# Author: Tony Wu (Xiangbo)                                                   #
# Email: xb.wu@mail.utoronto.ca                                               #
#                                                                             #
# Python version: developed under 3.4, additionally tested under 2.7          #
# Dependencies: Pygame 1.9.2, rsclasses.py                                    #
#                                                                             #
# License: GNU GPL v2.0                                                       #
#                                                                             #
# Copyright (c) 2014-2015 [Tony Wu], All Right Reserved                       #
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    import pygame
    import sys
    import time
    import pygame.mixer
    from math import *
    from pygame.locals import *

    pygame.init()

    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

    # rscalsses.py must be present

    from rsclasses import *

    # Constants - use default value unless debugging

    HORI_RES = 800                              # Horizontal Resolution
    VERT_RES = 600                              # Vertical Resolution
    FONT = "timesnewroman"                      # Game font
    FPS = 60                                    # Frames-per-second

    # The following image asset files must present

    bg = "background.jpg"
    wstar = "whitestar.png"
    rstar = "redstar.png"
    ystar = "yellowstar.png"
    bstar = "bluestar.png"
    bkship1 = "minienemy1.png"
    pship = "pship.png"
    pshipfl = "pshipfirelaser.png"
    pshipfly = "pshipfly.png"
    pshipflyback = "pshipflyback.png"
    pro1 = "projectile1.png"
    pro1f = "projectile1flash.png"
    las1 = "laser1.png"
    lasr = "laserred.png"
    em1 = "enemy1.png"
    em2 = "enemy2.png"
    em3 = "enemy3.png"
    em3f = "enemy3fire.png"
    em4 = "enemy4.png"
    ex1 = "explosion.png"
    bs1 = "boss1.png"
    bs2 = "boss2.png"
    bs2shoot = "boss2shoot.png"
    bs3 = "boss3.png"
    bs4 = "boss4.png"
    bs4r = "boss4ram.png"
    bf = "bossfinalyellow.png"
    bfr = "bossfinal.png"
    isplash = "introsplash.jpg"
    isplash2 = "poweredbysource.jpg"
    sscreen = "startscreen.jpg"
    hscreen = "helpscreen.jpg"
    b1w = "boss1red.png"
    b2w = "boss2red.png"
    b2sw = "boss2shootred.png"
    b3w = "boss3red.png"
    b4w = "boss4red.png"
    hbar = "healthbar.png"
    ebar = "energybar.png"
    eunit = "energyunit.png"
    eunitred = "energyunitred.png"
    efire = "enginefire.png"
    efireb = "enginefireblue.png"
    menus = "menuselector.png"
    menusf = "menuselectorflash.png"
    creds = "creditscreen.jpg"
    dscreen = "deathscreen.jpg"
    efl = "enginefirelow.png"
    wscrn = "winscreen.png"

    # The following sound asset files must present

    introsound = pygame.mixer.Sound("introlow.wav")
    menutheme = pygame.mixer.Sound("menutheme.wav")
    bossfight = pygame.mixer.Sound("bossfight.wav")
    boss2fight = pygame.mixer.Sound("boss2theme.wav")
    explosionS = pygame.mixer.Sound("explosion.wav")
    laserFX = pygame.mixer.Sound("laserfx.wav")
    leveltheme = pygame.mixer.Sound("leveltheme.wav")
    boss3fight = pygame.mixer.Sound("boss3theme.wav")
    boss4fight = pygame.mixer.Sound("boss4theme.wav")
    bombFX = pygame.mixer.Sound("nuke.wav")
    explosionS.set_volume(0.15)
    laserFX.set_volume(1.0)

    # Setting up game window

    screen = pygame.display.set_mode((HORI_RES, VERT_RES), 0, 32)

    # Setting up fonts

    stdfont = pygame.font.SysFont(FONT, 24)
    stdfont_bold = pygame.font.SysFont(FONT, 24)
    stdfont_bold.set_bold(True)

    # Generating pygame surfaces

    # Stars

    background = pygame.image.load(bg).convert()
    whitestar = pygame.image.load(wstar).convert_alpha()
    redstar = pygame.image.load(rstar).convert_alpha()
    yellowstar = pygame.image.load(ystar).convert_alpha()
    bluestar = pygame.image.load(bstar).convert_alpha()

    # Ships and projectiles

    backgroundship1 = pygame.image.load(bkship1).convert_alpha()
    playership = pygame.image.load(pship).convert_alpha()
    playershipfirelaser = pygame.image.load(pshipfl).convert_alpha()
    playershipfly = pygame.image.load(pshipfly).convert_alpha()
    playershipflyback = pygame.image.load(pshipflyback).convert_alpha()
    rocket = pygame.image.load(pro1).convert_alpha()
    rocketflash = pygame.image.load(pro1f).convert_alpha()
    enemy1 = pygame.image.load(em1).convert_alpha()
    enemy2 = pygame.image.load(em2).convert_alpha()
    enemy3 = pygame.image.load(em3).convert_alpha()
    enemy3fire = pygame.image.load(em3f).convert_alpha()
    enemy4 = pygame.image.load(em4).convert_alpha()
    explosion = pygame.image.load(ex1).convert_alpha()
    boss1 = pygame.image.load(bs1).convert_alpha()
    boss2 = pygame.image.load(bs2).convert_alpha()
    boss2shoot = pygame.image.load(bs2shoot).convert_alpha()
    boss3 = pygame.image.load(bs3).convert_alpha()
    boss4 = pygame.image.load(bs4).convert_alpha()
    boss4ram = pygame.image.load(bs4r).convert_alpha()
    bossfinal = pygame.image.load(bf).convert_alpha()
    bossfinalred = pygame.image.load(bfr).convert_alpha()
    introsplash = pygame.image.load(isplash).convert()
    introsplash2 = pygame.image.load(isplash2).convert()
    startscreen = pygame.image.load(sscreen).convert()
    helpscreen = pygame.image.load(hscreen).convert()
    boss1white = pygame.image.load(b1w).convert_alpha()
    boss2white = pygame.image.load(b2w).convert_alpha()
    boss2shootwhite = pygame.image.load(b2sw).convert_alpha()
    boss3white = pygame.image.load(b3w).convert_alpha()
    boss4white = pygame.image.load(b4w).convert_alpha()
    laser1 = pygame.image.load(las1).convert_alpha()
    laserred = pygame.image.load(lasr).convert_alpha()
    laserredver = pygame.transform.rotate(pygame.image.load(lasr).
                                          convert_alpha(), 90)
    enginefire = pygame.image.load(efire).convert_alpha()
    enginefireblue = pygame.image.load(efireb).convert_alpha()
    enginefirebig = pygame.transform.scale2x(enginefire).convert_alpha()
    enginefirelow = pygame.image.load(efl).convert_alpha()

    # In-game UI

    ui_healthbar = pygame.image.load(hbar).convert_alpha()
    ui_energybar = pygame.image.load(ebar).convert_alpha()
    ui_energyunit = pygame.image.load(eunit).convert_alpha()
    ui_energyunitred = pygame.image.load(eunitred).convert_alpha()

    # Menu UI

    ui_menuselector = pygame.image.load(menus).convert_alpha()
    ui_menuselectorflash = pygame.image.load(menusf).convert_alpha()
    creditscreen = pygame.image.load(creds).convert()
    deathscreen = pygame.image.load(dscreen).convert()
    winscreen = pygame.image.load(wscrn).convert()

    clock = pygame.time.Clock()

    pause = False

    a = cstar(30, HORI_RES, VERT_RES)
    laser = claser()

    # For movement

    wkey = False
    akey = False
    skey = False
    dkey = False

    win = False

    # For missile weapon
    isfire = False

    # For laser weapon
    islaser = False

    timer = -400
    (ex, ey) = (0, 0)         # Used for temp store of explosion locations
    score = 0                 # Player's score

    hitinframe = False        # Used to trigger collision warning
    collidelabeldelay = 0

    stage = 0
    # 1 -- FIRST WAVE
    # 2 -- BOSS (#1)
    # 3 -- SECOND WAVE
    # 4 -- BOSS (#2)
    # 5 -- THIRD WAVE
    # 6 -- BOSS (#3)
    # 7 -- FOURTH WAVE
    # 8 -- BOSS (#4)

    quota = 0

    flash = 0

    # introsplash
    pygame.display.set_caption("REDSHIFT v1.1")

    introsound.set_volume(1.0)
    introsound.play()
    for i in range(0, 50):
        screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    for i in range(0, 240):
        screen.blit(introsplash, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    for i in range(0, 45):
        screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    for i in range(0, 180):
        screen.blit(introsplash2, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    for i in range(0, 30):
        screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    lab_start = stdfont_bold.render("START GAME", True, (0, 160, 80))
    lab_help = stdfont_bold.render("VIEW HELP", True, (0, 160, 80))
    lab_credits = stdfont_bold.render("CREDITS", True, (0, 160, 80))

    lab_start_red = stdfont_bold.render("START GAME", True, (200, 80, 80))
    lab_help_red = stdfont_bold.render("VIEW HELP", True, (200, 80, 80))
    lab_credits_red = stdfont_bold.render("CREDITS", True, (200, 80, 80))

    start = False

    men = C_Menu(1, 1, 0)

    menutheme.set_volume(0.15)
    menutheme.play()

    # A trigger variable for starting the game

    gamestart = False

    while not start:

        # This loop runs while in the main menu

        clock.tick(FPS)
        men.timer += 1

        if men.location == 1:
            screen.blit(startscreen, (0, 0))
        if men.location == 2:
            screen.blit(helpscreen, (0, 0))
        if men.location == 3:
            screen.blit(creditscreen, (0, 0))

        if men.location == 1:
            if men.point == 1:
                if men.timer % 6 < 3:
                    screen.blit(ui_menuselector, (305, 330))
                else:
                    screen.blit(ui_menuselectorflash, (305, 330))
            if men.point == 2:
                if men.timer % 6 < 3:
                    screen.blit(ui_menuselector, (305, 380))
                else:
                    screen.blit(ui_menuselectorflash, (305, 380))
            if men.point == 3:
                if men.timer % 6 < 3:
                    screen.blit(ui_menuselector, (305, 430))
                else:
                    screen.blit(ui_menuselectorflash, (305, 430))

        if men.location == 1:
            if men.point == 1:
                screen.blit(lab_start_red, (335, 330))
            else:
                screen.blit(lab_start, (335, 330))

            if men.point == 2:
                screen.blit(lab_help_red, (342, 380))
            else:
                screen.blit(lab_help, (342, 380))

            if men.point == 3:
                screen.blit(lab_credits_red, (359, 430))
            else:
                screen.blit(lab_credits, (359, 430))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if men.point < 3:
                        men.point += 1
                        laserFX.play()
                if event.key == K_UP:
                    if men.point > 1:
                        men.point -= 1
                        laserFX.play()
                if event.key == K_RETURN:
                    if men.point == 1:
                        start = True
                        menutheme.stop()
                        leveltheme.play()
                    if men.point == 2:
                        men.location = 2
                    if men.point == 3:
                        men.location = 3
                if event.key == K_ESCAPE:
                    if men.location == 2 or men.location == 3:
                        men.location = 1
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    playerobj = cplayer(100, 250, 100, 100)

    # Initializing messages

    getreadymessage1 = stdfont.render("The Battle Approaches...",
                                      True, (255, 255, 255))
    getreadymessage = stdfont.render("PREPARE YOURSELF!", True, (255, 255, 0))
    endmsg1 = stdfont.render("People die in war.", True, (0, 0, 0))
    endmsg2 = stdfont.render("Good night, sweet prince.", True, (0, 0, 0))

    # Initializing enemy objects

    e1 = cenemy1(HORI_RES, VERT_RES, 5)
    e2 = cenemy2(HORI_RES, VERT_RES, 3)
    e3 = cenemy3(HORI_RES, VERT_RES)
    b1 = cboss1(HORI_RES, VERT_RES)
    b2 = cboss2(HORI_RES, VERT_RES)
    e4 = cenemy4(HORI_RES, VERT_RES, 2)

    # Explosion object
    expobj = C_Explosion()

    # Detector
    detect = cDetect()

    # Main game loop
    while True:

        scorelabel = stdfont.render("Hits: " + str(score), True,
                                    (255, 255, 255))
        healthlabel = stdfont.render("Health: " + str(playerobj.health), True,
                                     (255, 255, 255))
        energylabel = stdfont.render("Energy: " + str(playerobj.energy), True,
                                     (225, 225, 255))
        collidelabel = stdfont_bold.render("Collision Detected!", True,
                                           (225, 0, 0))

        clock.tick(FPS)

        timer += 1

        if flash < 11:
            flash += 1

        # -----------------------------------------------------
        # start of stage control code

        # Starting the game after the initial delay

        if stage == 0 and timer > 0:
            stage = 1

        # Refreshing enemy 1 during STAGE 1 and STAGE 3

        # 2nd and 3rd instance of enemy type 1

        if stage == 1:
            if timer > 0:
                if not e1.death[0]:
                    e1.refresh(0)
                if e1.xpos[0] < -40:
                    e1.respawn(0)
            if timer > 60:
                if not e1.death[1]:
                    e1.refresh(1)
                if e1.xpos[1] < -40:
                    e1.respawn(1)
            if timer > 80:
                if not e1.death[2]:
                    e1.refresh(2)
                if e1.xpos[2] < -40:
                    e1.respawn(2)
            if timer > 100:
                if not e1.death[3]:
                    e1.refresh(3)
                if e1.xpos[3] < -40:
                    e1.respawn(3)
            if timer > 120:
                if not e1.death[4]:
                    e1.refresh(4)
                if e1.xpos[4] < -40:
                    e1.respawn(4)

        # When kill quota is reached in stage 1

        if stage == 1 and quota > 10:
            for ennum in range(0, 5):
                expobj.addexplosion(e1.xpos[ennum], e1.ypos[ennum])
            quota = 0
            b1 = cboss1(HORI_RES, VERT_RES)
            stage = 2
            leveltheme.stop()
            bossfight.play()

        # When boss1 dies during STAGE 2

        if stage == 2:
            b1.refresh()
            if b1.health < 1:
                stage = 3
                e1.respawn(0)
                e2.respawn(0)
                delay1 = 0
                bossfight.stop()
                leveltheme.play()

        # Refreshing enemy2 during STAGE 3

        if stage == 3:
            if not e1.death[0]:
                e1.refresh(0)
            if e1.xpos[0] < -40:
                e1.respawn(0)

            if not e2.death[0]:
                e2.refresh(0)
            if e2.xpos[0] < -40:
                e2.respawn(0)

            if delay1 < 76:
                delay1 += 1

            if delay1 == 50:
                e2.respawn(1)

            if delay1 == 75:
                e2.respawn(2)
                delay1 = 76

            if delay1 > 50:
                if not e2.death[1]:
                    e2.refresh(1)
                if e2.xpos[1] < -40:
                    e2.respawn(1)

            if delay1 > 75:
                if not e2.death[2]:
                    e2.refresh(2)
                if e2.xpos[2] < -40:
                    e2.respawn(2)

        # When kill quota is reached during STAGE 3

        if stage == 3 and quota > 10:
            expobj.addexplosion(e1.xpos[0], e1.ypos[0])
            for ennum in range(0, 3):
                expobj.addexplosion(e2.xpos[ennum], e2.ypos[ennum])
            quota = 0
            b2 = cboss2(HORI_RES, VERT_RES)
            stage = 4
            leveltheme.stop()
            boss2fight.play()

        # Refreshing boss2 during STAGE 4

        if stage == 4:
            b2.refresh()
            if b2.health < 1:
                stage = 5
                quota = 0
                e3.respawn()
                e2.respawn(0)
                boss2fight.stop()
                leveltheme.play()

        if stage == 5:
            if not e3.death:
                e3.refresh()
            if e3.xpos < -40:
                e3.respawn()
            if not e2.death[0]:
                e2.refresh(0)
            if e2.xpos[0] < -40:
                e2.respawn(0)
            if quota > 10:
                stage = 6
                quota = 0
                b3 = cboss3(HORI_RES, VERT_RES)
                leveltheme.stop()
                boss3fight.play()

        if stage == 6:
            b3.refresh()
            if b3.health < 1:
                quota = 0
                stage = 7
                delay1 = 0
                e4.respawn(0)
                boss3fight.stop()
                leveltheme.play()

        if stage == 7:
            if delay1 < 50:
                delay1 += 1
            if delay1 == 50:
                e4.respawn(1)
                delay1 = 51
            if not e4.death[0]:
                e4.refresh(0, playerobj.ypos)
            if e4.xpos[0] < -40:
                e4.respawn(0)
            if delay1 == 51:
                if not e4.death[1]:
                    e4.refresh(1, playerobj.ypos)
                if e4.xpos[1] < -40:
                    e4.respawn(1)
            if quota > 10:
                stage = 8
                quota = 0
                b4 = cboss4(HORI_RES, VERT_RES)
                leveltheme.stop()
                boss4fight.play()

        if stage == 8:
            b4.refresh()
            if b4.health < 1:
                stage = 9
                quota = 0
                e2.respawn(0)
                e3.respawn()
                e4.respawn(0)
                boss4fight.stop()
                leveltheme.play()

        if stage == 9:
            if not e2.death[0]:
                e2.refresh(0)
            if not e3.death:
                e3.refresh()
            if not e4.death[0]:
                e4.refresh(0, playerobj.ypos)
            if e2.xpos[0] < -40:
                e2.respawn(0)
            if e3.xpos < -40:
                e3.respawn()
            if e4.xpos[0] < -40:
                e4.respawn(0)
            if quota > 10:
                stage = 10
                quota = 0
                b5 = cbossf(HORI_RES, VERT_RES)
                bombFX.play()

        if stage == 10:
            b5.refresh()
            if b5.done:
                win = True

        # End of stage control code
        # -----------------------------------------------------

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    wkey = True
                if event.key == K_s:
                    skey = True
                if event.key == K_a:
                    akey = True
                if event.key == K_d:
                    dkey = True
                if (event.key == K_SPACE) and (not isfire):
                    r = cmissile(playerobj.xpos, playerobj.ypos)
                    isfire = True
                if event.key == K_p:
                    if playerobj.energy > 0:
                        laser.show = True
                        islaser = True

            if event.type == KEYUP:
                if event.key == K_w:
                    wkey = False
                if event.key == K_s:
                    skey = False
                if event.key == K_a:
                    akey = False
                if event.key == K_d:
                    dkey = False
                if event.key == K_p:
                    laser.show = False
                    islaser = False

        a.refresh()

        if playerobj.energy < 1:
            laser.show = False
            islaser = False

        if (not islaser) and playerobj.energy < 100:
            if timer % 3 == 0:
                playerobj.energy += 1

        if isfire:
            r.refresh()

        screen.blit(background, (0, 0))
        for n in range(0, 18):
            screen.blit(whitestar, (a.xcors[n], a.ycors[n]))
        for n in range(18, 21):
            screen.blit(redstar, (a.xcors[n], a.ycors[n]))
        for n in range(21, 24):
            screen.blit(yellowstar, (a.xcors[n], a.ycors[n]))
        for n in range(24, 28):
            screen.blit(bluestar, (a.xcors[n], a.ycors[n]))
        for n in range(28, 30):
            screen.blit(backgroundship1, (a.xcors[n], a.ycors[n]))

        # Ship movement

        if akey:
            playerobj.moveleft()
        if dkey:
            playerobj.moveright()
        if wkey:
            playerobj.moveup()
        if skey:
            playerobj.movedown()

        # Laser following

        laser.refresh(playerobj.xpos, playerobj.ypos+13)

        if (laser.show):
            if (timer % 6 == 0 or timer % 6 == 1 or timer % 6 == 2):
                screen.blit(laser1, (laser.xpos, laser.ypos))
            if (timer % 6 == 0):
                laserFX.play()

        # When missile hits

        if (isfire):
            if (r.death):
                isfire = False

        # Missiles is fired/Collision detection

        if (isfire or laser.show) and stage > 0:
            if isfire:
                if (timer % 4 < 2):
                    screen.blit(rocket, (r.xpos, r.ypos))
                else:
                    screen.blit(rocketflash, (r.xpos, r.ypos))
            if islaser:
                playerobj.energy -= 1
            if stage == 1:
                if isfire:
                    for ennum in range(0, 5):
                        if abs(r.xpos - e1.xpos[ennum]) < 20 and \
                           abs(r.ypos - e1.ypos[ennum] - 10) < 20:
                            e1.health[ennum] -= 10
                if islaser:
                    for ennum in range(0, 5):
                        if abs(laser.ypos - e1.ypos[ennum] - 10) < 20:
                            e1.health[ennum] -= 1
                for ennum in range(0, 5):
                    if e1.health[ennum] < 1:
                        expobj.addexplosion(e1.xpos[ennum], e1.ypos[ennum])
                        e1.death[ennum] = True
                        if isfire:
                            r.death = True
                        score += 1
                        quota += 1
                        if stage == 1:
                            e1.respawn(ennum)
                            e1.death[ennum] = False

            if stage == 2:
                if isfire:
                    if abs(r.xpos - b1.xpos) < 20 and \
                       abs(r.ypos - b1.ypos - 28) < 30:
                        b1.health -= 1
                        r.death = True
                        score += 1
                        flash = 0
                        expobj.addexplosion(b1.xpos, b1.ypos)

            if stage == 3:
                if isfire:
                    for ennum in range(0, 3):
                        if abs(r.xpos - e2.xpos[ennum]) < 20 and \
                           abs(r.ypos - e2.ypos[ennum] - 10) < 20:
                            e2.health[ennum] -= 15
                    if abs(r.xpos - e1.xpos[0]) < 20 and \
                       abs(r.ypos - e1.ypos[0] - 10) < 20:
                        e1.health[0] -= 10
                if islaser:
                    for ennum in range(0, 3):
                        if abs(laser.ypos - e2.ypos[ennum] - 10) < 20:
                            e2.health[ennum] -= 1
                    if abs(laser.ypos - e1.ypos[0] - 10) < 20:
                        e1.health[0] -= 1
                if e1.health[0] < 1:
                    expobj.addexplosion(e1.xpos[0], e1.ypos[0])
                    e1.death[0] = True
                    if isfire:
                        r.death = True
                    score += 1
                    quota += 1
                    if stage == 3:
                        e1.respawn(0)
                        e1.death[0] = False
                for ennum in range(0, 3):
                    if e2.health[ennum] < 1:
                        expobj.addexplosion(e2.xpos[ennum], e2.ypos[ennum])
                        e2.death[ennum] = True
                        r.death = True
                        score += 1
                        quota += 1
                        if stage == 3:
                            e2.respawn(ennum)
                            e2.death[ennum] = False

            if stage == 4:
                if isfire:
                    if abs(r.xpos - b2.xpos) < 20 and \
                       abs(r.ypos - b2.ypos - 28) < 30:
                        b2.health -= 1
                        r.death = True
                        score += 1
                        flash = 0
                        expobj.addexplosion(b2.xpos, b2.ypos)

            if stage == 5:
                if isfire:
                    if abs(r.xpos - e3.xpos) < 20 and \
                       abs(r.ypos - e3.ypos - 10) < 20:
                        e3.health -= 10
                    if abs(r.xpos - e2.xpos[0]) < 20 and \
                       abs(r.ypos - e2.ypos[0] - 10) < 20:
                        e2.health[0] -= 15
                if islaser:
                    if abs(laser.ypos - e3.ypos - 10) < 20:
                        e3.health -= 1
                    if abs(laser.ypos - e2.ypos[0] - 10) < 20:
                        e2.health[0] -= 1
                if e3.health < 1:
                        expobj.addexplosion(e3.xpos, e3.ypos)
                        e3.death = True
                        r.death = True
                        score += 1
                        quota += 1
                        if stage == 5:
                            e3.respawn()
                            e3.death = False
                if e2.health[0] < 1:
                        expobj.addexplosion(e2.xpos[0], e2.ypos[0])
                        e2.death[0] = True
                        r.death = True
                        score += 1
                        quota += 1
                        if stage == 5:
                            e2.respawn(0)
                            e2.death[0] = False
            if stage == 6:
                if isfire:
                    if abs(r.xpos - b3.xpos) < 40 and \
                       abs(r.ypos - b3.ypos - 70) < 40:
                        b3.health -= 1
                        r.death = True
                        score += 1
                        flash = 0
                        expobj.addexplosion(b3.xpos, b3.ypos + 30)

            if stage == 7:
                if isfire:
                    if abs(r.xpos - e4.xpos[0]) < 20 and \
                       bs(r.ypos - e4.ypos[0] - 10) < 20:
                        e4.health[0] -= 10
                    if abs(r.xpos - e4.xpos[1]) < 20 and \
                       abs(r.ypos - e4.ypos[1] - 10) < 20:
                        e4.health[1] -= 10
                if islaser:
                    if abs(laser.ypos - e4.ypos[0] - 10) < 20:
                        e4.health[0] -= 1
                    if abs(laser.ypos - e4.ypos[1] - 10) < 20:
                        e4.health[1] -= 1
                if e4.health[0] < 1:
                    expobj.addexplosion(e4.xpos[0], e4.ypos[0])
                    e4.death[0] = True
                    if isfire:
                        r.death = True
                    score += 1
                    quota += 1
                    if stage == 7:
                        e4.respawn(0)
                        e4.death[0] = False
                if e4.health[1] < 1:
                    expobj.addexplosion(e4.xpos[1], e4.ypos[1])
                    e4.death[1] = True
                    if isfire:
                        r.death = True
                    score += 1
                    quota += 1
                    if stage == 7:
                        e4.respawn(1)
                        e4.death[1] = False

            if stage == 8:
                if isfire:
                    if abs(r.xpos - b4.xpos) < 40 and \
                       abs(r.ypos - b4.ypos - 70) < 40:
                        b4.health -= 1
                        r.death = True
                        score += 1
                        flash = 0
                        expobj.addexplosion(b4.xpos, b4.ypos + 30)

            if stage == 9:
                if isfire:
                    if abs(r.xpos - e2.xpos[0]) < 20 and \
                       abs(r.ypos - e2.ypos[0] - 10) < 20:
                        e2.health[0] -= 15
                    if abs(r.xpos - e3.xpos) < 20 and \
                       abs(r.ypos - e3.ypos - 10) < 20:
                        e3.health -= 10
                    if abs(r.xpos - e4.xpos[0]) < 20 and \
                       abs(r.ypos - e4.ypos[0] - 10) < 20:
                        e4.health[0] -= 10
                if islaser:
                    if abs(laser.ypos - e2.ypos[0] - 10) < 20:
                        e2.health[0] -= 1
                    if abs(laser.ypos - e3.ypos - 10) < 20:
                        e3.health -= 1
                    if abs(laser.ypos - e4.ypos[0] - 10) < 20:
                        e4.health[0] -= 1
                if e2.health[0] < 1:
                        expobj.addexplosion(e2.xpos[0], e2.ypos[0])
                        e2.death[0] = True
                        r.death = True
                        score += 1
                        quota += 1
                        if stage == 9:
                            e2.respawn(0)
                            e2.death[0] = False
                if e4.health[0] < 1:
                    expobj.addexplosion(e4.xpos[0], e4.ypos[0])
                    e4.death[0] = True
                    if isfire:
                        r.death = True
                    score += 1
                    quota += 1
                    if stage == 9:
                        e4.respawn(0)
                        e4.death[0] = False
                if e3.health < 1:
                        expobj.addexplosion(e3.xpos, e3.ypos)
                        e3.death = True
                        r.death = True
                        score += 1
                        quota += 1
                        if stage == 9:
                            e3.respawn()
                            e3.death = False

        # When explosion happens

        if stage > 0:
            expobj.refresh()

        if expobj.hasexplosion():
            for i in range(expobj.numofexplosion):
                screen.blit(explosion,
                            (expobj.ongoingxp[i][0],
                             expobj.ongoingxp[i][1] - 20))
                explosionS.play()

        # Rendering enemies during stage 1
        if stage == 1:
            # 5 instances of interceptor
            for ennum in range(0, 5):
                if not e1.death[ennum]:
                    screen.blit(enemy1, (e1.xpos[ennum], e1.ypos[ennum]))
                    if timer % 4 < 2:
                        screen.blit(enginefire,
                                    (e1.xpos[ennum] + 43, e1.ypos[ennum] + 20))
                        screen.blit(enginefire,
                                    (e1.xpos[ennum] + 43, e1.ypos[ennum]))

        # Rendering enemies during stage 3
        if stage == 3:
            # 1 instance of interceptor
            if not e1.death[0]:
                screen.blit(enemy1, (e1.xpos[0], e1.ypos[0]))
                if timer % 4 < 2:
                    screen.blit(enginefire, (e1.xpos[0] + 43, e1.ypos[0] + 20))
                    screen.blit(enginefire, (e1.xpos[0] + 43, e1.ypos[0]))
            # 3 instances of wave
            for ennum in range(0, 3):
                if not e2.death[ennum]:
                    screen.blit(enemy2, (e2.xpos[ennum], e2.ypos[ennum]))
                    if timer % 4 < 2:
                        screen.blit(enginefirebig,
                                    (e2.xpos[ennum] + 38, e2.ypos[ennum] + 4))

        # print player ship
        if not laser.show:
            if dkey:
                screen.blit(playershipfly,
                            (playerobj.xpos, playerobj.ypos))
            else:
                if akey:
                    screen.blit(playershipflyback,
                                (playerobj.xpos, playerobj.ypos))
                else:
                    screen.blit(playership,
                                (playerobj.xpos, playerobj.ypos))
        else:
            screen.blit(playershipfirelaser,
                        (playerobj.xpos, playerobj.ypos))

        if wkey or akey or skey or dkey:
            if timer % 4 < 2:
                screen.blit(enginefire, (playerobj.xpos, playerobj.ypos - 3))
                screen.blit(enginefire, (playerobj.xpos, playerobj.ypos + 18))
        else:
            if timer % 7 < 3:
                screen.blit(enginefirelow,
                            (playerobj.xpos, playerobj.ypos - 3))
                screen.blit(enginefirelow,
                            (playerobj.xpos, playerobj.ypos + 18))

        # Rendering the first boss during the first boss fight (stage 2)
        if stage == 2:
            if b1.xpos < 555:
                if timer % 4 < 2:
                    if b1.direction == 4 or b1.direction == 7:
                        screen.blit(enginefire, (b1.xpos + 50, b1.ypos + 0))
                    if b1.direction == 1:
                        screen.blit(enginefire, (b1.xpos + 50, b1.ypos + 55))
                    if b1.direction == 2:
                        screen.blit(enginefirebig,
                                    (b1.xpos + 71, b1.ypos + 20))
                        screen.blit(laserredver, (b1.xpos + 40, 0))
                    if b1.direction == 5:
                        screen.blit(enginefirebig,
                                    (b1.xpos + 71, b1.ypos + 20))
                        screen.blit(laserredver, (b1.xpos + 40, 0))
                    if b1.direction == 8:
                        screen.blit(enginefirebig,
                                    (b1.xpos + 71, b1.ypos + 20))
                        screen.blit(laserredver, (b1.xpos + 40, 0))
            else:
                if timer % 4 < 2:
                    screen.blit(enginefirebig, (b1.xpos + 71, b1.ypos + 20))
            if flash > 10:
                screen.blit(boss1, (b1.xpos, b1.ypos))
            else:
                screen.blit(boss1white, (b1.xpos, b1.ypos))

        if stage == 4:
            if b2.limit < 50 and b2.limit > 10:
                if timer % 6 < 3:
                    screen.blit(laserred, (-390, b2.ypos + 34))
                if flash > 10:
                    screen.blit(boss2shoot, (b2.xpos, b2.ypos))
                else:
                    screen.blit(boss2shootwhite, (b2.xpos, b2.ypos))
            else:
                if flash > 10:
                    screen.blit(boss2, (b2.xpos, b2.ypos))
                else:
                    screen.blit(boss2white, (b2.xpos, b2.ypos))
            if timer % 4 < 2:
                screen.blit(enginefireblue, (b2.xpos + 50, b2.ypos + 3))
                screen.blit(enginefireblue, (b2.xpos + 56, b2.ypos + 28))
                screen.blit(enginefireblue, (b2.xpos + 50, b2.ypos + 53))

        if stage == 5:
            if not e2.death[0]:
                screen.blit(enemy2, (e2.xpos[0], e2.ypos[0]))
                if timer % 4 < 2:
                    screen.blit(enginefirebig,
                                (e2.xpos[0] + 38, e2.ypos[0] + 4))
            if not e3.death:
                if e3.delay < 50 and e3.delay > 10:
                    screen.blit(enemy3fire, (e3.xpos, e3.ypos))
                    if (timer % 6 == 0 or timer % 6 == 1 or timer % 6 == 2):
                        screen.blit(laserred, (e3.xpos-HORI_RES, e3.ypos + 16))
                else:
                    screen.blit(enemy3, (e3.xpos, e3.ypos))
                if timer % 4 < 2:
                    screen.blit(enginefire, (e3.xpos + 45, e3.ypos - 1))
                    screen.blit(enginefire, (e3.xpos + 45, e3.ypos + 22))

        if stage == 6:
            if b3.fire:
                if (timer % 6 == 0 or timer % 6 == 1 or timer % 6 == 2):
                    screen.blit(laserred, (b3.xpos - 780, b3.ypos + 15))
                else:
                    screen.blit(laserred, (b3.xpos - 780, b3.ypos + 91))
            if flash > 10:
                screen.blit(boss3, (b3.xpos, b3.ypos))
            else:
                screen.blit(boss3white, (b3.xpos, b3.ypos))
            if timer % 4 < 2:
                screen.blit(enginefire, (b3.xpos + 94, b3.ypos + 15))
                screen.blit(enginefire, (b3.xpos + 94, b3.ypos + 80))
                screen.blit(enginefireblue, (b3.xpos + 20, b3.ypos + 20))
                screen.blit(enginefireblue, (b3.xpos + 20, b3.ypos + 75))
                screen.blit(enginefireblue, (b3.xpos + 60, b3.ypos + 48))
                screen.blit(enginefirebig, (b3.xpos + 90, b3.ypos + 40))

        if stage == 7:
            if not e4.death[0]:
                screen.blit(enemy4, (e4.xpos[0], e4.ypos[0]))
                if timer % 4 < 2:
                    screen.blit(enginefire, (e4.xpos[0] + 43, e4.ypos[0] + 20))
                    screen.blit(enginefire, (e4.xpos[0] + 43, e4.ypos[0]))
            if not e1.death[1]:
                screen.blit(enemy4, (e4.xpos[1], e4.ypos[1]))
                if timer % 4 < 2:
                    screen.blit(enginefire, (e4.xpos[1] + 43, e4.ypos[1] + 20))
                    screen.blit(enginefire, (e4.xpos[1] + 43, e4.ypos[1]))

        if stage == 8:
            if timer % 4 < 2:
                screen.blit(enginefireblue, (b4.xpos + 96, b4.ypos - 1))
                screen.blit(enginefireblue, (b4.xpos + 96, b4.ypos + 75))
                screen.blit(enginefireblue, (b4.xpos + 96, b4.ypos + 20))
                screen.blit(enginefireblue, (b4.xpos + 96, b4.ypos + 96))
                screen.blit(enginefirebig, (b4.xpos + 91, b4.ypos + 40))
            if b4.direction == 2 or b4.direction == 5:
                if flash > 10:
                    screen.blit(boss4ram, (b4.xpos, b4.ypos))
                else:
                    screen.blit(boss4white, (b4.xpos, b4.ypos))
            else:
                if flash > 10:
                    screen.blit(boss4, (b4.xpos, b4.ypos))
                else:
                    screen.blit(boss4white, (b4.xpos, b4.ypos))

        if stage == 9:
            if not e2.death[0]:
                screen.blit(enemy2, (e2.xpos[0], e2.ypos[0]))
                if timer % 4 < 2:
                    screen.blit(enginefirebig,
                                (e2.xpos[0] + 38, e2.ypos[0] + 4))
            if not e3.death:
                if e3.delay < 50 and e3.delay > 10:
                    screen.blit(enemy3fire, (e3.xpos, e3.ypos))
                    if timer % 4 < 2:
                        screen.blit(laserred, (e3.xpos-HORI_RES, e3.ypos+16))
                else:
                    screen.blit(enemy3, (e3.xpos, e3.ypos))
                if timer % 4 < 2:
                    screen.blit(enginefire, (e3.xpos + 45, e3.ypos - 1))
                    screen.blit(enginefire, (e3.xpos + 45, e3.ypos + 22))
            if not e4.death[0]:
                screen.blit(enemy4, (e4.xpos[0], e4.ypos[0]))
                if timer % 4 < 2:
                    screen.blit(enginefire, (e4.xpos[0] + 43, e4.ypos[0] + 20))
                    screen.blit(enginefire, (e4.xpos[0] + 43, e4.ypos[0]))

        if stage == 10:
            if timer % 30 > 1 and timer % 30 < 15:
                screen.blit(bossfinal, (b5.xpos, b5.ypos))
            else:
                screen.blit(bossfinalred, (b5.xpos, b5.ypos))

        # Detects if player is in contact with enemy1
        if (stage == 1):
            for ennum in range(0, 5):
                if not e1.death[ennum]:
                    if (detect.isColli(playerobj.xpos, playerobj.ypos,
                                       playerobj.ocxpos, playerobj.ocypos,
                                       e1.xpos[ennum], e1.ypos[ennum],
                                       e1.ocxpos[ennum], e1.ocypos[ennum])):
                        playerobj.health -= 1
                        hitinframe = True

        if (not e1.death[0]) and (stage == 3):
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               e1.xpos[0], e1.ypos[0], e1.ocxpos[0],
                               e1.ocypos[0])):
                playerobj.health -= 1
                hitinframe = True

        # Detects if player is in contact with boss1

        if stage == 2:
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               b1.xpos, b1.ypos, b1.ocxpos, b1.ocypos)):
                playerobj.health -= 1
                hitinframe = True
            elif b1.direction == 2 or b1.direction == 5 or b1.direction == 8:
                if (detect.isColli(playerobj.xpos, playerobj.ypos,
                                   playerobj.ocxpos, playerobj.ocypos,
                                   b1.xpos + 40, 0, b1.xpos + 41, VERT_RES)):
                    playerobj.health -= 1
                    hitinframe = True

        # Detects if player is in contact with enemy2

        if (stage == 3 or stage == 5 or stage == 9) and (e2.death[0] == False):
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               e2.xpos[0], e2.ypos[0], e2.ocxpos[0],
                               e2.ocypos[0])):
                playerobj.health -= 2
                hitinframe = True

        if stage == 3 and (not e2.death[1]):
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               e2.xpos[1], e2.ypos[1], e2.ocxpos[1],
                               e2.ocypos[1])):
                playerobj.health -= 2
                hitinframe = True

        if stage == 3 and e2.death[2] == False:
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               e2.xpos[2], e2.ypos[2], e2.ocxpos[2],
                               e2.ocypos[2])):
                playerobj.health -= 2
                hitinframe = True

        # Detects if player is in contact with boss2

        if stage == 4:
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               b2.xpos, b2.ypos, b2.ocxpos, b2.ocypos)):
                playerobj.health -= 1
                hitinframe = True
            if b2.limit < 50 and b2.limit > 10:
                if abs(playerobj.ypos - b2.ypos - 25) < 30 \
                   and playerobj.xpos < b2.xpos:
                    playerobj.health -= 1
                    hitinframe = True

        # Detects contact with sniper's beam

        if stage == 5 or stage == 9:
            if e3.delay < 50 and e3.delay > 10:
                if abs(playerobj.ypos - e3.ypos - 15) < 30:
                    playerobj.health -= 1
                    hitinframe = True

        # Detects contact with boss3

        if stage == 6:
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               b3.xpos, b3.ypos, b3.ocxpos, b3.ocypos)):
                playerobj.health -= 1
                hitinframe = True
            if b3.fire:
                if (abs(playerobj.ypos - b3.ypos)) < 6 or \
                   (abs(playerobj.ypos - b3.ypos - 76)) < 6:
                    playerobj.health -= 1
                    hitinframe = True

        # Detects contact with tracker

        if (not e4.death[0]) and (stage == 7 or stage == 9):
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               e4.xpos[0], e4.ypos[0], e4.ocxpos[0],
                               e4.ocypos[0])):
                playerobj.health -= 1
                hitinframe = True

        if (not e4.death[1]) and stage == 7:
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               e4.xpos[1], e4.ypos[1], e4.ocxpos[1],
                               e4.ocypos[1])):
                playerobj.health -= 1
                hitinframe = True

        # Detects contact with boss 4

        if stage == 8:
            if (detect.isColli(playerobj.xpos, playerobj.ypos,
                               playerobj.ocxpos, playerobj.ocypos,
                               b4.xpos, b4.ypos, b4.ocxpos, b4.ocypos)):
                playerobj.health -= 1
                hitinframe = True

        if playerobj.health < 1:
            ender = False
            while not ender:
                screen.blit(deathscreen, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            pygame.quit()
            sys.exit()

        if win:
            screen.blit(winscreen, (0, 0))
            pygame.display.update()
            ender = False
            a = 0
            while not ender:
                clock.tick(FPS)
                a += 1
                if a > 90:
                    screen.blit(endmsg1, (100, 150))
                if a > 180:
                    screen.blit(endmsg2, (200, 350))
                if a > 270:
                    screen.blit(endtime, (400, 250))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            pygame.quit()
            sys.exit()

        # --------------------------------------------------------------------
        # Start of game UI code

        truetime = float(timer / 6)
        truetime = truetime / 10

        if truetime >= 0:
            lab_clock = stdfont.render("Time: " + str(int(floor(truetime))),
                                       True, (255, 255, 255))
        else:
            lab_clock = stdfont.render("Time: 0", True, (255, 255, 255))
        screen.blit(lab_clock, (140, 30))
        endtime = stdfont.render("Your clear time was " +
                                 str(int(floor(truetime))) +
                                 " seconds.", True, (0, 0, 0))

        if hitinframe:
            screen.blit(collidelabel, (230, 55))
            collidelabeldelay += 1
            if collidelabeldelay > 30:
                hitinframe = False
                collidelabeldelay = 0

        if timer < 0:
            screen.blit(getreadymessage1, (300, 260))

        if timer > -200 and timer < 0:
            screen.blit(getreadymessage, (300, 300))

        screen.blit(scorelabel, (30, 30))
        screen.blit(ui_healthbar, (400, 0))
        for i in range(0, int(floor(playerobj.health/5))):
            if playerobj.health > 33:
                screen.blit(ui_energyunit, (513 + i * 12, 12))
            else:
                screen.blit(ui_energyunitred, (513 + i * 12, 12))
        screen.blit(ui_energybar, (200, 555))
        for i in range(0, int(floor(playerobj.energy / 5))):
            if playerobj.energy > 33:
                screen.blit(ui_energyunit, (313 + i * 12, 570))
            else:
                screen.blit(ui_energyunitred, (313 + i * 12, 570))

        # End of game UI code
        # --------------------------------------------------------------------

        pygame.display.update()
