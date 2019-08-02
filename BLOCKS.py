import pygame as pg 
import random
import sys

pg.init()

fps=pg.time.Clock()

#display Initialozations

WIDTH=800
HEIGHT=800
player_size=50
player_pos=[WIDTH/2,HEIGHT-2*player_size]

enemy_size=50
enemy_pos=[random.randint(0,WIDTH-enemy_size),0]
enemy_list=[enemy_pos]

speed=10
score=0

screen=pg.display.set_mode((HEIGHT,WIDTH))

my_font=pg.font.SysFont("monospace",35)


def drop_enemies(enemy_list):
	delay =random.random()
	if len(enemy_list)<10 and delay < 0.1:
		x_pos=random.randint(0,WIDTH-enemy_size)
		y_pos=0
		enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
			pg.draw.rect(screen,(0,0,255),(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

def update_enemy_pos(enemy_list,score):

	for idx,enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1]<HEIGHT:
			enemy_pos[1] +=speed
		else:
			enemy_list.pop(idx)
			score +=1
	return score

def collision_check(enemy_list,player_pos):
	for enemy_pos in enemy_list:
		if collision_detect(player_pos,enemy_pos):
			return True

	return False



#collison detection

def collision_detect(player_pos,enemy_pos):

	p_x=player_pos[0]
	p_y=player_pos[1]

	e_x=enemy_pos[0]
	e_y=enemy_pos[1]

	if (e_x>=p_x and e_x <(p_x+player_size)) or (p_x >=e_x and p_x <(e_x+enemy_size)):
		if(e_y>=p_y and e_y<(p_y+player_size)) or (p_y >=e_y and p_y < (e_y+enemy_size)):
			return True
	return False

# main loop 

game_over= False 


while not game_over:

	for event in pg.event.get():

		if event.type==pg.QUIT:

			sys.exit()

		if event.type==pg.KEYDOWN:

			x=player_pos[0]
			y=player_pos[1]

			if event.key==pg.K_LEFT:
				x-= player_size
			elif event.key==pg.K_RIGHT:
				x+= player_size

			player_pos=[x,y]

	
	
	
	screen.fill((0,0,0))

	
	pg.draw.rect(screen,(255,0,0),(player_pos[0],player_pos[1],player_size,player_size))

	
	drop_enemies(enemy_list)
	score=update_enemy_pos(enemy_list,score)
	print(score)
	if collision_check(enemy_list,player_pos):
		game_over=True

	text="SCORE:"+str(score)
	label=my_font.render(text,1,(255,255,0))
	screen.blit(label,(WIDTH-200,HEIGHT-40))

	draw_enemies(enemy_list)


	



	fps.tick(30)

	pg.display.update()


    
    




