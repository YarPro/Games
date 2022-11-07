import arcade

class Base(arcade.Sprite):
    def __init__(self, filename, window, friendship):
        super().__init__(filename, 1.7)
        self.window = window
        self.hp = 5
        self.friendship = friendship

    def update(self, friendship):
        self.friendship = friendship
        self.hit = arcade.check_for_collision_with_list(self, self.window.bullets)
        for hit in self.hit:
            if self.friendship == False:
                self.window.red_base.hp -= 1
            elif self. friendship == True:
                self.window.green_base.hp -= 1
            hit.kill()
        if self.hp <= 0:
            self.kill()

        
        if arcade.check_for_collision(self, self.window.player):
            if 0 < self.window.player.top - self.bottom < 10:
                self.window.player.top = self.bottom
            elif 0 < self.top - self.window.player.bottom < 10:
                self.window.player.bottom = self.top
            elif 0 < self.window.player.right - self.left < 10:
                self.window.player.right = self.left
            elif 0 < self.right - self.window.player.left < 10:
                self.window.player.left = self.right
    
    def draw(self):
        super().draw()
        if self.hp > 0:
            arcade.draw_rectangle_outline(self.center_x, self.center_y + 300, 250, 15, arcade.color.BLACK)
            arcade.draw_rectangle_filled(self.center_x - ((5 - self.hp) * 25), self.center_y + 300, 50 * self.hp, 14, arcade.color.DARK_GREEN)
        