# -----------------------------------------------------------------------------
# File name: rsclasses.py                                                     #
# Date created: 3/20/2014                                                     #
# Date last modified: 1/18/2015                                               #
#                                                                             #
# Author: Tony Wu (Xiangbo)                                                   #
# Email: xb.wu@mail.utoronto.ca                                               #
#                                                                             #
# Python version: developed under 3.4, additionally tested under 2.7          #
# Dependencies: None                                                          #
#                                                                             #
# License: GNU GPL v2.0                                                       #
#                                                                             #
# Copyright (c) 2014-2015 [Tony Wu], All Right Reserved                       #
# -----------------------------------------------------------------------------


class cDetect:

    # This class is used for collision detection

    def isColli(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        '''(int,int,int,int,int,int,int,int) -> bool
        Intakes the int coordinates of two object inheriting from the
        "freebody" class.
        Returns True if the two objects collide.
        Else, return False.
        This functions is used to calculate collision
        '''

        if (ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1):
            return True
        else:
            return False


class C_Menu:

    # Stores some variables used by the main menu

    def __init__(self, location, point, timer):
        # location is the page within the menu (help screen, credits, etc.)
        self.location = location
        # point is where the selector is location
        self.point = point
        # timer is just an int for the selector
        self.timer = timer


class cfreebody:

    # This class contains location data

    xpos = 0
    ypos = 0
    ocxpos = 0
    ocypos = 0
    xmax = 800
    ymax = 600


class C_Explosion(cfreebody):

    # This class stores information about ongoing explosions to be rendered
    # Explosions are kept for 20 refresh cycles before they are moved
    # Example:
    # [[xpos1,ypos1,timeleft],[xpos2,ypos2,timeleft]]

    def __init__(self):
        self.ongoingxp = []
        self.numofexplosion = 0

    def addexplosion(self, xpos, ypos):
        '''(int, int) -> NoneType
        Adds an explosion at the specified coordinate.
        Returns None.
        '''

        self.ongoingxp.append([xpos, ypos, 20])
        self.numofexplosion += 1

    def hasexplosion(self):
        '''(NoneType) -> bool
        Returns True if there are explosions going on, else, returns False.
        '''

        if self.numofexplosion > 0:
            return True
        else:
            return False

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns None.
        '''

        counter = 0
        while counter < self.numofexplosion:
            if self.ongoingxp[counter][2] > 0:
                self.ongoingxp[counter][2] -= 1
            else:
                self.ongoingxp.pop(counter)
                self.numofexplosion -= 1
                # This is required to compensate for list.pop()
                counter -= 1
            counter += 1


class cship(cfreebody):

    # This class is used by all ships

    health = 0


class cplayer(cship):

    # This class is used for the player's ship

    # The size of the sprite used in pixels, used to calculate collision

    SPRITESIZE_X = 50
    SPRITESIZE_Y = 30

    # Player energy

    energy = 0

    def __init__(self, xpos, ypos, health, energy):
        # USAGE: XPOSITION, YPOSITION, HEALTH, ENERGY
        self.xpos = xpos
        self.ypos = ypos
        self.ocxpos = xpos + self.SPRITESIZE_X
        self.ocypos = ypos + self.SPRITESIZE_Y
        self.health = health
        self.energy = energy

    def moveup(self):
        '''(NoneType) -> NoneType
        Used for ship movement upward.
        Returns NoneType.
        '''
        if self.ypos > 40:
            self.ypos -= 5
            self.ocypos -= 5

    def movedown(self):
        '''(NoneType) -> NoneType
        Used for ship movement downward.
        Returns NoneType.
        '''
        if self.ypos < 560:
            self.ypos += 5
            self.ocypos += 5

    def moveleft(self):
        '''(NoneType) -> NoneType
        Used for ship movement left.
        Returns NoneType.
        '''
        if self.xpos > 40:
            self.xpos -= 5
            self.ocxpos -= 5

    def moveright(self):
        '''(NoneType) -> NoneType
        Used for ship movement right.
        Returns NoneType.
        '''
        if self.xpos < 760:
            self.xpos += 5
            self.ocxpos += 5


class cmissile(cfreebody):

    # This class is used for the missile that the player fires

    rang = 0
    death = False

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos + 11
        self.death = False

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''
        self.xpos = self.xpos + 10
        self.rang = self.rang + 1
        if self.rang > 25:
            self.death = True


class cenemy1(cship):

    # This class is used by type 1 enemies

    death = []
    health = []
    xpos = []
    ypos = []
    ocxpos = []
    ocypos = []

    SPRITESIZE_X = 50
    SPRITESIZE_Y = 36

    def __init__(self, xmax, ymax, number):
        import random
        self.xmax = xmax
        self.ymax = ymax
        for i in range(0, number):
            self.xpos.append(xmax)
            self.health.append(10)
            random.seed()
            randomy = random.randint(30, (self.ymax-30))
            self.ypos.append(randomy)
            self.ocxpos.append(xmax + self.SPRITESIZE_X)
            self.ocypos.append(randomy + self.SPRITESIZE_Y)
            self.death.append(False)

    def refresh(self, i):
        '''(int) -> NoneType
        The int parameter is the designation of the specific enemy
        being refreshed.
        Returns NoneType.
        '''
        self.xpos[i] = self.xpos[i] - 4
        self.ocxpos[i] = self.xpos[i] + self.SPRITESIZE_X

    def respawn(self, i):
        '''(int) -> NoneType
        The int parameter is the designation of the specific enemy
        being respawned.
        Returns NoneType.
        '''
        import random
        self.health[i] = 10
        random.seed()
        self.xpos[i] = self.xmax
        self.ocxpos[i] = self.xmax + self.SPRITESIZE_X
        randomy = random.randint(30, (self.ymax-30))
        self.ypos[i] = randomy
        self.ocypos[i] = randomy + self.SPRITESIZE_Y


class cenemy2(cship):

    # This class is used by type 2 enemy

    death = []
    health = []
    xpos = []
    ypos = []
    ocxpos = []
    ocypos = []

    SPRITESIZE_X = 50
    SPRITESIZE_Y = 36

    def __init__(self, xmax, ymax, number):
        import random
        self.xmax = xmax
        self.ymax = ymax
        for i in range(0, number):
            self.xpos.append(xmax)
            self.ocxpos.append(xmax + self.SPRITESIZE_X)
            self.health.append(15)
            random.seed()
            randomy = random.randint(30, (self.ymax-200))
            self.ypos.append(randomy)
            self.ocypos.append(randomy + self.SPRITESIZE_Y)
            self.death.append(False)

    def refresh(self, i):
        '''(int) -> NoneType
        The int parameter is the designation of the specific enemy
        being refreshed.
        Returns NoneType.
        '''

        import math
        self.xpos[i] -= 3
        self.ocxpos[i] = self.xpos[i] + self.SPRITESIZE_X
        self.ypos[i] += 5 * (math.sin((self.xpos[i]) / 50))
        self.ocypos[i] = self.ypos[i] + self.SPRITESIZE_Y

    def respawn(self, i):
        '''(int) -> NoneType
        The int parameter is the designation of the specific enemy
        being respawned.
        Returns NoneType.
        '''

        self.health[i] = 15
        import random
        random.seed()
        self.xpos[i] = self.xmax
        self.ocxpos[i] = self.xpos[i] + self.SPRITESIZE_X
        self.ypos[i] = random.randint(30, (self.ymax - 200))
        self.ocypos[i] = self.ypos[i] + self.SPRITESIZE_Y


class cenemy3(cship):

    # This class is used by type 3 enemies

    death = False
    delay = 0

    SPRITESIZE_X = 50
    SPRITESIZE_Y = 36

    def __init__(self, xmax, ymax):
        self.health = 20
        import random
        random.seed()
        self.xmax = xmax
        self.ymax = ymax
        self.xpos = xmax
        self.ypos = random.randint(50, (self.ymax - 50))
        self.death = False
        self.delay = 60
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''

        if self.xpos > (self.xmax - 150):
            self.xpos -= 1
        elif self.delay > 1:
            self.delay -= 1
        elif self.delay == 1:
            self.xpos -= 5
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y

    def respawn(self):
        '''(NoneType) -> Nonetype
        Used to respawn the enemy.
        Returns NoneType.
        '''
        self.health = 20
        import random
        random.seed()
        self.xpos = self.xmax
        self.ypos = random.randint(50, (self.ymax - 50))
        self.delay = 60
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y


class cenemy4(cship):

    # This class is used by type 4 enemies

    death = []
    health = []
    xpos = []
    ypos = []
    ocxpos = []
    ocypos = []

    SPRITESIZE_X = 50
    SPRITESIZE_Y = 36

    def __init__(self, xmax, ymax, number):
        import random
        self.xmax = xmax
        self.ymax = ymax
        for i in range(0, number):
            self.xpos.append(xmax)
            self.health.append(10)
            random.seed()
            randomy = (random.randint(30, (self.ymax - 30)))
            self.ypos.append(randomy)
            self.ocxpos.append(xmax + self.SPRITESIZE_X)
            self.ocypos.append(randomy + self.SPRITESIZE_Y)
            self.death.append(False)

    def refresh(self, i, target):
        '''(int, int) -> NoneType
        The first int parameter is the designation of the specific enemy
        being refreshed. The second int parameter is the y coordinate of the
        player.
        Returns NoneType
        '''
        self.xpos[i] = self.xpos[i] - 5
        if self.ypos[i] < target:
            self.ypos[i] += 2
        else:
            self.ypos[i] -= 2
        self.ocxpos[i] = self.xpos[i] + self.SPRITESIZE_X
        self.ocypos[i] = self.ypos[i] + self.SPRITESIZE_Y

    def respawn(self, i):
        '''(int) -> NoneType
        The int parameter is the designation of the specific enemy
        being respawned.
        Returns NoneType.
        '''

        import random
        self.health[i] = 10
        random.seed()
        self.xpos[i] = self.xmax
        self.ypos[i] = random.randint(30, (self.ymax - 30))
        self.ocxpos[i] = self.xpos[i] + self.SPRITESIZE_X
        self.ocypos[i] = self.ypos[i] + self.SPRITESIZE_Y


class cboss1(cship):

    # This class is used for the first boss

    SPRITESIZE_X = 75
    SPRITESIZE_Y = 70

    direction = 1

    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.xpos = xmax
        self.ypos = 300
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y
        self.health = 30

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''

        if self.xpos < 550:
            if self.direction == 1:
                self.ypos -= 2
                if self.ypos < 100:
                    self.direction = 2
            if self.direction == 2:
                self.xpos -= 7
                if self.xpos < 200:
                    self.direction = 3
            if self.direction == 3:
                self.xpos += 6
                if self.xpos > 550:
                    self.direction = 4
            if self.direction == 4:
                self.ypos += 2
                if self.ypos > 275:
                    self.direction = 5
            if self.direction == 5:
                self.xpos -= 7
                if self.xpos < 200:
                    self.direction = 6
            if self.direction == 6:
                self.xpos += 6
                if self.xpos > 550:
                    self.direction = 7
            if self.direction == 7:
                self.ypos += 2
                if self.ypos > 450:
                    self.direction = 8
            if self.direction == 8:
                self.xpos -= 7
                if self.xpos < 200:
                    self.direction = 9
            if self.direction == 9:
                self.xpos += 6
                if self.xpos > 550:
                    self.direction = 1

        else:
            self.xpos -= 1
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y


class cboss2(cship):

    # This class is used for the second boss

    SPRITESIZE_X = 75
    SPRITESIZE_Y = 70

    direction = 1
    limit = 60

    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.xpos = xmax
        self.ypos = 300
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y
        self.health = 30
        self.direction = 0
        self.limit = 60
        self.target = 100

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''

        if self.direction == 0:
            self.xpos -= 1
            if self.xpos < 600:
                self.direction = 1

        if self.direction == 1:
            if self.xpos > 400:
                self.xpos -= 3
            else:
                self.direction = 2
        if self.direction == 2:
            if self.limit > 0:
                self.limit -= 1
            else:
                self.limit = 60
                self.direction = 3
        if self.direction == 3:
            if self.xpos < (self.xmax - 100):
                self.xpos += 4
            else:
                self.direction = 4
        if self.direction == 4:
            import random
            random.seed()
            self.target = random.randint(100, self.ymax - 150)
            self.direction = 5
        if self.direction == 5:
            ispass = False
            if self.ypos < self.target:
                self.ypos += 3
                if self.ypos > self.target:
                    ispass = True
            else:
                self.ypos -= 3
                if self.ypos < self.target:
                    ispass = True
            if ispass:
                self.direction = 1

        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y


class cboss3(cship):

    # This class is used by the third boss

    SPRITESIZE_X = 100
    SPRITESIZE_Y = 110

    direction = True
    fire = False

    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.xpos = xmax
        self.ypos = 300
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y
        self.health = 40

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''

        if self.xpos < 550:
            if self.ypos < 100:
                self.direction = True

            if self.ypos > 450:
                self.direction = False

            if self.ypos < 175 or self.ypos > 375:
                self.fire = True
            else:
                self.fire = False

            if self.direction:
                self.ypos += 3
            else:
                self.ypos -= 3
        else:
            self.xpos -= 1
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y


class cboss4(cship):

    # This class is used for the fourth boss

    SPRITESIZE_X = 100
    SPRITESIZE_Y = 110

    direction = 1

    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.xpos = xmax
        self.ypos = 300
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y
        self.health = 50

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''

        if self.xpos < 550:
            if self.direction == 1:
                self.ypos -= 3
                if self.ypos < 100:
                    self.direction = 2
            if self.direction == 2:
                self.xpos -= 5
                if self.xpos < 100:
                    self.direction = 3
            if self.direction == 3:
                self.xpos += 4
                if self.xpos > 550:
                    self.direction = 4
            if self.direction == 4:
                self.ypos += 3
                if self.ypos > 450:
                    self.direction = 5
            if self.direction == 5:
                self.xpos -= 5
                if self.xpos < 100:
                    self.direction = 6
            if self.direction == 6:
                self.xpos += 4
                if self.xpos > 550:
                    self.direction = 1
        else:
            self.xpos -= 2
        self.ocxpos = self.xpos + self.SPRITESIZE_X
        self.ocypos = self.ypos + self.SPRITESIZE_Y


class cbossf(cship):

    # A class for the final boss

    done = False
    direction = 1

    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.xpos = xmax
        self.ypos = 300

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''

        self.xpos -= 1
        if self.xpos < 400:
            self.done = True


class claser(cfreebody):

    # A class for laser weapons

    show = False

    def refresh(self, xpos, ypos):
        '''(int, int) -> Nonetype
        A refresh function that must be ran during every frame.
        The two int parameters are the new coordinates of the laser.
        Returns NoneType.
        '''

        self.xpos = xpos
        self.ypos = ypos


class cstar:

    # A class for background stars

    xcors = []
    ycors = []
    spd = []
    stars = 0

    def __init__(self, stars, xmax, ymax):
        import random
        random.seed()
        self.xmax = xmax
        self.ymax = ymax
        self.stars = stars
        for i in range(0, stars):
            self.xcors.append(random.randint(1, (self.xmax-1)))
            self.ycors.append(random.randint(1, (self.ymax-1)))
            self.spd.append(random.randint(3, 15))

    def refresh(self):
        '''(NoneType) -> Nonetype
        A refresh function that must be ran during every frame.
        Returns NoneType.
        '''

        import random
        random.seed()

        for i in range(0, self.stars):
            self.xcors[i] = self.xcors[i] - self.spd[i]
            if self.xcors[i] < 0:
                self.xcors[i] = self.xmax
                self.ycors[i] = random.randint(1, (self.ymax-1))
                self.spd[i] = random.randint(3, 15)
