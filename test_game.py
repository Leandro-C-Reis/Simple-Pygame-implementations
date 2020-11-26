import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('My first Python Game')

clock  = pygame.time.Clock()

crashed = False
print('not Quited')
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == 768 and event.key == 8:
            crashed = True
        print(event)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()