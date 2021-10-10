import pygame
import random
from math import pi

pygame.init()

# Screen size and colours
WIDTH, HEIGHT = 500, 650
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
SKY_BLUE = (135, 206, 235)

# Font used
font = pygame.font.SysFont("helvetica", 20, bold = True)

FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pi estimation using Monte Carlo")
clock = pygame.time.Clock()

# Some derived constants to determine location of the shapes
SIDE = WIDTH - WIDTH // 10
START_X = WIDTH // 20
START_Y = WIDTH // 20
END_X = START_X + SIDE
END_Y = START_Y + SIDE
RADIUS = SIDE // 2
CENTRE = (START_X + SIDE // 2, START_Y + SIDE // 2)

# The variables to be used to estimate pi.
in_points = 0
total_points = 0

def draw_screen():
    rectangle = pygame.Rect(START_X, START_Y, SIDE, SIDE)
    pygame.draw.rect(screen, GREEN, rectangle, 2)
    pygame.draw.circle(screen, YELLOW, CENTRE, RADIUS, 2)

# Plot a single pixel within the boundaries of a square.
def draw_points(num):
    global total_points, in_points

    for _ in range(num):
        x = random.uniform(START_X, END_X)
        y = random.uniform(START_X, END_X)

        cx, cy = CENTRE
        colour = SKY_BLUE

        # Find the distance between the random point and the centre of the circle
        distance = (cx - x) ** 2 + (cy - y) ** 2

        # If the distance is less than the radius, it lies within the circle.
        if distance < RADIUS ** 2:
            in_points += 1
            colour = RED

        pygame.draw.line(screen, colour, (x, y), (x, y))
        #pygame.draw.circle(screen, colour, (int(x), int(y)), 1)
        total_points += 1
    
    calculated_pi = 4 * (in_points / total_points)
    error = abs(pi - calculated_pi) / pi * 100

    # Draw a black box below the square for text-output purposes.
    # Gives the illusion of the text being refreshed.
    text_box = pygame.Rect(10, END_Y + 1, WIDTH, HEIGHT)
    pygame.draw.rect(screen, BLACK, text_box)

    pi_expression = "Estimated pi = " + str(calculated_pi)
    err_text = font.render("Error = {:.4f}%".format(error), True, WHITE)
    label = font.render(pi_expression, 2, WHITE)

    screen.blit(label, (20, END_Y + 20))
    screen.blit(err_text, (20, END_Y + 40))

# Draw the initial screen (square + circle)
draw_screen()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Change the parameter for faster drawing.
    draw_points(10)
    
    pygame.display.update()

pygame.quit()