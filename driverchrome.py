import pygame
from random import randint

pygame.init()
screen=pygame.display.set_mode((430,600))
pygame.display.set_caption("plappy bird")#khai bao ten tro choi
clock=pygame.time.Clock()
WHITE=(255,255,255)
RED=(255,0,0)
score=0
pausing=False

font=pygame.font.SysFont('san',20)
font1=pygame.font.SysFont('san',30)
font2=pygame.font.SysFont('san',35)

x_bird=50
y_bird=350
bird_img=pygame.image.load('bird.png')
bird_img=pygame.transform.scale(bird_img,(35,35)) #khai bao anh chim
d_2tube = 180 #setup kich thuc anh?
bird_drop_velocity=5
gravity=0.5
tube_velocity=2



tube1_x=400
tube2_x=600
tube3_x=800
tube_width=50
tube1_height=randint(80,420)
tube2_height=randint(80,420)
tube3_height=randint(80,420)

tube_img=pygame.image.load('tube.png')
sand_img=pygame.image.load('sand.png')
sand_img=pygame.transform.scale(sand_img,(400,20))



tube_op_img=pygame.image.load('tube_op.png')
#dua am thanh
sound1 = pygame.mixer.Sound('tick.wav')





background_img=pygame.image.load('background.png')
background_img=pygame.transform.scale(background_img,(430,600))
running=True

tube1_pass=False
tube2_pass=False
tube3_pass=False

while running:
    
    clock.tick(60)
    screen.fill(WHITE)
    screen.blit(background_img,(0,0))
    sand=screen.blit(sand_img,(0,580))
    tube1_img=pygame.transform.scale(tube_img,(tube_width,tube1_height))
    tube1=screen.blit(tube1_img,(tube1_x,0))
    tube2_img=pygame.transform.scale(tube_img,(tube_width,tube2_height))
    tube2=screen.blit(tube2_img,(tube2_x,0))
    tube3_img=pygame.transform.scale(tube_img,(tube_width,tube3_height))
    tube3=screen.blit(tube3_img,(tube3_x,0)) 
#ep anh ong doi dien
    tube1_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube1_height+d_2tube)))
    tube1_op=screen.blit(tube1_op_img,(tube1_x,tube1_height+d_2tube))
    tube2_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube2_height+d_2tube)))
    tube2_op=screen.blit(tube2_op_img,(tube2_x,tube2_height+d_2tube))
    tube3_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube3_height+d_2tube)))
    tube3_op=screen.blit(tube3_op_img,(tube3_x,tube3_height+d_2tube))
    #ong di chuyen xang trai
    tube1_x-=tube_velocity
    tube2_x-=tube_velocity
    tube3_x-=tube_velocity
    #tao ong moi
    if tube1_x<-tube_width:
        tube1_x=550
        tube1_height=randint(80,420)
        tube1_pass=False
    if tube2_x<-tube_width:
        tube2_x=550
        tube2_height=randint(80,420)
        tube2_pass=False
    if tube3_x<-tube_width:
        tube3_x=550
        tube3_height=randint(80,420)
        tube3_pass=False
    
    
    #ve cat
   



    bird=screen.blit(bird_img,(x_bird,y_bird)) #dua chim vao man hinhg
    y_bird=y_bird+bird_drop_velocity
    bird_drop_velocity=bird_drop_velocity+gravity
    #ghi diem
    score_txt=font.render("Score:"+str(score),True,RED)
    screen.blit(score_txt,(5,5))
    #chym qua ong
    if tube1_x+tube_width<=x_bird and tube1_pass==False:
        score+=1
        tube1_pass=True
        pygame.mixer.Sound.play(sound1) 
    if tube2_x+tube_width<=x_bird and tube2_pass==False:
        score+=1
        tube2_pass=True
        pygame.mixer.Sound.play(sound1)
    if tube3_x+tube_width<=x_bird and tube3_pass==False:
        score+=1
        tube3_pass=True
        pygame.mixer.Sound.play(sound1)

    #kiem tra va tram
    tubes=[tube1,tube2,tube3,tube1_op,tube2_op,tube3_op,sand]
    for tube in tubes:
        if bird.colliderect(tube):
            pygame.mixer.pause()
            tube_velocity=0
            bird_drop_velocity=0
            game_over_txt=font1.render("game over,score"+str(score),True,RED)
            screen.blit(game_over_txt,(125,260))
            space_txt=font2.render("nhan dau cach de tiep tuc",True,RED)
            screen.blit(space_txt,(80,280))
           
            pausing=True

    
    


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                

               

                bird_drop_velocity=0
                bird_drop_velocity=bird_drop_velocity-9
          

                if pausing:
                    pygame.mixer.unpause()
                    x_bird=50
                    y_bird=350
                    tube1_x=400
                    tube2_x=600
                    tube3_x=800
                    tube_velocity=2
                    score=0
                    pausing=False

             

    pygame.display.flip()



pygame.quit()