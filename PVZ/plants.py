import arcade
import time
from animate import Animate
from items import *

def cal_cent_x(x):
    x -= 248
    cell_number = x // 78
    new_x = cell_number * 78 + 248 + 39
    return(new_x, cell_number)

def cal_cent_y(y):
    y -= 24
    cell_number = y // 100
    new_y = cell_number * 100 + 24 + 50
    return(new_y, cell_number)


class Plants(Animate):
    def __init__ (self, cost, hp, image, window):
        super().__init__(image, 0.11)
        self.cost = cost
        self.hp = hp
        self.window = window
    
    def update(self):
        self.dam_p = arcade.check_for_collision_with_list(self, self.window.zombies)

        for zombie in self.dam_p:
            self.hp -= zombie.damage

        if self.hp <= 0:
            self.kill()

class SunFlower(Plants):
    def __init__(self, window):
        super().__init__(50,80, "plants/sun1.png", window)
        self.timer = time.time()
        self.textures = []
        self.window = window
        for i in range (2):
            self.textures.append(arcade.load_texture(f'plants/sun{i+1}.png'))

    def update(self):
        super().update()
        if time.time() - self.timer > 10:
            self.window.suns.append(SunMoney(self.center_x, self.center_y + 20))
            self.timer = time.time()
        
class PeaShooter(Plants):
    def __init__(self, window):
        super().__init__(100,100, "plants/pea1.png", window)
        self.timer = time.time()
        self.textures = []
        self.window = window
        for i in range (3):
            self.textures.append(arcade.load_texture(f'plants/pea{i+1}.png'))
        
    def update(self):
        super().update()
        if time.time() - self.timer > 2:
            self.window.peas.append(Bullet(self.center_x + 20, self.center_y + 20))
            self.timer = time.time()
            self.window.peas_sound.play (0.6,0,False)


class WallNut(Plants):
    def __init__(self, window):
        super().__init__(50, 275, "plants/nut1.png", window)
        self.textures = []

        for i in range (3):
            self.textures.append(arcade.load_texture(f'plants/nut{i+1}.png'))


class TorchWood(Plants):
    def __init__(self, window):
        super().__init__(175,120, "plants/tree1.png", window)       
        self.textures = []


        for i in range (3):
            self.textures.append(arcade.load_texture(f'plants/tree{i+1}.png'))

    def update(self):
        super().update()
        self.hit = arcade.check_for_collision_with_list(self, self.window.peas)
        for pea in self.hit:
            pea.texture = arcade.load_texture("items/firebul.png")
            pea.damage = 75
        
