import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) #topleft 0,0, go right needs increasing x, go downward increasing y
pygame.display.set_caption('Runner game')
clock = pygame.time.Clock() #C capital
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # need to deal with alpha values
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True: # loop to make the excutable window runnining constant
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print('key up')
        
        # two different methods for input?
        # when using classes you want the controls inside of the relevant class. pygame.mouse
        # and pygame.keys are great for that
    
    screen.blit(sky_surface,(0,0)) # blit, moving the colored object according to the coordinate //offsets     
    screen.blit(ground_surface,(0,300)) # order of excution matters sky -> ground
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
    # pygame.draw.line(screen, 'Gold',(0,0),pygame.mouse.get_pos(),10)
    # pygame.draw.ellipse(screen, 'Brown',pygame.Rect(50,200,100,100))

    screen.blit(score_surf,score_rect)

    #print(player_rect.left) 
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')


    # if player_rect.colliderect(snail_rect):
    #     print('collision')  # collide then 1, no then 0
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())



    # draw all our element
    # update everything
    pygame.display.update()
    clock.tick(60) # FPS set to 60 60 frames per second