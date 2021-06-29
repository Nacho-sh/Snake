import pygame
import random
import time
from variables import size, BLACK, run, i, last_move, tail, GREEN, RED, head_pos, moves
last_pos = [head_pos[0], head_pos[1]]
class Food(pygame.sprite.Sprite, object):
    global tail
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1, 39) * 15, random.randint(1, 39) * 15)
        valid = False
        u = 0

                    


class Body(pygame.sprite.Sprite):
    global count, moves, tail, last_pos, run
    def __init__(self, position, HEAD):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = position
        if HEAD == True:
            self.image = pygame.image.load("head.png").convert_alpha()
        else:
            self.image.fill(RED)
        

    def move_right(self):
        if len(moves) < count:
            moves.insert(0, last_move) 
        if count > 0:
            tail_mover()
        self.rect.x += 15
        head_pos[0] += 15 
        if count == 0:
            last_pos[0] += 15
        if head_pos[0] > 750:
            pygame.quit()

    def move_left(self):
        if len(moves) < count:
            moves.insert(0, last_move)
        if count > 0:
            tail_mover()
        self.rect.x -= 15
        head_pos[0] -= 15 
        if count == 0:
            last_pos[0] -= 15
        if head_pos[0] < 0:
            pygame.quit()




    def move_up(self):
        if len(moves) < count:
            moves.insert(0, last_move)
        if count > 0:
            tail_mover()
        self.rect.y -= 15
        head_pos[1] -= 15 
        if count == 0:
                last_pos[1] -= 15
        if head_pos[1] < 0:
            pygame.quit()






    def move_down(self):
        if len(moves) < count:
            moves.insert(0, last_move)
        if count > 0:
            tail_mover()
        self.rect.y += 15
        head_pos[1] += 15
        if count == 0:
            last_pos[1] += 15
        if head_pos[1] > 600:
            pygame.quit()




    def tail_right(self):
        self.rect.x += 15
        

        
    def tail_left(self):
        self.rect.x -= 15
        

        
    def tail_up(self):
        self.rect.y -= 15

        
    def tail_down(self):
        self.rect.y += 15


last_dir = 0
def tail_mover():
    global count, moves, tail, last_move, last_pos, last_dir
    u = 0
    while u < count:
        if moves[u] == "down":
            tail[u].tail_down()
            

        elif moves[u] == "up":
            tail[u].tail_up()
            
            
        elif moves[u] == "right":
            tail[u].tail_right()
            

        else:
            tail[u].tail_left()
            

        u = u + 1

    if moves[-1] == "down":
        last_pos[1] = last_pos[1] + 15
        last_dir = "down"
    elif moves[-1] == "up":
        last_pos[1] = last_pos[1] - 15
        last_dir = "up"
    elif moves[-1] == "right":
        last_pos[0] = last_pos[0] + 15
        last_dir = "right"
    else:
        last_pos[0] = last_pos[0] - 15
        last_dir = "left"
    moves.pop()



count = 0
screen = pygame.display.set_mode(size)
def title():
    if count > 0:
        pygame.display.set_caption("Snake    Score:" + str(count))
    else:
        pygame.display.set_caption("Snake    Score: 0")

clock = pygame.time.Clock()
all_sprites_list = pygame.sprite.Group()

grow_dir = last_move

body_list = pygame.sprite.Group()

def grow():
    global count, tail, last_pos, moves, last_dir
    if count > 0:
        if last_dir == "down":
            tail.append(Body((last_pos[0], last_pos[1] - 15), False))
            last_pos[1] = last_pos[1] - 15
            moves.append(last_dir)

        elif last_dir == "up":
            tail.append(Body((last_pos[0], last_pos[1] + 15), False))
            last_pos[1] = last_pos[1] + 15
            moves.append(last_dir)

        elif last_dir == "right":
            tail.append(Body((last_pos[0] - 15, last_pos[1]), False))
            last_pos[0] = last_pos[0] - 15
            moves.append(last_dir)

        else:
            tail.append(Body((last_pos[0] + 15, last_pos[1]), False))
            last_pos[0] = last_pos[0] + 15
            moves.append(last_dir)
    else:
        if last_move == "down":
            tail.append(Body((last_pos[0], last_pos[1] - 15), False))
            last_pos[1] = last_pos[1] - 15

        elif last_move == "up":
            tail.append(Body((last_pos[0], last_pos[1] + 15), False))
            last_pos[1] = last_pos[1] + 15

        elif last_move == "right":
            tail.append(Body((last_pos[0] - 15, last_pos[1]), False))
            last_pos[0] = last_pos[0] - 15

        else:
            tail.append(Body((last_pos[0] + 15, last_pos[1]), False))
            last_pos[0] = last_pos[0] + 15

    all_sprites_list.add(tail[count])
    body_list.add(tail[count])
    count = count + 1
    moves.insert(0, last_move)

    

def def_mov():
        if last_move == "left":
            head.move_left()
        elif last_move == "right":
            head.move_right()
        elif last_move == "up":
            head.move_up()
        elif last_move == "down":
            head.move_down()

head = Body((375, 300), True)
all_sprites_list.add(head)



new_food = Food()
all_sprites_list.add(new_food)
food_list = pygame.sprite.Group()
food_list.add(new_food)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run = False


    keys = pygame.key.get_pressed()
    


    if keys[pygame.K_LEFT] | keys[pygame.K_a]:
        if last_move != "right":
            head.move_left()
            last_move = "left"
        else:
            def_mov()
    elif keys[pygame.K_RIGHT] | keys[pygame.K_d]:
        if last_move != "left":
            head.move_right()
            last_move = "right"
        else:
            def_mov()
    elif keys[pygame.K_UP] | keys[pygame.K_w]:
        if last_move != "down":
            head.move_up()
            last_move = "up"
        else:
            def_mov()
    elif keys[pygame.K_DOWN] | keys[pygame.K_s]:
        if last_move != "up":
            head.move_down()
            last_move = "down"
        else:
            def_mov()
    else:
        def_mov()

        title()
    sprites_collide_list = pygame.sprite.spritecollide(head, food_list, False)
    for new_food in sprites_collide_list:
        sprites_collide_list.remove(new_food)
        food_list.remove(new_food)
        all_sprites_list.remove(new_food)
        new_food = Food()
        all_sprites_list.add(new_food)
        food_list.add(new_food)
        grow()

        
    
    body_collision_list = pygame.sprite.spritecollide(head, body_list, False)
    for head in body_collision_list:
        run = False
    
    x = 0
    if count > 0:
        food_inbody_list = pygame.sprite.spritecollide(tail[x], food_list, False)
        for x in tail:
            for tail[x] in food_inbody_list:
                new_food = Food()
                all_sprites_list.remove(new_food)
                food_list.remove(new_food)
                all_sprites_list.add(new_food)
                food_list.add(new_food)

    
    all_sprites_list.update()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    pygame.time.delay(100)
    clock.tick(60)



pygame.quit()