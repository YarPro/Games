
import arcade
import math
import time
from our_tank import *
from bullet import *



class Enemy(arcade.Sprite):
    def __init__(self, window, texture):
        super().__init__(texture, 0.12)
        self.change_x = 2
        self.change_y = 2
        self.window = window
        self.hp = 3
        self.time_to_reshoot = time.time()
    
    def move_to_target(self):
        self.part_x = math.cos(math.radians(self.angle))
        self.part_y = math.sin(math.radians(self.angle))
        self.center_x += self.part_x * self.change_x
        self.center_y += self.part_y * self.change_y
    
    def update(self):
        if self.hp <= 0:
            self.texture = arcade.load_texture("images//red_broken.png")
        else:
            if arcade.get_distance_between_sprites(self.window.player, self) < 300 and self.window.player.hp > 0:
                if arcade.get_distance_between_sprites(self.window.player, self) > 100:
                    self.move_to_target()
                self.rotate_to_player() 
                self.shoot()
            elif arcade.get_distance_between_sprites(self.window.green_base, self) < 400:
                self.rotate_to_base()
                self.shoot()
            else:
                self.angle = 180
                self.move_to_target()
            self.hit = arcade.check_for_collision_with_list(self, self.window.bullets)
            for hit in self.hit:
                if hit.friendly:
                    self.hp -= 1
                    hit.kill()
        for tank in self.window.enemy:
            self.collision(tank)
        self.collision(self.window.player)

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
        if time.time() - self.time_to_reshoot >= 6:
                self.bullet = Bullet(self.center_x, self.center_y, "images//red_bullet.png")
                self.bullet.angle = self.angle
                self.window.bullets.append(self.bullet)
                self.time_to_reshoot = time.time()
    
    def rotate_to_player(self):
        delta_x = self.window.player.center_x - self.center_x
        delta_y = self.window.player.center_y - self.center_y
        self.angle = math.degrees(math.atan2(delta_y, delta_x))
    
    def rotate_to_base(self):
        delta_x = self.window.green_base.center_x - self.center_x
        delta_y = self.window.green_base.center_y - self.center_y
        self.angle = math.degrees(math.atan2(delta_y, delta_x))

    #def draw(self):
    #    super().draw()
    #    arcade.draw_rectangle_outline(self.center_x, self.center_y + 35, 30, 10, arcade.color.BLACK)
    #    arcade.draw_rectangle_filled(self.center_x - ((3 - self.hp) * 3), self.center_y + 35, 10 * self.hp, 9, arcade.color.DARK_GREEN)