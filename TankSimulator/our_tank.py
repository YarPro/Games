import arcade
import math
from bullet import *

class Player(arcade.Sprite):
    def __init__(self, window):
        super().__init__("images/green.png", 0.12)
        self.set_position(100, 100)
        self.window = window
        self.hp = 5

    def update(self):
        self.angle += self.change_angle
        self.part_x = math.cos(math.radians(self.angle))
        self.part_y = math.sin(math.radians(self.angle))
        self.center_x += self.part_x * self.change_x
        self.center_y += self.part_y * self.change_y
        self.hit = arcade.check_for_collision_with_list(self, self.window.bullets)
        for hit in self.hit:
            if not hit.friendly:
                self.hp -= 1
                hit.kill()
        for tank in self.window.enemy:
            self.collision(tank)

    def collision(self, sprite):
        if arcade.check_for_collision(self, sprite):
            if 0 < abs(sprite.top - self.bottom) < 20:
                sprite.top = self.bottom
            elif 0 < abs(sprite.bottom - self.top) < 20:
                sprite.bottom = self.top
            elif 0 < abs(sprite.right - self.left) < 20:
                sprite.right = self.left
            elif 0 < abs(self.right - sprite.left) < 20:
                sprite.left = self.right

    def shoot(self):
        self.bullet = Bullet(self.center_x, self.center_y, "images//green_bullet.png")
        self.bullet.angle = self.angle
        self.window.bullets.append(self.bullet)
    
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 35, 50, 10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.center_x - ((5 - self.hp) * 5), self.center_y + 35, 10 * self.hp, 9, arcade.color.DARK_GREEN)
    

        