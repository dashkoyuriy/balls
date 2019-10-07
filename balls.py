import pygame
import random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface(screen.get_size())

clock = pygame.time.Clock()
MYEVENTTYPE = 1
pygame.time.set_timer(MYEVENTTYPE, 10)

running = True
radius = 10
circle = []
circle_color = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            circle.append(list((x1, y1)))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            circle_color.append((r, g, b))
            pygame.draw.circle(screen, (r, g, b), (x1, y1), radius)
            pygame.display.flip()
        if event.type == MYEVENTTYPE:
            screen2.blit(screen, (0, 0))
            for i in range(len(circle)):
                pygame.draw.circle(screen2, (0, 0, 0), tuple(circle[i]), radius)
                circle[i][1] += 1
                if circle[i][1] + radius <= height:
                    pygame.draw.circle(screen2, circle_color[i], tuple(circle[i]), radius)
                else:
                    pygame.draw.circle(screen2, circle_color[i], (circle[i][0], height - radius), radius)
            screen.blit(screen2, (0, 0))
            pygame.display.flip()
pygame.quit()