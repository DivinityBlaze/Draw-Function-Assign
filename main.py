import pygame

# Function to draw a pair-colored rectangle
def drawRect(color1, color2, x, y, width, height):
    pygame.draw.rect(screen, color1, [x, y, width, height])
    pygame.draw.rect(screen, color2, [x, y - height, width, height])

# Function to depict a stickman figure
def drawStickman(color, x, y):
    # Draw the head
    pygame.draw.circle(screen, color, (x, y), 10)
    # Draw the body
    pygame.draw.line(screen, color, (x, y + 10), (x, y + 30), 2)
    # Draw the arms
    pygame.draw.line(screen, color, (x, y + 15), (x - 10, y + 25), 2)
    pygame.draw.line(screen, color, (x, y + 15), (x + 10, y + 25), 2)
    # Draw the legs
    pygame.draw.line(screen, color, (x, y + 30), (x - 10, y + 40), 2)
    pygame.draw.line(screen, color, (x, y + 30), (x + 10, y + 40), 2)

# Screen settings
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rubayats thingy")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Main loop
done = False
clock = pygame.time.Clock()

# Main event loop
while not done:  # Primary game loop
    for event in pygame.event.get():  # Check for user input
        if event.type == pygame.QUIT:  # Handle user clicking close
            done = True  # Set flag indicating we're done, exiting loop
    screen.fill(WHITE)  # Fill screen with white color

    # Drawing colored rectangles
    drawRect(BLACK, BLUE, 100, 100, 200, 10)
    drawRect(BLACK, BLUE, 200, 200, 300, 50)
    drawRect(BLACK, BLUE, 300, 300, 200, 10)

    # Drawing stickmen figures
    drawStickman(RED, 400, 150)
    drawStickman(RED, 200, 350)
    drawStickman(RED, 600, 300)

    pygame.display.flip()  # Update screen display
    clock.tick(60)  # Cap frame rate to 60 frames per second

# Quit Pygame
pygame.quit()