import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)

current_color = BLACK
brush_size = 5
mode = "line"

def draw_circle(surface, color, position, radius):
    pygame.draw.circle(surface, color, position, radius)

def draw_rect(surface, color, start_pos, end_pos):
    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.rect(surface, color, rect, 2)

drawing = False
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                if mode == "rect":
                    draw_rect(screen, current_color, start_pos, end_pos)
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    draw_circle(screen, current_color, start_pos, radius)
            drawing = False
        
        if event.type == pygame.MOUSEMOTION and drawing and mode == "line":
            pygame.draw.line(screen, current_color, start_pos, event.pos, brush_size)
            start_pos = event.pos
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_l:
                mode = "line"
            elif event.key == pygame.K_e:
                current_color = WHITE
            elif event.key == pygame.K_b:
                current_color = BLACK
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_p:
                current_color = RED
            elif event.key == pygame.K_o:
                current_color = BLUE
            
    pygame.display.flip()
