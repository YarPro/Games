import arcade
import math

class Bullet(arcade.Sprite):
    def __init__(self, x, y, image):
        super().__init__(image, 0.12)
        self.change_x = 10
        self.change_y = 10
        if image == "images//green_bullet.png":
            self.friendly = True
        else:
            self.friendly = False
        self.set_position(x, y)
    
    def update(self):
        self.part_x = math.cos(math.radians(self.angle))
        self.part_y = math.sin(math.radians(self.angle))
        self.center_x += self.part_x * self.change_x
        self.center_y += self.part_y * self.change_y