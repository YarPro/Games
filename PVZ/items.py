import arcade
import time
from constants import *
from plants import *

class Bullet(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__("items//bul.png", 0.12)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 4
        self.damage = 50
    
    def update(self):
        self.center_x += self.change_x

        if self.right >= SCREEN_WIDTH:
            self.kill()

class SunMoney(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__("items//sun.png", 0.12)
        self.center_x = center_x
        self.center_y = center_y
        self.change_y = 0.5
        self.timer = time.time()

    def update(self):
        self.center_y -= self.change_y
        self.angle += 1
        if time.time() - self.timer > 5:
            self.kill()
            self.timer = 0

class SunsFall(SunMoney):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y)
    
    def update(self):
        self.center_y -= self.change_y
        self.angle += 1
        if self.top < 0:
            self.kill()
            self.timer = 0
        

        


    