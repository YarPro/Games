
import arcade
import random
from animate import Animate
from plants import cal_cent_y
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Zombies(Animate):
    def __init__(self, image, y, hp, damage, speed, window):
        super().__init__(image, 0.1)
        self.set_position(SCREEN_WIDTH + 75, y)
        self.hp = hp
        self.damage = damage
        self.change_x = speed
        self.window = window
        self.is_walk = True
    
    def update(self):
        self.dam_z = arcade.check_for_collision_with_list(self, self.window.peas)
        for pea in self.dam_z:
            self.hp -= pea.damage
            pea.kill()

        self.dam_z = arcade.check_for_collision_with_list(self, self.window.plants)


        self.is_walk = True

        for plant in self.dam_z:
            plant.hp -= self.damage 
            self.is_walk = False
        
        if self.is_walk == True:
            self.center_x -= self.change_x 

        if self.hp <= 0:
            
            self.kill()
            return True

class Default_Z(Zombies):
    def __init__(self, window):
        super().__init__("zombies/zom1.png", cal_cent_y(random.randint(30, SCREEN_HEIGHT - 150))[0], 500, 0.08, 0.3, window)
        for i in range (2):
            self.textures.append(arcade.load_texture(f'zombies/zom{i+1}.png'))

class Conus_Z(Zombies):
    def __init__(self, window):
        super().__init__("zombies/cone1.png", cal_cent_y(random.randint(30, SCREEN_HEIGHT - 150))[0], 750, 0.08, 0.3, window)
        self.textures = []
        for i in range (2):
            self.textures.append(arcade.load_texture(f'zombies/cone{i+1}.png'))

class Bucket_Z(Zombies):
    def __init__(self, window):
        super().__init__("zombies/buck1.png", cal_cent_y(random.randint(30, SCREEN_HEIGHT - 150))[0], 1500, 0.08, 0.3, window)
        self.textures = []
        for i in range (2):
            self.textures.append(arcade.load_texture(f'zombies/buck{i+1}.png'))

class Big_Z(Zombies):
    def __init__(self, window):
        super().__init__("zombies/buck1.png", cal_cent_y(random.randint(30, SCREEN_HEIGHT - 150))[0], 7500, 0.08, 0.5, window)
        self.textures = []
        for i in range (1):
            self.textures.append(arcade.load_texture(f'zombies/big{i+1}.png'))