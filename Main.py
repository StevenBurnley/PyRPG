#!/usr/bin/env python2.7-32

import os
import pygame

from MapUtil import genMap, drawMap
from Objects import *
from Characters import Player
from Characters import Enemy


player = Player()
pygame.init()


genMap()
#while True:
keys = pygame.key.get_pressed()

while not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
    pass

if keys[pygame.K_w]:
    player.act(w)

elif keys[pygame.K_s]:
    player.act(s)

elif keys[pygame.K_a]:
    player.act(a)

elif keys[pygame.K_d]:
    player.act(d)
