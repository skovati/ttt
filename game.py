import pygame

pygame.init()

# side of square window
SIDE = 1000
# space between rectangles
SPACE = 15
# calculate size of rectanges from window size
SIZE = int((SIDE - (4*SPACE)) / 3)
# while rectangles
RECT_COLOR = (189,189,189)
RED = (244,67,54)
GREEN = (76,175,80)

# save window 
w = pygame.display.set_mode((SIDE, SIDE))

# title window
pygame.display.set_caption("ttt")

# 2d list to hold rectangle objects
rects = []
# initialize vert to SPACE
vert = SPACE
for row in range(3):
    # and horiz to SPACE each outer loop
    horiz = SPACE
    rects.append([])
    for col in range(3):
        # so that inside rectangles are drawn at horiz, vert, left to right, top to bottom
        rects[row].append(pygame.draw.rect(w, RECT_COLOR, (horiz, vert, SIZE, SIZE)))
        # increment positions
        horiz = horiz + SPACE + SIZE
    vert = vert + SPACE + SIZE

# boolean flag for game loop
running = True

player = 0

# main game loop
while running:

    pygame.time.delay(100)

    for event in pygame.event.get():
        # if exit button hit, quit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for row in rects:
                for rect in row:
                    if rect.collidepoint(pos):
                        if player == 0:
                            pygame.draw.rect(w, 
                                    RED,
                                    (rect.left + SPACE, rect.top + SPACE, SIZE-(2*SPACE), SIZE-(2*SPACE)))
                            player = 1
                        else:
                            pygame.draw.circle(w,
                                    GREEN,
                                    (rect.centerx, rect.centery), (SIZE/2)-SPACE)
                            player = 0

    # draw frame
    pygame.display.update()

# exit after game loop
pygame.quit()
