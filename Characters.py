class Character:
    charX = None
    charY = None
    charImg = None
    moveSpeed = None
    HP = None

    def act():
        pass

    def adjustHP(change):
        HP = HP + change

class Player(Character):
    charX = 10
    charY = 10
    charImg = "#"
    moveSpeed = 1
    HP = 100

    def act(input):
        if input == "w":
            playery -= moveSpeed
        elif input =="a":
            playerx -= moveSpeed
        elif input =="s":
            playery += moveSpeed
        elif input =="d":
            playerx += moveSpeed

class Enemy(Character):
    charX = 7
    charY = 7
    charImg = "$"
    moveSpeed = 1
    HP = 70

    def Act():
        pass