import pygame
import sys
import math

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)

# Default drawing settings
current_color = BLACK
brush_size = 5
mode = "line"

# Shape drawing functions
def draw_circle(surface, color, position, radius):
    pygame.draw.circle(surface, color, position, radius, 2)

def draw_rect(surface, color, start_pos, end_pos):
    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.rect(surface, color, rect, 2)

def draw_square(surface, color, start_pos, end_pos):
    # Calculate side length from the smallest side
    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
    rect = pygame.Rect(start_pos, (side, side))
    pygame.draw.rect(surface, color, rect, 2)

def draw_right_triangle(surface, color, start_pos, end_pos):
    x1, y1 = start_pos
    x2, y2 = end_pos
    points = [(x1, y1), (x2, y2), (x1, y2)]
    pygame.draw.polygon(surface, color, points, 2)

def draw_equilateral_triangle(surface, color, start_pos, end_pos):
    x1, y1 = start_pos
    x2, y2 = end_pos
    side = abs(x2 - x1)
    height = int(side * math.sqrt(3) / 2)
    points = [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - height)]
    pygame.draw.polygon(surface, color, points, 2)

def draw_rhombus(surface, color, start_pos, end_pos):
    x1, y1 = start_pos
    x2, y2 = end_pos
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(surface, color, points, 2)

# Main loop variables
drawing = False
start_pos = None

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Start drawing on mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Draw the shape on mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                if mode == "rect":
                    draw_rect(screen, current_color, start_pos, end_pos)
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    draw_circle(screen, current_color, start_pos, radius)
                elif mode == "square":
                    draw_square(screen, current_color, start_pos, end_pos)
                elif mode == "right_triangle":
                    draw_right_triangle(screen, current_color, start_pos, end_pos)
                elif mode == "equilateral_triangle":
                    draw_equilateral_triangle(screen, current_color, start_pos, end_pos)
                elif mode == "rhombus":
                    draw_rhombus(screen, current_color, start_pos, end_pos)
            drawing = False

        # While moving the mouse and holding click in "line" mode, draw freehand
        if event.type == pygame.MOUSEMOTION and drawing and mode == "line":
            pygame.draw.line(screen, current_color, start_pos, event.pos, brush_size)
            start_pos = event.pos

        # Keyboard shortcuts to change mode or color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_l:
                mode = "line"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_e:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_b:
                current_color = BLACK
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_p:
                current_color = RED
            elif event.key == pygame.K_o:
                current_color = BLUE
            elif event.key == pygame.K_w:
                current_color = WHITE  # eraser

    pygame.display.flip()
